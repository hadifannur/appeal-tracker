@echo off
cd /d "%~dp0"

echo === Appeal Tracker Setup ===
echo.

REM Check Python is installed
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3 from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo Virtual environment created.
) else (
    echo Virtual environment already exists, skipping creation.
)

REM Activate and install dependencies
echo Installing dependencies...
call .venv\Scripts\activate.bat
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)

REM Check .env file exists
if not exist ".env" (
    echo.
    echo WARNING: .env file not found.
    echo Please create a .env file with the required credentials before running the app.
    echo See the project README or ask your team lead for the credentials.
)

echo.
echo === Setup complete! Run run.bat to start the app. ===
pause
