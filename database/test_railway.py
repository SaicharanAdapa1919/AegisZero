"""
AegisZero: Railway Cloud Database Setup & Verification Tool
Tests connection to your live Railway PostgreSQL database and seeds the schema and employees.
"""

import os
import sys

def get_railway_url():
    # 1. Check environment variable
    url = os.getenv("DATABASE_URL")
    if url and "railway" in url or (url and "postgres" in url):
        return url
    
    # 2. Check local .env file
    env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                if line.strip().startswith("DATABASE_URL="):
                    return line.strip().split("DATABASE_URL=", 1)[1].strip().strip('"').strip("'")
    return None

def test_and_seed_railway(db_url: str):
    import psycopg2
    from psycopg2.extras import RealDictCursor

    print("=" * 70)
    print("[INFO] Connecting to Cloud PostgreSQL Database...")
    print("=" * 70)

    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        print("[OK] Connection Successful to Cloud PostgreSQL!")

        # Read schema.sql
        schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
        with open(schema_path, "r") as f:
            sql_script = f.read()

        print("[INFO] Applying schema and seeding employee records...")
        cursor.execute(sql_script)
        conn.commit()

        # Query records
        cursor.execute("SELECT employee_id, name, email, \"current_role\", access_status FROM enterprise_identities ORDER BY employee_id")
        rows = cursor.fetchall()
        print("\n" + "=" * 80)
        print("LIVE CLOUD DATABASE TABLE (enterprise_identities):")
        print("=" * 80)
        for r in rows:
            print(f"  {r[0]:<10} | {r[1]:<18} | {r[2]:<30} | {r[4]}")
        print("=" * 80)

        conn.close()
        print("\n[SUCCESS] Cloud Database is 100% Configured and Ready!")
        return True

    except Exception as e:
        print(f"\n[ERROR] Failed to connect: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        railway_url = sys.argv[1]
    else:
        railway_url = get_railway_url()

    if not railway_url:
        print("Usage:")
        print("  python test_railway.py \"postgresql://postgres:password@roundhouse.proxy.rlwy.net:PORT/railway\"")
        print("\nOr paste your Railway DATABASE_URL into the .env file.")
    else:
        test_and_seed_railway(railway_url)
