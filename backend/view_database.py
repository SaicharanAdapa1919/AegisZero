"""
AegisZero: Terminal Database CLI Viewer & Editor
Inspect, query, add, edit, or reset employee records in aegiszero_enterprise.db
"""

import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "aegiszero_enterprise.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def view_identities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT employee_id, name, email, current_role, drift_days, admin_keys, annual_waste_usd, access_status 
        FROM enterprise_identities
    """)
    rows = cursor.fetchall()
    conn.close()

    print("\n" + "=" * 115)
    print(f"{'ID':<10} {'NAME':<18} {'EMAIL':<30} {'ROLE':<20} {'DRIFT':<7} {'KEYS':<6} {'WASTE':<10} {'STATUS'}")
    print("=" * 115)
    for r in rows:
        waste_str = f"${r[6]:,.0f}" if r[6] else "$0"
        print(f"{r[0]:<10} {r[1]:<18} {r[2]:<30} {r[3]:<20} {str(r[4])+'d':<7} {str(r[5]):<6} {waste_str:<10} {r[7]}")
    print("=" * 115 + "\n")

def view_audit_logs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, audit_id, employee_id, action, annual_savings_usd, sha256_hash, timestamp FROM audit_logs")
    rows = cursor.fetchall()
    conn.close()

    print("\n" + "=" * 115)
    print(f"{'#':<4} {'AUDIT ID':<18} {'TARGET':<22} {'ACTION':<14} {'SAVINGS':<12} {'TIMESTAMP'}")
    print("=" * 115)
    if not rows:
        print("  (No audit logs yet. Run the swarm to generate audit entries!)")
    for r in rows:
        savings_str = f"${r[4]:,.0f}" if r[4] else "$0"
        print(f"{r[0]:<4} {r[1]:<18} {r[2]:<22} {r[3]:<14} {savings_str:<12} {r[6]}")
    print("=" * 115 + "\n")

def update_status(employee_id, new_status, new_admin_keys=0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE enterprise_identities 
        SET access_status = ?, admin_keys = ? 
        WHERE employee_id = ? OR email = ?
    """, (new_status, new_admin_keys, employee_id, employee_id))
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    if affected > 0:
        print(f"✅ Success: Updated {employee_id} to status='{new_status}', admin_keys={new_admin_keys}")
    else:
        print(f"❌ Error: Employee {employee_id} not found in database.")

def reset_all_to_baseline():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE enterprise_identities 
        SET access_status = 'PENDING_REVIEW', admin_keys = 3 
        WHERE drift_days > 0
    """)
    conn.commit()
    conn.close()
    print("🔄 Baseline Restored: Transferred employees set back to PENDING_REVIEW & admin_keys=3")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "view":
            view_identities()
        elif cmd == "audit":
            view_audit_logs()
        elif cmd == "reset":
            reset_all_to_baseline()
            view_identities()
        elif cmd == "set" and len(sys.argv) >= 4:
            emp_id = sys.argv[2]
            stat = sys.argv[3]
            keys = int(sys.argv[4]) if len(sys.argv) > 4 else 0
            update_status(emp_id, stat, keys)
            view_identities()
        else:
            print("Usage:")
            print("  python view_database.py view              # Show all employees")
            print("  python view_database.py audit             # Show immutable audit logs")
            print("  python view_database.py reset             # Reset records to baseline")
            print("  python view_database.py set EMP-101 REVOKED 0   # Change status")
    else:
        view_identities()
