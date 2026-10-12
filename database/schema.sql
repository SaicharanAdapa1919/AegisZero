-- AegisZero: Production Cloud Database Schema
-- Run this in your Cloud Database SQL Editor (Supabase / Neon / Railway / PostgreSQL)

-- 1. Create Enterprise Identities Table
CREATE TABLE IF NOT EXISTS enterprise_identities (
    employee_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    previous_role VARCHAR(150),
    "current_role" VARCHAR(150),
    drift_days INT DEFAULT 0,
    active_apps TEXT,
    monthly_cost NUMERIC(10, 2) DEFAULT 0.00,
    admin_keys INT DEFAULT 0,
    annual_waste_usd NUMERIC(10, 2) DEFAULT 0.00,
    access_status VARCHAR(50) DEFAULT 'PENDING_REVIEW',
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create Immutable Audit Ledger Table
CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    audit_id VARCHAR(100) UNIQUE NOT NULL,
    employee_id VARCHAR(50),
    action VARCHAR(100),
    annual_savings_usd NUMERIC(10, 2),
    sha256_hash VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Seed Initial Enterprise Records
INSERT INTO enterprise_identities (
    employee_id, name, email, previous_role, "current_role", drift_days, active_apps, monthly_cost, admin_keys, annual_waste_usd, access_status
) VALUES 
('EMP-101', 'David Chen', 'david@gmail.com', 'Payment Gateway', 'Internal Tooling', 75, 'AWS Root, Figma Pro, Datadog Admin, GitHub', 1476.00, 3, 17700.00, 'PENDING_REVIEW'),
('EMP-102', 'Sarah Jenkins', 'sarah.jenkins@company.com', 'UI/UX Design', 'Marketing & Growth', 120, 'Figma Pro, Salesforce Admin, Miro', 395.00, 1, 2940.00, 'PENDING_REVIEW'),
('EMP-103', 'Marcus Vance', 'marcus.vance@company.com', 'Infra On-Call', 'Customer Success', 60, 'AWS DB Admin, PagerDuty, Zendesk', 1344.00, 1, 14940.00, 'PENDING_REVIEW'),
('EMP-104', 'Elena Rostova', 'elena.rostova@company.com', 'Mobile Engineering', 'Mobile Engineering', 0, 'GitHub Dev, Apple Org, Figma Viewer', 36.00, 0, 0.00, 'COMPLIANT'),
('EMP-105', 'Tariq Al-Mansoor', 'tariq.almansoor@company.com', 'Cloud Contractor', 'Data Science', 90, 'Snowflake Admin, AWS Admin, GitHub', 2071.00, 3, 19920.00, 'PENDING_REVIEW')
ON CONFLICT (employee_id) DO NOTHING;
