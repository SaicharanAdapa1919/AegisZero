"""
AegisZero: Enterprise Identity & SaaS Simulation Engine
Simulates enterprise employee records, role transitions, SaaS licenses, and behavioral activity.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any
import time

@dataclass
class License:
    app_name: str
    tier: str  # e.g., 'Enterprise Admin', 'Pro Editor', 'Standard', 'Viewer'
    monthly_cost_usd: float
    last_login_days_ago: int
    last_productive_action_days_ago: int  # PR created, commit, API write, Figma edit
    has_admin_privileges: bool = False
    is_downgradable: bool = True
    target_downgrade_tier: str = "Free Viewer"
    target_downgrade_cost: float = 0.0

@dataclass
class Employee:
    id: str
    name: str
    department: str
    current_role: str
    previous_role: str
    role_changed_days_ago: int
    licenses: List[License] = field(default_factory=list)
    risk_level: str = "LOW"  # LOW, MEDIUM, CRITICAL_ZOMBIE
    status: str = "UNPROCESSED"  # UNPROCESSED, ANALYZED, AUTONOMOUSLY_OPTIMIZED

class EnterpriseDirectory:
    def __init__(self):
        self.reset()

    def reset(self):
        self.employees: List[Employee] = [
            Employee(
                id="EMP-101",
                name="David Chen",
                department="Internal Tooling",
                current_role="Staff Backend Engineer",
                previous_role="Payment Gateway Lead (Left project 75 days ago)",
                role_changed_days_ago=75,
                licenses=[
                    License("AWS IAM Production", "Root/AdminAccess", 1200.0, 3, 75, has_admin_privileges=True, target_downgrade_tier="JIT 1hr STS Token", target_downgrade_cost=0.0),
                    License("Figma Enterprise", "Pro Designer Editor", 75.0, 4, 110, has_admin_privileges=False, target_downgrade_tier="Free Viewer", target_downgrade_cost=0.0),
                    License("GitHub Enterprise", "Org Admin", 21.0, 1, 1, has_admin_privileges=True, target_downgrade_tier="Developer Seat", target_downgrade_cost=21.0),
                    License("Datadog APM", "Full Admin Seat", 180.0, 12, 85, has_admin_privileges=True, target_downgrade_tier="Read-Only User", target_downgrade_cost=0.0)
                ]
            ),
            Employee(
                id="EMP-102",
                name="Sarah Jenkins",
                department="Marketing & Growth",
                current_role="Content Strategist",
                previous_role="Product Designer (Switched 120 days ago)",
                role_changed_days_ago=120,
                licenses=[
                    License("Figma Enterprise", "Pro Designer Editor", 75.0, 2, 120, has_admin_privileges=False, target_downgrade_tier="Free Viewer", target_downgrade_cost=0.0),
                    License("Salesforce Enterprise", "System Admin", 300.0, 8, 90, has_admin_privileges=True, target_downgrade_tier="Standard User", target_downgrade_cost=150.0),
                    License("Miro Board", "Enterprise Creator", 20.0, 5, 14, has_admin_privileges=False, target_downgrade_tier="Free Viewer", target_downgrade_cost=0.0)
                ]
            ),
            Employee(
                id="EMP-103",
                name="Marcus Vance",
                department="Customer Success",
                current_role="Tier-1 Support Agent",
                previous_role="Infrastructure On-Call (Switched 60 days ago)",
                role_changed_days_ago=60,
                licenses=[
                    License("AWS IAM Production", "Database Admin", 1200.0, 14, 60, has_admin_privileges=True, target_downgrade_tier="Revoked", target_downgrade_cost=0.0),
                    License("PagerDuty", "High Urgency Responder", 45.0, 2, 60, has_admin_privileges=False, target_downgrade_tier="Stakeholder Viewer", target_downgrade_cost=0.0),
                    License("Zendesk", "Agent Seat", 99.0, 1, 1, has_admin_privileges=False, target_downgrade_tier="Agent Seat", target_downgrade_cost=99.0)
                ]
            ),
            Employee(
                id="EMP-104",
                name="Elena Rostova",
                department="Mobile Engineering",
                current_role="iOS Senior Developer",
                previous_role="iOS Senior Developer (Stable)",
                role_changed_days_ago=0,
                licenses=[
                    License("GitHub Enterprise", "Developer Seat", 21.0, 1, 1, has_admin_privileges=False, target_downgrade_tier="Developer Seat", target_downgrade_cost=21.0),
                    License("Figma Enterprise", "Free Viewer", 0.0, 1, 1, has_admin_privileges=False, target_downgrade_tier="Free Viewer", target_downgrade_cost=0.0),
                    License("Apple Developer Org", "Member", 15.0, 3, 2, has_admin_privileges=False, target_downgrade_tier="Member", target_downgrade_cost=15.0)
                ]
            ),
            Employee(
                id="EMP-105",
                name="Tariq Al-Mansoor",
                department="Data Science",
                current_role="ML Researcher",
                previous_role="Cloud Operations Contractor (Transitioned 90 days ago)",
                role_changed_days_ago=90,
                licenses=[
                    License("Snowflake", "Accountadmin Role", 850.0, 6, 90, has_admin_privileges=True, target_downgrade_tier="Data Analyst Role", target_downgrade_cost=150.0),
                    License("AWS IAM Production", "AdministratorAccess", 1200.0, 11, 90, has_admin_privileges=True, target_downgrade_tier="SageMaker Scoped Only", target_downgrade_cost=200.0),
                    License("GitHub Enterprise", "Org Owner", 21.0, 1, 5, has_admin_privileges=True, target_downgrade_tier="Developer Seat", target_downgrade_cost=21.0)
                ]
            ),
        ]

    def get_summary_metrics(self) -> Dict[str, Any]:
        total_monthly_spend = sum(
            sum(lic.monthly_cost_usd for lic in emp.licenses)
            for emp in self.employees
        )
        
        # Calculate potential waste
        potential_monthly_savings = 0.0
        zombie_accounts_count = 0
        toxic_admin_privileges = 0

        for emp in self.employees:
            for lic in emp.licenses:
                if lic.last_productive_action_days_ago > 30 and lic.is_downgradable:
                    potential_monthly_savings += (lic.monthly_cost_usd - lic.target_downgrade_cost)
                    zombie_accounts_count += 1
                if lic.has_admin_privileges and emp.role_changed_days_ago > 30:
                    toxic_admin_privileges += 1

        annual_savings = potential_monthly_savings * 12.0

        return {
            "total_employees": len(self.employees),
            "total_monthly_spend": round(total_monthly_spend, 2),
            "potential_monthly_savings": round(potential_monthly_savings, 2),
            "potential_annual_savings": round(annual_savings, 2),
            "zombie_licenses_count": zombie_accounts_count,
            "toxic_admin_privileges_count": toxic_admin_privileges,
            "compliance_risk_score": 87 if toxic_admin_privileges > 0 else 12  # out of 100
        }
