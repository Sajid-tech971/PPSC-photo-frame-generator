@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  start "Pabna Frame Server" cmd /k "cd /d %~dp0 && py server.py"
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    start "Pabna Frame Server" cmd /k "cd /d %~dp0 && python server.py"
  ) else (
    echo Python 3 was not found. Please install Python 3.
    pause
    exit /b 1
  )
)
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8000
