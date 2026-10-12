"""
Generate the exhaustive AegisZero Web Application Complete Guide PDF.
Explains every single visual element, button, metric, table column, 
employee profile, and agent war-room tab on the website in detail.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

CUR_DIR = os.path.dirname(__file__)
PDF_OUT = os.path.join(CUR_DIR, "AegisZero_Web_Application_Complete_Guide.pdf")

doc = SimpleDocTemplate(
    PDF_OUT,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=21, leading=25,
    textColor=colors.HexColor('#0F172A'), spaceAfter=4
)
subtitle_style = ParagraphStyle(
    'DocSubTitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=11, leading=15,
    textColor=colors.HexColor('#0284C7'), spaceAfter=8
)
h1_style = ParagraphStyle(
    'SectionH1', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=13, leading=17,
    textColor=colors.HexColor('#0F172A'), spaceBefore=10, spaceAfter=4
)
h2_style = ParagraphStyle(
    'SectionH2', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=10.5, leading=14.5,
    textColor=colors.HexColor('#0369A1'), spaceBefore=6, spaceAfter=3
)
body_style = ParagraphStyle(
    'BodyCustom', parent=styles['Normal'],
    fontName='Helvetica', fontSize=8.5, leading=12.5,
    textColor=colors.HexColor('#334155'), spaceAfter=4
)
bullet_style = ParagraphStyle(
    'BulletCustom', parent=styles['Normal'],
    fontName='Helvetica', fontSize=8.5, leading=12.5,
    textColor=colors.HexColor('#334155'), leftIndent=12, firstLineIndent=-8, spaceAfter=2.5
)
callout_style = ParagraphStyle(
    'CalloutText', parent=styles['Normal'],
    fontName='Helvetica', fontSize=8.5, leading=12.5,
    textColor=colors.HexColor('#0F172A')
)
code_style = ParagraphStyle(
    'CodeText', parent=styles['Normal'],
    fontName='Courier', fontSize=8, leading=11,
    textColor=colors.HexColor('#E2E8F0')
)

story = []

# ================= PAGE 1 =================
story.append(Paragraph("AegisZero Web Application: Comprehensive UI & System Guide", title_style))
story.append(Paragraph("Complete Screen-by-Screen, Button-by-Button & Component Walkthrough", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=8))

intro_box = (
    "<b>Purpose of this Guide:</b> This document provides an exhaustive, line-by-line explanation of every visual element, "
    "control button, KPI metric card, table entry, and multi-agent war-room tab featured in the AegisZero web application "
    "(<font face='Courier'>identity_app.py</font>). Use this as your master reference manual when explaining or demonstrating the live website to judges."
)
story.append(Table([[Paragraph(intro_box, callout_style)]], colWidths=[540], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BAE6FD')),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(Spacer(1, 6))

# SECTION 1: SIDEBAR CONTROLS
story.append(Paragraph("1. The Left Sidebar Navigation & Control Panel", h1_style))
story.append(Paragraph(
    "The sidebar sits on the left of the screen and acts as the interactive mission control for the user or judge:",
    body_style
))

sidebar_data = [
    [Paragraph("<b>Sidebar Element</b>", h2_style), Paragraph("<b>Function & Underlying Behavior</b>", h2_style), Paragraph("<b>Visual Feedback on Screen</b>", h2_style)],
    [
        Paragraph("<b>App Branding & Icon</b>", body_style),
        Paragraph("Displays the shield insignia, app title ('AegisZero'), subtitle, and Track 1 metadata badge.", body_style),
        Paragraph("Establishes enterprise identity governance theme immediately.", body_style)
    ],
    [
        Paragraph("<b>🔄 Reset Directory</b>", body_style),
        Paragraph("Resets all 5 employees back to their original unanalyzed state, wipes the swarm cache, and resets optimization state to False.", body_style),
        Paragraph("Restores all metrics to the un-optimized baseline (18% SOC2, 4 toxic keys, $55,500 waste).", body_style)
    ],
    [
        Paragraph("<b>⚡ Run 7-Agent Swarm<br/>(Primary Action)</b>", body_style),
        Paragraph("The primary trigger. Ingests all employee profiles and passes them to the Master Orchestrator, which dispatches the 7 specialized agents in parallel and sequential order.", body_style),
        Paragraph("Shows an animated loading spinner ('7-Agent Swarm analyzing behavioral telemetry...'), followed by a green success banner and unlocks the War-Room.", body_style)
    ],
    [
        Paragraph("<b>✨ 1-Click Autonomous Execution</b>", body_style),
        Paragraph("Only appears <i>after</i> the Swarm has completed its analysis. Simulates zero-touch execution across cloud IAM and SCIM APIs with zero human tickets.", body_style),
        Paragraph("Fires celebratory digital balloons, turns toxic keys to 0, jumps SOC2 to 98%, and updates table status to '🟢 OPTIMIZED'.", body_style)
    ],
]
t_sb = Table(sidebar_data, colWidths=[120, 240, 180], style=[
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
])
story.append(t_sb)
story.append(Spacer(1, 6))

# SECTION 2: TOP EXECUTIVE KPI METRICS
story.append(Paragraph("2. The Top Executive KPI Metric Bar (5 Real-Time Cards)", h1_style))
story.append(Paragraph(
    "Positioned at the top of the main dashboard, these 5 KPI metric cards give enterprise executives and judges an instantaneous summary of the health, financial waste, and security posture of the company:",
    body_style
))

kpi_data = [
    [Paragraph("<b>Metric Card</b>", h2_style), Paragraph("<b>Pre-Optimization State</b>", h2_style), Paragraph("<b>Post-Optimization State</b>", h2_style), Paragraph("<b>What It Proves to the Judges</b>", h2_style)],
    [
        Paragraph("<b>1. Monitored Users</b>", body_style),
        Paragraph("<b>5 Staff</b><br/>(Active Directory)", body_style),
        Paragraph("<b>5 Staff</b><br/>(Active Directory)", body_style),
        Paragraph("Confirms the sample directory size monitored across all departments.", body_style)
    ],
    [
        Paragraph("<b>2. Total SaaS Spend</b>", body_style),
        Paragraph("<b>$7,186 / month</b><br/>(Baseline spend)", body_style),
        Paragraph("<b>$7,186 / month</b><br/>(Baseline spend)", body_style),
        Paragraph("Shows the current gross software subscription run-rate of the enterprise.", body_style)
    ],
    [
        Paragraph("<b>3. Annual Waste</b>", body_style),
        Paragraph("<b>$55,500.00</b><br/><font color='#DC2626'>-$4,625/mo bleed</font>", body_style),
        Paragraph("<b>$55,500.00</b><br/><font color='#16A34A'>Reclaimed! (100% ROI)</font>", body_style),
        Paragraph("Direct monetary proof of FinOps cash recovery. Turns bleeding loss into reclaimed profit.", body_style)
    ],
    [
        Paragraph("<b>4. Toxic Admin Keys</b>", body_style),
        Paragraph("<b>4 Keys</b><br/><font color='#DC2626'>Critical Risk</font>", body_style),
        Paragraph("<b>0 Keys</b><br/><font color='#16A34A'>All Neutralized</font>", body_style),
        Paragraph("Proves permanent high-privilege keys (AWS Root, Snowflake Admin) were revoked without incident.", body_style)
    ],
    [
        Paragraph("<b>5. SOC2 Compliance</b>", body_style),
        Paragraph("<b>18% (Critical Fail)</b><br/><font color='#DC2626'>Violations Active</font>", body_style),
        Paragraph("<b>98% (Audit Ready)</b><br/><font color='#16A34A'>+80% jump</font>", body_style),
        Paragraph("Demonstrates immediate corporate audit readiness for SOC2 CC6.1 & ISO27001.", body_style)
    ],
]
t_kpi = Table(kpi_data, colWidths=[110, 120, 130, 180], style=[
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
])
story.append(t_kpi)

story.append(PageBreak())

# ================= PAGE 2 =================
# SECTION 3: EMPLOYEE REGISTRY TABLE
story.append(Paragraph("3. Enterprise Identity & Permission Risk Registry Table", h1_style))
story.append(Paragraph(
    "This central table renders the full active directory. It shows how different departments and employee roles "
    "harbor hidden risks and waste. Here is the breakdown of every column and sample employee:",
    body_style
))

col_breakdown = (
    "<b>Table Columns Explained:</b><br/>"
    "• <b>ID:</b> Unique employee enterprise badge identifier (e.g. EMP-101).<br/>"
    "• <b>Name:</b> Employee full name.<br/>"
    "• <b>Department:</b> Current organizational business unit.<br/>"
    "• <b>Current Role:</b> Current active job title.<br/>"
    "• <b>Role History:</b> Previous team assignment and the exact elapsed days since transition.<br/>"
    "• <b>Active Apps:</b> Number of enterprise SaaS and cloud platforms currently provisioned to this user.<br/>"
    "• <b>Monthly Spend:</b> Dollar sum of all active license subscriptions consumed by this user per month.<br/>"
    "• <b>Zombie Apps:</b> Number of apps where user had 0 productive actions (commits/edits) for >30 days.<br/>"
    "• <b>Admin Keys:</b> Count of permanent superuser/administrator credentials held by this employee.<br/>"
    "• <b>Status Badge:</b> Dynamic status indicating compliance: <font color='#DC2626'><b>🚨 CRITICAL ZOMBIE</b></font>, <font color='#D97706'><b>🟡 ZOMBIE DETECTED</b></font>, or <font color='#16A34A'><b>🟢 OPTIMIZED</b></font>."
)
story.append(Table([[Paragraph(col_breakdown, body_style)]], colWidths=[540], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(Spacer(1, 6))

story.append(Paragraph("The 5 Pre-Configured Enterprise Personas in the Website:", h2_style))
persona_data = [
    [Paragraph("<b>Employee Persona</b>", h2_style), Paragraph("<b>Department & Role Drift History</b>", h2_style), Paragraph("<b>Licenses Held & Zombie Risk</b>", h2_style), Paragraph("<b>Identified Annual Waste</b>", h2_style)],
    [
        Paragraph("<b>1. David Chen</b><br/>(EMP-101)", body_style),
        Paragraph("Internal Tooling.<br/><i>Former Payment Lead (left 75 days ago)</i>", body_style),
        Paragraph("AWS Root ($1200), Figma Pro ($75), GitHub Admin ($21), Datadog Admin ($180).<br/><b>3 Zombie Apps + 3 Admin Keys</b>", body_style),
        Paragraph("<b>$17,700 / year</b><br/>(Highest Risk Persona)", body_style)
    ],
    [
        Paragraph("<b>2. Sarah Jenkins</b><br/>(EMP-102)", body_style),
        Paragraph("Marketing & Growth.<br/><i>Former Designer (switched 120 days ago)</i>", body_style),
        Paragraph("Figma Pro ($75), Salesforce Admin ($300), Miro Creator ($20).<br/><b>2 Zombie Apps + 1 Admin Key</b>", body_style),
        Paragraph("<b>$2,940 / year</b>", body_style)
    ],
    [
        Paragraph("<b>3. Marcus Vance</b><br/>(EMP-103)", body_style),
        Paragraph("Customer Success.<br/><i>Former Infra On-Call (switched 60 days ago)</i>", body_style),
        Paragraph("AWS Database Admin ($1200), PagerDuty Responder ($45), Zendesk Agent ($99).<br/><b>2 Zombie Apps + 1 Admin Key</b>", body_style),
        Paragraph("<b>$14,940 / year</b>", body_style)
    ],
    [
        Paragraph("<b>4. Elena Rostova</b><br/>(EMP-104)", body_style),
        Paragraph("Mobile Engineering.<br/><i>Senior iOS Dev (Stable, 0 days drift)</i>", body_style),
        Paragraph("GitHub Dev ($21), Figma Viewer ($0), Apple Org ($15).<br/><b>0 Zombie Apps + 0 Admin Keys</b>", body_style),
        Paragraph("<b>$0.00 / year</b><br/>(Compliant Control Baseline)", body_style)
    ],
    [
        Paragraph("<b>5. Tariq Al-Mansoor</b><br/>(EMP-105)", body_style),
        Paragraph("Data Science.<br/><i>Former Cloud Contractor (transitioned 90d ago)</i>", body_style),
        Paragraph("Snowflake Accountadmin ($850), AWS Admin ($1200), GitHub Owner ($21).<br/><b>3 Zombie Apps + 3 Admin Keys</b>", body_style),
        Paragraph("<b>$19,920 / year</b>", body_style)
    ],
]
t_per = Table(persona_data, colWidths=[100, 150, 190, 100], style=[
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
])
story.append(t_per)

story.append(PageBreak())

# ================= PAGE 3 =================
# SECTION 4: THE MULTI-AGENT WAR ROOM
story.append(Paragraph("4. The Multi-Agent War-Room: Exhaustive Tab Walkthrough", h1_style))
story.append(Paragraph(
    "When a user runs the swarm, the lower half of the website opens into the <b>Multi-Agent Autonomous War-Room</b>. "
    "A dropdown lets you select any employee (e.g., David Chen) to inspect their deliberations across 8 specialized tab views:",
    body_style
))

tabs_detail = [
    [Paragraph("<b>War-Room Tab</b>", h2_style), Paragraph("<b>Visual Elements & Data Rendered</b>", h2_style), Paragraph("<b>Technical Significance for Judges</b>", h2_style)],
    [
        Paragraph("<b>Tab 1: 🚀 Master Orchestrator</b>", body_style),
        Paragraph("• Terminal event bus stream with chronological timestamps.<br/>• Shows continuous ingestion, parallel dispatch to Agents 1-7, and consensus scoring.", body_style),
        Paragraph("Proves the central controller is not a hardcoded script, but a stateful DAG orchestrator.", body_style)
    ],
    [
        Paragraph("<b>Tab 2: 👤 Agent 1: HR Context</b>", body_style),
        Paragraph("• Assessment banner: <i>'Role shifted 75 days ago from Payment Gateway Lead to Internal Tooling'</i>.<br/>• Raw JSON telemetry displaying tenure metrics.", body_style),
        Paragraph("Proves the system cross-references HR organizational hierarchy with digital permissions.", body_style)
    ],
    [
        Paragraph("<b>Tab 3: 🔬 Agent 2: Behavioral Audit</b>", body_style),
        Paragraph("• Success banner: <i>'Exposed 3 applications with active SSO logins but 0 productive contributions'</i>.<br/>• Table showing days since last login vs. days since last actual PR/Figma edit.", body_style),
        Paragraph("Demonstrates the first major breakthrough: exposing 'Passive Lurkers' whom Okta/Zylo miss.", body_style)
    ],
    [
        Paragraph("<b>Tab 4: 🛡️ Agent 3: Blast Radius</b>", body_style),
        Paragraph("• Safety card: <i>'Scanned 42 CI/CD pipelines and cron jobs to ensure zero production crashes'</i>.<br/>• Score: <b>0.0% Blast Radius (VERIFIED SAFE TO REVOKE)</b>.", body_style),
        Paragraph("Demonstrates the second major breakthrough: eliminating IT fear of breaking production.", body_style)
    ],
    [
        Paragraph("<b>Tab 5: 💰 Agent 4: FinOps Arbitrage</b>", body_style),
        Paragraph("• Annual savings metric: <b>$17,700.00 / yr</b>.<br/>• Graceful Micro-Tiering plan table: from Tier & Cost to Target Downgrade Tier & Cost (e.g. AWS Root to JIT STS, Figma Pro to Free Viewer).", body_style),
        Paragraph("Proves concrete, auditable financial ROI that CFOs and IT directors care about.", body_style)
    ],
    [
        Paragraph("<b>Tab 6: 🔐 Agent 5: Security & SOC2</b>", body_style),
        Paragraph("• Warning badge: <b>HIGH_AUDIT_FAIL</b>.<br/>• Exact breach citations: <b>SOC2 CC6.1 Principle of Least Privilege Violation</b> on AWS IAM.", body_style),
        Paragraph("Proves immediate compliance value by linking permissions to real cybersecurity standards.", body_style)
    ],
    [
        Paragraph("<b>Tab 7: ⚡ Agent 6: API Synthesizer</b>", body_style),
        Paragraph("• Synthesized AWS CLI commands: <font face='Courier'>aws iam detach-user-policy ... && aws iam create-role --role-name JIT-STS-1hr</font>.<br/>• SCIM PATCH API curl payloads for Figma and Datadog.", body_style),
        Paragraph("Proves the system writes real, executable cloud configurations rather than just generating text.", body_style)
    ],
    [
        Paragraph("<b>Tab 8: 💬 Agent 7: Slack Bot Comms</b>", body_style),
        Paragraph("• Beautifully styled Slack message card addressed to David Chen.<br/>• Friendly explanation of graceful downgrade.<br/>• <b>1-Click Self-Healing Restore Link:</b> <font face='Courier'>https://aegiszero.internal/restore?user=EMP-101...</font>", body_style),
        Paragraph("Demonstrates the third major breakthrough: zero employee friction and zero IT helpdesk tickets.", body_style)
    ],
]
t_tab = Table(tabs_detail, colWidths=[120, 240, 180], style=[
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 4.5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
])
story.append(t_tab)

story.append(PageBreak())

# ================= PAGE 4 =================
# SECTION 5: LIVE DEMONSTRATION SCRIPT
story.append(Paragraph("5. Step-by-Step Live Demonstration Guide (For Presentation)", h1_style))
story.append(Paragraph(
    "Follow this exact sequence of clicks during your live demo to deliver a seamless, high-impact presentation:",
    body_style
))

demo_steps = [
    [Paragraph("<b>Demo Step</b>", h2_style), Paragraph("<b>Action to Perform on Screen</b>", h2_style), Paragraph("<b>What to Say to the Judges</b>", h2_style)],
    [
        Paragraph("<b>Phase 1: Baseline View</b>", body_style),
        Paragraph("Open the web app at <font face='Courier'>http://localhost:8501</font>. Point to the top KPI cards and the employee table.", body_style),
        Paragraph("<i>'Judges, notice our baseline: 5 employees, $7,186/mo spend, but $55,500/year bleeding in waste with an 18% failing SOC2 compliance score.'</i>", body_style)
    ],
    [
        Paragraph("<b>Phase 2: Trigger Swarm</b>", body_style),
        Paragraph("Click the blue <b>'⚡ Run 7-Agent Swarm'</b> button in the left sidebar.", body_style),
        Paragraph("<i>'With one click, our Master Orchestrator dispatches our 7 specialized agents. Within 3 seconds, all 5 employees are audited across HR, Git, CI/CD, and CloudTrail.'</i>", body_style)
    ],
    [
        Paragraph("<b>Phase 3: Inspect Persona</b>", body_style),
        Paragraph("Select <b>'David Chen'</b> in the dropdown. Click through Tabs 2, 3, 4, 6, and 8.", body_style),
        Paragraph("<i>'Look at David: HR confirms he left Payments 75 days ago; Behavioral audit proves 0 edits; Blast radius confirms 0% outage risk; and here is the synthesized AWS CLI command and friendly Slack card.'</i>", body_style)
    ],
    [
        Paragraph("<b>Phase 4: Autonomous Execution</b>", body_style),
        Paragraph("Click the green <b>'✨ 1-Click Autonomous Execution'</b> button in the sidebar.", body_style),
        Paragraph("<i>'Now watch zero-touch remediation: digital balloons fire, toxic admin keys drop to 0, SOC2 jumps from 18% to 98%, and we recover $55,500/year with zero human tickets!'</i>", body_style)
    ],
]
t_demo = Table(demo_steps, colWidths=[110, 200, 230], style=[
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 5.5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
])
story.append(t_demo)
story.append(Spacer(1, 10))

# SECTION 6: SUMMARY OF ARCHITECTURE & LAUNCH COMMAND
story.append(Paragraph("6. Launch Command & Codebase Summary", h1_style))
story.append(Paragraph(
    "The complete web application is built in Python using Streamlit, supported by modular simulation and multi-agent backend engines:",
    body_style
))

code_box = (
    "<b>TERMINAL EXECUTION COMMAND:</b><br/>"
    "<font face='Courier'>cd C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\aegismesh<br/>"
    "streamlit run identity_app.py</font><br/><br/>"
    "<b>CODE ARCHITECTURE FILE MAP:</b><br/>"
    "• <font face='Courier'>identity_app.py</font>: Frontend web dashboard, KPI cards, table visualizer, tabbed war-room.<br/>"
    "• <font face='Courier'>identity_engine.py</font>: Enterprise data models, employee personas, SaaS license metrics, simulation state.<br/>"
    "• <font face='Courier'>identity_agents.py</font>: Master Zero-Trust Orchestrator + 7 specialized autonomous worker agents."
)
story.append(Table([[Paragraph(code_box, body_style)]], colWidths=[540], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
    ('PADDING', (0,0), (-1,-1), 8),
]))

doc.build(story)
print(f"COMPLETE WEBSITE GUIDE PDF GENERATED AT: {PDF_OUT}")
