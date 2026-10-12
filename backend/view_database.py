import os
import sys
import time

# Ensure Windows terminal doesn't crash on emojis
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Auto import db_manager
try:
    import db_manager
except ImportError:
    from backend import db_manager

def get_identities():
    return db_manager.fetch_all_identities()

def print_identities(identities):
    mode = db_manager.get_db_mode()
    print("\n" + "=" * 115)
    print(f"AEGISZERO ENTERPRISE DATABASE VIEWER | MODE: [{mode}]")
    print("=" * 115)
    print(f"{'EMP ID':<10} {'NAME':<18} {'EMAIL':<30} {'ROLE':<20} {'DRIFT':<7} {'KEYS':<6} {'STATUS'}")
    print("-" * 115)
    for r in identities:
        role = r.get("current_role") or r.get("role") or "N/A"
        drift = f"{r.get('drift_days', 0)}d"
        keys = str(r.get("admin_keys", 0))
        status = r.get("access_status", "UNKNOWN")
        print(f"{r.get('employee_id',''):<10} {r.get('name',''):<18} {r.get('email',''):<30} {role:<20} {drift:<7} {keys:<6} {status}")
    print("=" * 120 + "\n")

def view_identities():
    identities = get_identities()
    print_identities(identities)

def view_audit_logs():
    mode = db_manager.get_db_mode()
    print("\n" + "=" * 115)
    print(f"📜 AEGISZERO IMMUTABLE AUDIT LOGS | MODE: [{mode}]")
    print("=" * 115)
    if mode == "POSTGRES_CLOUD":
        import psycopg2
        from psycopg2.extras import RealDictCursor
        conn = psycopg2.connect(db_manager.DATABASE_URL, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM audit_logs ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
    else:
        import sqlite3
        conn = sqlite3.connect(db_manager.LOCAL_SQLITE_PATH)
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM audit_logs ORDER BY id DESC").fetchall()
        conn.close()

    print(f"{'ID':<6} {'AUDIT ID':<18} {'TARGET':<22} {'ACTION':<16} {'SAVINGS':<12} {'TIMESTAMP'}")
    print("-" * 115)
    if not rows:
        print("  (No audit logs recorded yet. Trigger remediation to generate SOC2 logs.)")
    for r in rows:
        r_dict = dict(r)
        savings = f"${r_dict.get('annual_savings_usd', 0):,.0f}"
        ts = str(r_dict.get("timestamp") or r_dict.get("created_at") or "")[:19]
        print(f"{str(r_dict.get('id','')):<6} {r_dict.get('audit_id',''):<18} {r_dict.get('employee_id',''):<22} {r_dict.get('action',''):<16} {savings:<12} {ts}")
    print("=" * 115 + "\n")

def watch_live(interval=3):
    print(f"👀 Live Watching Database every {interval}s... (Press Ctrl+C to stop)")
    last_snapshot = None
    try:
        while True:
            identities = get_identities()
            current_snapshot = [(r['employee_id'], r['access_status'], r['admin_keys']) for r in identities]
            if current_snapshot != last_snapshot:
                # Clear screen in terminal if possible
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"[LIVE UPDATE DETECTED at {time.strftime('%H:%M:%S')}]")
                print_identities(identities)
                last_snapshot = current_snapshot
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped live watching.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "view":
            view_identities()
        elif cmd == "watch":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 2
            watch_live(interval)
        elif cmd == "audit":
            view_audit_logs()
        elif cmd == "reset":
            mode = db_manager.get_db_mode()
            if mode == "POSTGRES_CLOUD":
                import psycopg2
                conn = psycopg2.connect(db_manager.DATABASE_URL)
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE enterprise_identities
                    SET access_status = 'PENDING_REVIEW',
                        admin_keys = CASE 
                            WHEN employee_id IN ('EMP-101', 'EMP-105') THEN 3 
                            WHEN employee_id IN ('EMP-102', 'EMP-103') THEN 1 
                            ELSE 0 
                        END
                    WHERE employee_id != 'EMP-104';
                """)
                conn.commit()
                conn.close()
            else:
                db_manager.init_database()
            print("🔄 Baseline Restored: Transferred employees set back to PENDING_REVIEW")
            view_identities()
        else:
            print("Usage:")
            print("  python view_database.py view              # Show all employees")
            print("  python view_database.py watch             # Live watch updates in real-time")
            print("  python view_database.py audit             # Show immutable audit logs")
            print("  python view_database.py reset             # Reset records to baseline")
    else:
        view_identities()
