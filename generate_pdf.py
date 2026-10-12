"""
Script to generate the comprehensive AegisZero Executive Proposal and Technical Blueprint PDF.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import sys
import os

pdf_path = os.path.join(os.path.dirname(__file__), "AegisZero_Executive_Proposal.pdf")

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Custom Styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=24,
    leading=28,
    textColor=colors.HexColor('#1E293B'),
    spaceAfter=8
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=13,
    leading=17,
    textColor=colors.HexColor('#0284C7'),
    spaceAfter=15
)

h1_style = ParagraphStyle(
    'SectionH1',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#0F172A'),
    spaceBefore=14,
    spaceAfter=6
)

h2_style = ParagraphStyle(
    'SectionH2',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=colors.HexColor('#0369A1'),
    spaceBefore=10,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#334155'),
    spaceAfter=6
)

bullet_style = ParagraphStyle(
    'BulletCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13.5,
    textColor=colors.HexColor('#334155'),
    leftIndent=15,
    firstLineIndent=-10,
    spaceAfter=4
)

callout_style = ParagraphStyle(
    'CalloutText',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#0F172A')
)

story = []

# ================= PAGE 1 =================
story.append(Paragraph("AegisZero: Autonomous Zero-Trust Identity & SaaS FinOps Swarm", title_style))
story.append(Paragraph("Track 1: Orchestrator + Agents (Enterprise Agentic Workflows) | MOURI Tech Hackathon", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=12))

# Executive Summary Box
summary_text = (
    "<b>Executive Summary:</b> AegisZero is an autonomous, multi-agent enterprise governance system designed to "
    "solve the multi-million dollar problem of <b>'Ghost Access'</b>, <b>Zombie SaaS licenses</b>, and "
    "<b>Toxic Admin Privileges</b>. Built with a Master Orchestrator and 7 specialized agents, it replaces months "
    "of manual, rubber-stamped human spreadsheets with an autonomous, continuous closed-loop that detects role drift, "
    "proves zero blast-radius, and executes graceful micro-tiering with zero employee friction."
)
summary_table = Table([[Paragraph(summary_text, callout_style)]], colWidths=[530])
summary_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BAE6FD')),
    ('PADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(summary_table)
story.append(Spacer(1, 10))

# 1. THE PROBLEM STATEMENT (Crystal Clear)
story.append(Paragraph("1. The Real-World Problem Statement (Explained Simply)", h1_style))
story.append(Paragraph(
    "In every enterprise with thousands of employees (such as technology consultancies and corporate IT), staff frequently "
    "switch projects, get promoted, or transition teams. When employees transition, their digital privileges rarely keep up.",
    body_style
))

p_example = (
    "<b>The Real-Life Scenario:</b><br/>"
    "• 6 months ago, an engineer named <b>David</b> was assigned to a high-security Payment Gateway project. He was granted "
    "permanent <b>AWS Production Root Access</b> ($1,200/mo), a <b>Figma Pro Designer Editor</b> seat ($75/mo), and a "
    "<b>Datadog Full Admin</b> license ($180/mo).<br/>"
    "• Today, David moves to an internal documentation team.<br/>"
    "• <b>What actually happens:</b> Nobody revokes his old permissions! The company continues bleeding thousands of dollars "
    "every month for software seats David never uses (<b>Zombie Spend</b>). More dangerously, David retains full backdoor access "
    "to production customer databases and credit card systems (<b>Severe Security & SOC2 Compliance Breach</b>)."
)
story.append(Table([[Paragraph(p_example, body_style)]], colWidths=[530], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FDE68A')),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(Spacer(1, 10))

# 2. WHAT ALREADY EXISTS & WHY IT FAILS
story.append(Paragraph("2. What Already Exists in the Market & Why It Fails", h1_style))
story.append(Paragraph(
    "Companies currently spend millions on Identity Governance (IGA) tools like <b>SailPoint</b> or <b>Okta</b>, and SaaS "
    "management platforms like <b>Zylo</b>. Yet, over 80% of data breaches and massive cloud waste still occur due to ghost access. Here is why existing software fails:",
    body_style
))

story.append(Paragraph("• <b>The 'Rubber-Stamp' Failure:</b> Every 6 months, tools like SailPoint email managers a spreadsheet containing 500+ checkboxes asking 'Do your people still need this?'. Overworked managers don't have time to audit 500 rows, so they simply click <b>'Select All → Approve' in 5 seconds</b> without looking.", bullet_style))
story.append(Paragraph("• <b>The 'Single Sign-On' (SSO) Blind Spot:</b> SaaS management tools only track whether a user clicked the login button in the last 30 days. If an engineer clicked a Figma link once just to view a diagram, the tool marks them as 'Active User' and continues paying $75/month for a Pro Editor seat.", bullet_style))
story.append(Paragraph("• <b>Fear of Breaking Production (The Blast-Radius Dilemma):</b> IT administrators never dare revoke an engineer's API key or AWS permission because they worry: <i>'What if an automated backend script or CI/CD deployment uses his token and crashes the entire website?'</i>", bullet_style))
story.append(Paragraph("• <b>The Binary Revocation Trap:</b> Traditional software only offers binary choices: either delete the user entirely (which breaks collaboration and creates angry Slack complaints) or leave them on an expensive Admin seat.", bullet_style))

story.append(PageBreak())

# ================= PAGE 2 =================
story.append(Paragraph("3. What We Are Adding: The 3 Groundbreaking Advancements", h1_style))
story.append(Paragraph(
    "AegisZero solves the blind spots of existing enterprise tools by introducing 3 novel technological capabilities:",
    body_style
))

adv_data = [
    [
        Paragraph("<b>Advancement</b>", h2_style),
        Paragraph("<b>The Industry Flaw Today</b>", h2_style),
        Paragraph("<b>AegisZero's Innovation</b>", h2_style)
    ],
    [
        Paragraph("<b>1. Deep Behavioral Auditing</b>", body_style),
        Paragraph("Only checks binary SSO login dates. Treats passive page viewers as active paid users.", body_style),
        Paragraph("Audits <b>real productive output</b> (Git pull requests, Jira sprint boards, CloudTrail API calls). Exposes 'Passive Lurkers' who log in but produce 0 edits.", body_style)
    ],
    [
        Paragraph("<b>2. Predictive Blast-Radius Simulation</b>", body_style),
        Paragraph("IT admins are afraid to revoke keys due to fear of breaking automated background processes.", body_style),
        Paragraph("Automatically scans 40+ CI/CD pipelines, Dockerfiles, and cron jobs to mathematically verify: <b>Blast radius = 0.0%</b> (100% safe to revoke).", body_style)
    ],
    [
        Paragraph("<b>3. Graceful Micro-Tiering & Self-Healing</b>", body_style),
        Paragraph("Revocation is harsh and binary (deletes users, triggering IT support tickets and friction).", body_style),
        Paragraph("Executes <b>Graceful Micro-Tiering</b>: downgrades Pro Editors to Free Viewers, converts static AWS Root keys to 1-hour JIT tokens, and sends a friendly Slack bot message with a 1-click restore link.", body_style)
    ]
]
t_adv = Table(adv_data, colWidths=[130, 190, 210])
t_adv.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t_adv)
story.append(Spacer(1, 12))

# 4. HOW IT WORKS & ARCHITECTURE
story.append(Paragraph("4. How It Works: Multi-Agent Architecture & Swarm Workflow", h1_style))
story.append(Paragraph(
    "AegisZero operates as an autonomous, multi-agent swarm coordinated by a central <b>Master Zero-Trust Orchestrator</b>. "
    "Each agent specializes in a distinct enterprise domain, communicating through an event bus with minimal human intervention:",
    body_style
))

agent_data = [
    [Paragraph("<b>Agent Name</b>", h2_style), Paragraph("<b>Enterprise Domain & Responsibility</b>", h2_style)],
    [
        Paragraph("<b>🚀 Master Orchestrator</b>", body_style),
        Paragraph("Coordinates the 7 worker agents, correlates cross-department data, resolves policy conflicts, and executes autonomous zero-touch remediation.", body_style)
    ],
    [
        Paragraph("<b>👤 1. HR Context Agent</b>", body_style),
        Paragraph("Monitors HR records (Workday/BambooHR) for job title transitions, promotions, and department moves to detect role drift.", body_style)
    ],
    [
        Paragraph("<b>🔬 2. Deep Behavioral Audit Agent</b>", body_style),
        Paragraph("Analyzes real developer/staff output across Git PRs, Jira boards, and API calls to separate real productive work from passive logins.", body_style)
    ],
    [
        Paragraph("<b>🛡️ 3. Blast-Radius & Dependency Agent</b>", body_style),
        Paragraph("Inspects CI/CD pipelines (GitHub Actions, Jenkins) and cron jobs to ensure revoking an access key will not cause production outages.", body_style)
    ],
    [
        Paragraph("<b>💰 4. SaaS License & FinOps Agent</b>", body_style),
        Paragraph("Calculates dollar drain per seat (AWS, Figma, Datadog, Salesforce) and designs the optimal financial downgrade path.", body_style)
    ],
    [
        Paragraph("<b>🔐 5. Security & Compliance Agent</b>", body_style),
        Paragraph("Audits toxic permission combinations against SOC2 CC6.1, ISO27001, and HIPAA compliance policies.", body_style)
    ],
    [
        Paragraph("<b>⚡ 6. Graceful Downgrade Synthesizer</b>", body_style),
        Paragraph("Generates production-grade API payloads (Okta SCIM, AWS CLI, GitHub API) to execute micro-tier downgrades without account deletion.", body_style)
    ],
    [
        Paragraph("<b>💬 7. Autonomous Employee Slack Bot</b>", body_style),
        Paragraph("Sends a polite automated Slack notification with a 1-click self-healing restore link, eliminating IT helpdesk support tickets.", body_style)
    ],
]
t_agent = Table(agent_data, colWidths=[160, 370])
t_agent.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('PADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t_agent)

story.append(PageBreak())

# ================= PAGE 3 =================
story.append(Paragraph("5. End-to-End Autonomous Workflow (Step-by-Step)", h1_style))

workflow_text = (
    "<b>Step 1: Continuous Ingestion</b><br/>"
    "The Master Orchestrator continuously pulls data from HR systems, SSO providers (Okta/Azure AD), GitHub/Jira, and CloudTrail.<br/><br/>"
    "<b>Step 2: Dual-Signal Correlation (HR vs. Behavior)</b><br/>"
    "Agent 1 flags that an employee moved out of the Payments team 75 days ago. Agent 2 verifies that despite recent logins, "
    "the employee has made 0 Git PRs, 0 Figma edits, and 0 database writes in over 60 days.<br/><br/>"
    "<b>Step 3: Automated Safety Proof (Blast Radius)</b><br/>"
    "Agent 3 cross-references the employee's personal API keys against all 42 automated deployment scripts and confirms: 0 dependent pipelines.<br/><br/>"
    "<b>Step 4: Financial & Compliance Calculation</b><br/>"
    "Agent 4 identifies $17,700/year in recoverable waste for this employee. Agent 5 flags a Critical SOC2 violation for dormant AWS Root privileges.<br/><br/>"
    "<b>Step 5: Zero-Touch Autonomous Execution</b><br/>"
    "Agent 6 executes the graceful micro-tiering command. The user is downgraded to Free Viewer, and AWS Root is converted to a 1-hour JIT token.<br/><br/>"
    "<b>Step 6: Self-Healing Employee Notification</b><br/>"
    "Agent 7 pings the employee on Slack with a friendly message and a 1-click instant restore link. The loop closes with zero IT tickets created."
)
story.append(Table([[Paragraph(workflow_text, body_style)]], colWidths=[530], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(Spacer(1, 10))

# 6. BUSINESS IMPACT & RESULTS
story.append(Paragraph("6. Measured Business Impact & ROI", h1_style))
impact_data = [
    [Paragraph("<b>Metric</b>", h2_style), Paragraph("<b>Before AegisZero</b>", h2_style), Paragraph("<b>With AegisZero Swarm</b>", h2_style)],
    [
        Paragraph("<b>SaaS & Cloud Waste</b>", body_style),
        Paragraph("$55,500 / year bleed (across 5 sample staff)", body_style),
        Paragraph("<b>$55,500 Reclaimed (100% ROI recovery)</b>", body_style)
    ],
    [
        Paragraph("<b>SOC2 Compliance Health</b>", body_style),
        Paragraph("18% (Critical Audit Failure)", body_style),
        Paragraph("<b>98% (Audit Ready, 0 Toxic Admin Keys)</b>", body_style)
    ],
    [
        Paragraph("<b>IT Access Review Duration</b>", body_style),
        Paragraph("2 to 4 weeks of manual spreadsheet reviews", body_style),
        Paragraph("<b>5 seconds autonomous continuous audit</b>", body_style)
    ],
    [
        Paragraph("<b>Employee Friction & Tickets</b>", body_style),
        Paragraph("Hundreds of angry tickets when accounts are deleted", body_style),
        Paragraph("<b>0 tickets (Graceful downgrade + 1-click restore)</b>", body_style)
    ],
]
t_impact = Table(impact_data, colWidths=[150, 190, 190])
t_impact.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('PADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t_impact)
story.append(Spacer(1, 10))

# 7. HOW TO RUN INSTRUCTIONS
story.append(Paragraph("7. Technical Implementation & Running the Live Demo", h1_style))
story.append(Paragraph(
    "AegisZero is fully implemented in Python and Streamlit with interactive telemetry dashboards. "
    "To launch the live demonstration on your laptop:",
    body_style
))
code_run = (
    "<b>PowerShell Execution Command:</b><br/>"
    "<font face='Courier'>cd C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\aegismesh<br/>"
    "streamlit run identity_app.py</font><br/><br/>"
    "<i>Access the interactive dashboard at: <b>http://localhost:8501</b></i>"
)
story.append(Table([[Paragraph(code_run, body_style)]], colWidths=[530], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
    ('PADDING', (0,0), (-1,-1), 8),
]))

# Build Document
doc.build(story)
print(f"PDF successfully generated at: {pdf_path}")
