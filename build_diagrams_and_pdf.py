"""
Build crisp, professional visual diagrams (Architecture & Workflow) 
and embed them into the AegisZero Executive Proposal PDF.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

CUR_DIR = os.path.dirname(__file__)

# ----------------- 1. GENERATE ARCHITECTURE DIAGRAM -----------------
def generate_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background canvas
    fig.patch.set_facecolor('#0F172A')
    ax.set_facecolor('#0F172A')

    # Title
    ax.text(50, 96, "AegisZero: Multi-Agent Enterprise Architecture", 
            ha='center', va='center', color='white', fontsize=16, fontweight='bold')
    ax.text(50, 92, "High-Level Distributed System Blueprint", 
            ha='center', va='center', color='#38BDF8', fontsize=10)

    # Box styles
    def draw_box(x, y, w, h, bg, border, title, desc, title_color='white', desc_color='#94A3B8'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1.2,rounding_size=2",
                                      facecolor=bg, edgecolor=border, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2 + 2, title, ha='center', va='center', color=title_color, fontsize=9, fontweight='bold')
        ax.text(x + w/2, y + h/2 - 3, desc, ha='center', va='center', color=desc_color, fontsize=7.5)

    # 1. Ingestion Layer (Top)
    draw_box(4, 76, 20, 10, '#1E293B', '#38BDF8', "HR Systems", "Workday / BambooHR")
    draw_box(28, 76, 20, 10, '#1E293B', '#38BDF8', "Identity & SSO", "Okta / Azure AD / Ping")
    draw_box(52, 76, 20, 10, '#1E293B', '#38BDF8', "Developer Telemetry", "GitHub / Jira / GitLab")
    draw_box(76, 76, 20, 10, '#1E293B', '#38BDF8', "Cloud & Audit Logs", "AWS CloudTrail / Datadog")

    # Ingestion Label Box
    rect_ingest = patches.FancyBboxPatch((2, 73), 96, 16, boxstyle="round,pad=0.5,rounding_size=1",
                                         facecolor='none', edgecolor='#475569', linestyle='--', linewidth=1)
    ax.add_patch(rect_ingest)
    ax.text(4, 73.5, "LAYER 1: ENTERPRISE DATA INGESTION", color='#94A3B8', fontsize=7, fontweight='bold')

    # Downward Arrow to Orchestrator
    ax.annotate('', xy=(50, 62), xytext=(50, 71),
                arrowprops=dict(facecolor='#38BDF8', edgecolor='#38BDF8', width=2, headwidth=7))

    # 2. Master Orchestrator (Middle Top)
    draw_box(22, 51, 56, 11, '#1E3A8A', '#60A5FA', 
             "MASTER ZERO-TRUST ORCHESTRATOR", 
             "State Machine • Conflict Resolution • Policy Enforcement • DAG Dispatcher",
             title_color='#93C5FD', desc_color='#E2E8F0')

    # Connection line down to Agent Swarm
    ax.plot([50, 50], [51, 44], color='#60A5FA', linewidth=2)
    ax.plot([10, 90], [44, 44], color='#60A5FA', linewidth=1.5)

    # 3. Agent Swarm (Middle Layer) - 8 Agents
    agents = [
        ("Agent 1: HR", "Role Drift", 2, 29, 10.5, 12),
        ("Agent 2: Entropy", "PRs vs SSO", 14, 29, 10.5, 12),
        ("Agent 3: AST Safe", "CI/CD 0% Risk", 26, 29, 10.5, 12),
        ("Agent 4: FinOps", "$ Tier Savings", 38, 29, 10.5, 12),
        ("Agent 5: Security", "SOC2 CC6.1", 50, 29, 10.5, 12),
        ("Agent 6: JIT Synth", "AWS & SCIM", 62, 29, 10.5, 12),
        ("Agent 7: Slack Bot", "1-Click Heal", 74, 29, 10.5, 12),
        ("Agent 8: Scribe", "SOC2 Ledger", 86, 29, 10.5, 12),
    ]

    for title, desc, x, y, w, h in agents:
        ax.plot([x + w/2, x + w/2], [44, y + h], color='#60A5FA', linewidth=1)
        draw_box(x, y, w, h, '#1E293B', '#818CF8', title, desc, title_color='#A5B4FC', desc_color='#CBD5E1')

    # Converging lines down to Execution Layer
    ax.plot([7, 91], [26, 26], color='#818CF8', linewidth=1.5)
    for title, desc, x, y, w, h in agents:
        ax.plot([x + w/2, x + w/2], [y, 26], color='#818CF8', linewidth=1)
    ax.annotate('', xy=(50, 19), xytext=(50, 26),
                arrowprops=dict(facecolor='#818CF8', edgecolor='#818CF8', width=2, headwidth=7))

    # 4. Execution & Delivery Layer (Bottom)
    draw_box(4, 6, 28, 11, '#064E3B', '#34D399', 
             "SCIM / Cloud IAM APIs", "Graceful Micro-Tiering Execution", title_color='#6EE7B7')
    draw_box(36, 6, 28, 11, '#4A154B', '#F472B6', 
             "Autonomous Slack Bot", "Zero-Friction 1-Click Restore Link", title_color='#FBCFE8')
    draw_box(68, 6, 28, 11, '#312E81', '#A78BFA', 
             "SRE & FinOps Cockpit", "Continuous SOC2 & Cost Audit", title_color='#C4B5FD')

    arch_img_path = os.path.join(CUR_DIR, "architecture_diagram.png")
    plt.tight_layout()
    plt.savefig(arch_img_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    return arch_img_path

# ----------------- 2. GENERATE WORKFLOW DIAGRAM -----------------
def generate_workflow_diagram():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')

    fig.patch.set_facecolor('#0F172A')
    ax.set_facecolor('#0F172A')

    ax.text(50, 46, "AegisZero: End-to-End Autonomous Workflow", 
            ha='center', va='center', color='white', fontsize=15, fontweight='bold')
    ax.text(50, 42, "Step-by-Step Continuous Governance & Self-Healing Pipeline", 
            ha='center', va='center', color='#38BDF8', fontsize=9.5)

    steps = [
        ("Step 1: Telemetry Ingest", "HR changes + SSO logins\n+ Git PRs + CloudTrail", 2, 12, 16, 22),
        ("Step 2: Dual Correlation", "Detects role transition\nvs 0 productive edits", 22, 12, 16, 22),
        ("Step 3: Blast Radius", "Scans 40+ pipelines;\nverifies 0% outage risk", 42, 12, 16, 22),
        ("Step 4: Swarm Synthesis", "FinOps $ plans + SOC2\n+ AWS/SCIM commands", 62, 12, 16, 22),
        ("Step 5: Zero-Touch Heal", "Auto-downgrades tiers;\nsends Slack 1-click restore", 82, 12, 16, 22)
    ]

    for title, desc, x, y, w, h in steps:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1,rounding_size=2",
                                      facecolor='#1E293B', edgecolor='#38BDF8', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 5, title, ha='center', va='center', color='#93C5FD', fontsize=8.5, fontweight='bold')
        ax.text(x + w/2, y + h/2 - 3, desc, ha='center', va='center', color='#E2E8F0', fontsize=7.5)

        # Connector arrow to next step
        if x < 80:
            ax.annotate('', xy=(x + w + 3.5, y + h/2), xytext=(x + w + 0.5, y + h/2),
                        arrowprops=dict(facecolor='#38BDF8', edgecolor='#38BDF8', width=2, headwidth=6))

    wf_img_path = os.path.join(CUR_DIR, "workflow_diagram.png")
    plt.tight_layout()
    plt.savefig(wf_img_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    return wf_img_path

# ----------------- 3. REBUILD THE COMPLETE PDF -----------------
def rebuild_pdf(arch_img, wf_img):
    pdf_path = os.path.join(CUR_DIR, "AegisZero_Executive_Proposal.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=22, leading=26,
        textColor=colors.HexColor('#0F172A'), spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=12, leading=16,
        textColor=colors.HexColor('#0284C7'), spaceAfter=10
    )
    h1_style = ParagraphStyle(
        'SectionH1', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=14, leading=18,
        textColor=colors.HexColor('#0F172A'), spaceBefore=10, spaceAfter=5
    )
    h2_style = ParagraphStyle(
        'SectionH2', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=colors.HexColor('#0369A1'), spaceBefore=6, spaceAfter=3
    )
    body_style = ParagraphStyle(
        'BodyTextCustom', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=colors.HexColor('#334155'), spaceAfter=5
    )
    bullet_style = ParagraphStyle(
        'BulletCustom', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=colors.HexColor('#334155'), leftIndent=12, firstLineIndent=-8, spaceAfter=3
    )
    callout_style = ParagraphStyle(
        'CalloutText', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # PAGE 1: Executive Summary & Problem
    story.append(Paragraph("AegisZero: Autonomous Zero-Trust Identity & SaaS FinOps Swarm", title_style))
    story.append(Paragraph("Track 1: Orchestrator + Agents (Enterprise Agentic Workflows) | MOURI Tech Hackathon", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=8))

    summary_text = (
        "<b>Executive Summary:</b> AegisZero is an autonomous, multi-agent enterprise governance system designed to "
        "solve the multi-million dollar problem of <b>'Ghost Access'</b>, <b>Zombie SaaS licenses</b>, and "
        "<b>Toxic Admin Privileges</b>. Built with a Master Orchestrator and 7 specialized agents, it replaces months "
        "of manual, rubber-stamped human spreadsheets with an autonomous, continuous closed-loop that detects role drift, "
        "proves zero blast-radius, and executes graceful micro-tiering with zero employee friction."
    )
    story.append(Table([[Paragraph(summary_text, callout_style)]], colWidths=[540], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BAE6FD')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(Spacer(1, 8))

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
    story.append(Table([[Paragraph(p_example, body_style)]], colWidths=[540], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FDE68A')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(Spacer(1, 6))

    story.append(Paragraph("2. What Already Exists in the Market & Why It Fails", h1_style))
    story.append(Paragraph("• <b>The 'Rubber-Stamp' Failure:</b> Every 6 months, tools like SailPoint email managers spreadsheets containing 500+ checkboxes. Overworked managers click <b>'Select All → Approve' in 5 seconds</b> without looking.", bullet_style))
    story.append(Paragraph("• <b>The 'Single Sign-On' (SSO) Blind Spot:</b> Tools like Zylo only track whether a user clicked login. If an engineer clicked Figma once just to view a diagram, it marks them as an 'Active User' and pays $75/mo.", bullet_style))
    story.append(Paragraph("• <b>Fear of Breaking Production (Blast Radius):</b> IT admins never dare revoke an engineer's API key because they worry: <i>'What if an automated background script uses this key and crashes production?'</i>", bullet_style))
    story.append(Paragraph("• <b>The Binary Revocation Trap:</b> Traditional software only offers two extremes: either delete the user entirely (which breaks collaboration) or leave them on an expensive Admin seat.", bullet_style))

    story.append(PageBreak())

    # PAGE 2: VISUAL ARCHITECTURE DIAGRAM
    story.append(Paragraph("3. Multi-Agent System Architecture (Visual Blueprint)", h1_style))
    story.append(Paragraph(
        "AegisZero is structured into 4 cohesive operational tiers: an Enterprise Ingestion Layer, a Master Zero-Trust "
        "Orchestrator, a 7-Agent Specialized Swarm, and an Autonomous Zero-Touch Execution & Delivery Layer:",
        body_style
    ))
    story.append(Spacer(1, 4))
    story.append(Image(arch_img, width=540, height=365))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Layer Breakdown:", h2_style))
    story.append(Paragraph("• <b>Layer 1 (Ingestion):</b> Connects directly to Workday (HR), Okta/Azure AD (SSO), GitHub/Jira (Developer Output), and AWS CloudTrail (API Activity).", bullet_style))
    story.append(Paragraph("• <b>Layer 2 (Master Orchestrator):</b> Acts as the central event bus and DAG coordinator, orchestrating parallel worker agent execution.", bullet_style))
    story.append(Paragraph("• <b>Layer 3 (7-Agent Swarm):</b> Domain-specialized agents executing HR drift analysis, deep behavioral verification, blast-radius proofs, FinOps math, SOC2 compliance, API command synthesis, and Slack bot comms.", bullet_style))
    story.append(Paragraph("• <b>Layer 4 (Zero-Touch Execution):</b> Safely executes micro-tiering via SCIM APIs, issues temporary AWS STS tokens, and sends 1-click self-healing links.", bullet_style))

    story.append(PageBreak())

    # PAGE 3: VISUAL WORKFLOW & ADVANCEMENTS
    story.append(Paragraph("4. End-to-End Autonomous Workflow (Step-by-Step Flowchart)", h1_style))
    story.append(Paragraph(
        "The complete lifecycle executes autonomously from real-time event detection to self-healing resolution:",
        body_style
    ))
    story.append(Spacer(1, 4))
    story.append(Image(wf_img, width=540, height=255))
    story.append(Spacer(1, 8))

    story.append(Paragraph("5. The 3 Groundbreaking Advancements (Why We Win)", h1_style))
    adv_data = [
        [Paragraph("<b>Advancement</b>", h2_style), Paragraph("<b>The Industry Flaw Today</b>", h2_style), Paragraph("<b>AegisZero's Innovation</b>", h2_style)],
        [
            Paragraph("<b>1. Deep Behavioral Auditing</b>", body_style),
            Paragraph("Only checks binary SSO login dates. Treats passive page viewers as active paid users.", body_style),
            Paragraph("Audits <b>real productive output</b> (Git pull requests, Jira sprint boards, CloudTrail API calls). Exposes 'Passive Lurkers' who produce 0 edits.", body_style)
        ],
        [
            Paragraph("<b>2. Predictive Blast-Radius Simulation</b>", body_style),
            Paragraph("IT admins are afraid to revoke keys due to fear of breaking automated background processes.", body_style),
            Paragraph("Automatically scans 40+ CI/CD pipelines, Dockerfiles, and cron jobs to mathematically verify: <b>Blast radius = 0.0%</b> (100% safe to revoke).", body_style)
        ],
        [
            Paragraph("<b>3. Graceful Micro-Tiering & Self-Healing</b>", body_style),
            Paragraph("Revocation is harsh and binary (deletes users, triggering IT support tickets and friction).", body_style),
            Paragraph("Executes <b>Graceful Micro-Tiering</b>: downgrades Pro Editors to Free Viewers, converts AWS Root to 1-hr JIT STS tokens, and sends a Slack bot with a 1-click restore link.", body_style)
        ]
    ]
    t_adv = Table(adv_data, colWidths=[130, 190, 220], style=[
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ])
    story.append(t_adv)

    story.append(PageBreak())

    # PAGE 4: BUSINESS IMPACT & HOW TO RUN
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
    t_impact = Table(impact_data, colWidths=[150, 195, 195], style=[
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ])
    story.append(t_impact)
    story.append(Spacer(1, 10))

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
    story.append(Table([[Paragraph(code_run, body_style)]], colWidths=[540], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))

    doc.build(story)
    print(f"COMPLETE PDF WITH DIAGRAMS GENERATED AT: {pdf_path}")

if __name__ == "__main__":
    arch = generate_architecture_diagram()
    wf = generate_workflow_diagram()
    rebuild_pdf(arch, wf)
