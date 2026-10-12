from http.server import BaseHTTPRequestHandler
import json

EMPLOYEES = [
    {
        "employee_id": "EMP-101",
        "name": "David Chen",
        "email": "david@gmail.com",
        "previous_role": "Payment Gateway",
        "current_role": "Internal Tooling",
        "drift_days": 75,
        "active_apps": "AWS Root, Figma Pro, Datadog Admin, GitHub",
        "monthly_cost": 1476.0,
        "admin_keys": 3,
        "annual_waste_usd": 17700.0,
        "access_status": "PENDING_REVIEW"
    },
    {
        "employee_id": "EMP-102",
        "name": "Sarah Jenkins",
        "email": "sarah.jenkins@company.com",
        "previous_role": "UI/UX Design",
        "current_role": "Marketing & Growth",
        "drift_days": 120,
        "active_apps": "Figma Pro, Salesforce Admin, Miro",
        "monthly_cost": 395.0,
        "admin_keys": 1,
        "annual_waste_usd": 2940.0,
        "access_status": "PENDING_REVIEW"
    },
    {
        "employee_id": "EMP-103",
        "name": "Marcus Vance",
        "email": "marcus.vance@company.com",
        "previous_role": "Infra On-Call",
        "current_role": "Customer Success",
        "drift_days": 60,
        "active_apps": "AWS DB Admin, PagerDuty, Zendesk",
        "monthly_cost": 1344.0,
        "admin_keys": 1,
        "annual_waste_usd": 14940.0,
        "access_status": "PENDING_REVIEW"
    },
    {
        "employee_id": "EMP-104",
        "name": "Elena Rostova",
        "email": "elena.rostova@company.com",
        "previous_role": "Mobile Engineering",
        "current_role": "Mobile Engineering",
        "drift_days": 0,
        "active_apps": "GitHub Dev, Apple Org, Figma Viewer",
        "monthly_cost": 36.0,
        "admin_keys": 0,
        "annual_waste_usd": 0.0,
        "access_status": "COMPLIANT"
    },
    {
        "employee_id": "EMP-105",
        "name": "Tariq Al-Mansoor",
        "email": "tariq.almansoor@company.com",
        "previous_role": "Cloud Contractor",
        "current_role": "Data Science",
        "drift_days": 90,
        "active_apps": "Snowflake Admin, AWS Admin, GitHub",
        "monthly_cost": 2071.0,
        "admin_keys": 3,
        "annual_waste_usd": 19920.0,
        "access_status": "PENDING_REVIEW"
    }
]

import os

DATABASE_URL = os.getenv("DATABASE_URL")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        identities = EMPLOYEES
        if DATABASE_URL and ("postgres" in DATABASE_URL or "neon" in DATABASE_URL or "railway" in DATABASE_URL):
            try:
                import psycopg2
                from psycopg2.extras import RealDictCursor
                conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
                cur = conn.cursor()
                cur.execute("SELECT * FROM enterprise_identities ORDER BY employee_id")
                rows = cur.fetchall()
                conn.close()
                if rows:
                    identities = [dict(r) for r in rows]
            except Exception as e:
                pass

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(identities).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
