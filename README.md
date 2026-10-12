# AegisZero: Enterprise Autonomous Zero-Trust Identity & SaaS FinOps Engine

An autonomous multi-agent mesh that mathematically eliminates toxic standing admin privileges and reclaims zombie cloud SaaS spend when employees switch squads.

---

## 🏗️ Production Architecture & Directory Layout

```
AegisZero-Enterprise/
│
├── frontend/                   # Production Vercel App (HTML5 + TailwindCSS + JS)
│   ├── index.html              # Cockpit Dashboard (KPI gauges, 8-agent tabs)
│   ├── package.json            # Node / Vercel deployment spec
│   ├── vercel.json             # Serverless routing rules
│   └── api/                    # Vercel Python Serverless Backend Functions
│       ├── health.py           # GET  /api/health
│       ├── employees.py        # GET  /api/employees
│       └── run-swarm.py        # POST /api/run-swarm (Autonomous Remediation)
│
├── backend/                    # Local FastAPI Server & Autonomous 8-Agent Swarm
│   ├── server.py               # REST API server (FastAPI + Uvicorn)
│   ├── identity_agents.py      # The 8 autonomous AI agents & master orchestrator
│   ├── identity_engine.py      # Data classes (Employee, License, Directory)
│   ├── view_database.py       # Terminal CLI database inspection tool
│   └── requirements.txt        # Backend Python dependencies
│
├── database/                   # Embedded & Cloud Database Assets
│   ├── aegiszero_enterprise.db # Local SQLite Relational Database
│   └── enterprise_identities.csv # Aligned enterprise schema for DB imports
│
├── docs/                       # Presentation & Hackathon Keynote Assets
│   ├── Workato_Hack_AegisZero_10_Slides.pptx # 10-slide keynote presentation deck
│   ├── AegisZero_Complete_Project_Dossier.pdf # Master technical blueprint & 12-min script
│   ├── DEMO_VOICEOVER_SCRIPT.md # Verbatim timed presentation voiceover script
│   └── PRESENTATION_PITCH.md   # Pitch deck script
│
├── run_app.bat                 # 1-Click Local Launch Script
└── .gitignore                  # GitHub deployment exclusion rules
```

---

## 🚀 How to Run Locally in VSCode

1. Open **VSCode** and open the folder:
   ```text
   C:\Users\DELL\OneDrive\Desktop\AegisZero-Enterprise
   ```
2. Double-click **`run_app.bat`** (or in VSCode terminal run `cd backend && python server.py`).
3. Open your browser at **`http://localhost:8000`**.

---

## 🌐 How to Deploy to Vercel & Push to GitHub

### 1. Push to GitHub
In your VSCode terminal:
```bash
git init
git add .
git commit -m "feat: complete AegisZero enterprise architecture with serverless backend and database"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aegiszero-enterprise.git
git push -u origin main
```

### 2. Deploy to Vercel (Production Cloud)
You can deploy directly from your terminal using Vercel CLI:
```bash
cd frontend
npx vercel --prod
```
* **Root Directory on Vercel:** Select `frontend` (or `./frontend`).
* Vercel will automatically serve the UI and execute the serverless Python functions in `/api` with zero server configuration required!

---

## 🛡️ Database Management (Local SQLite)

To view or edit the database at any time from your VSCode terminal:
```bash
cd backend
python view_database.py view              # Inspect all employee records
python view_database.py audit             # View cryptographic audit ledger
python view_database.py set EMP-101 REVOKED 0 # Update an employee's access
python view_database.py reset             # Restore to baseline state
```
