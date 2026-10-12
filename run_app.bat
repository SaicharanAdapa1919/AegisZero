@echo off
echo ============================================================
echo Starting AegisZero Autonomous Swarm (Backend + Frontend)...
echo ============================================================
cd /d %~dp0\backend
start http://localhost:8000
"C:\Users\DELL\AppData\Local\Python\bin\python.exe" server.py
pause