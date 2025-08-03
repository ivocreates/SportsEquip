@echo off
REM SpEquip E-Commerce Platform Setup Script for Windows
REM This script sets up the entire application automatically

echo ====================================
echo SpEquip E-Commerce Platform Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo [1/6] Checking Python installation...
python --version

REM Create virtual environment
echo.
echo [2/6] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Removing old one...
    rmdir /s /q venv
)
python -m venv venv

REM Activate virtual environment
echo.
echo [3/6] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo [4/6] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

REM Run setup script
echo.
echo [5/6] Setting up database and directories...
python setup.py

REM Seed database
echo.
echo [6/6] Seeding database with sample data...
python seed_database.py

echo.
echo ====================================
echo Setup completed successfully!
echo ====================================
echo.
echo To start the application:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Run the application: python run.py
echo 3. Open your browser to: http://localhost:5000
echo.
echo Demo Credentials:
echo Admin: admin@spequip.com / admin123
echo User:  user@spequip.com / user123
echo.
echo Press any key to start the application now...
pause >nul

REM Start the application
echo Starting SpEquip application...
python run.py
