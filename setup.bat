@echo off
setlocal enabledelayedexpansion

:: SpEquip E-Commerce Platform Setup Script for Windows
:: This script sets up the complete development environment

echo.
echo ====================================================
echo    SpEquip E-Commerce Platform - Setup Script
echo ====================================================
echo.

:: Check if Python is installed
echo [1/8] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Python %PYTHON_VERSION% found ✓

:: Check if pip is available
echo.
echo [2/8] Checking pip installation...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not available
    echo Please reinstall Python with pip included
    pause
    exit /b 1
)
echo pip is available ✓

:: Create virtual environment
echo.
echo [3/8] Creating virtual environment...
if exist "venv" (
    echo Virtual environment already exists, removing old one...
    rmdir /s /q venv
)

python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo Virtual environment created ✓

:: Activate virtual environment
echo.
echo [4/8] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo Virtual environment activated ✓

:: Upgrade pip to latest version
echo.
echo [5/8] Upgrading pip to latest version...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo WARNING: Failed to upgrade pip, continuing with current version
)

:: Install dependencies
echo.
echo [6/8] Installing Python dependencies...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    echo This might be due to network issues or missing requirements.txt
    pause
    exit /b 1
)
echo Dependencies installed ✓

:: Setup database and directories
echo.
echo [7/8] Setting up database and directories...
python setup.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to setup database
    pause
    exit /b 1
)
echo Database setup completed ✓

:: Seed database with sample data
echo.
echo [8/8] Seeding database with sample data...
python seed_database.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to seed database
    pause
    exit /b 1
)
echo Database seeding completed ✓

:: Create startup script
echo.
echo Creating startup script...
(
echo @echo off
echo cd /d "%CD%"
echo call venv\Scripts\activate.bat
echo echo.
echo echo ====================================================
echo echo    SpEquip E-Commerce Platform - Starting Server
echo echo ====================================================
echo echo.
echo echo Server will start at: http://localhost:5000
echo echo.
echo echo Demo Credentials:
echo echo Admin: admin@spequip.com / admin123
echo echo User:  user@spequip.com / user123
echo echo.
echo echo Press Ctrl+C to stop the server
echo echo.
echo python run.py
echo pause
) > start_spequip.bat

echo.
echo ====================================================
echo              SETUP COMPLETED SUCCESSFULLY!
echo ====================================================
echo.
echo What's been set up:
echo ✓ Python virtual environment
echo ✓ All required dependencies
echo ✓ Database with sample data
echo ✓ Application structure
echo ✓ Startup script
echo.
echo Demo Credentials:
echo Admin: admin@spequip.com / admin123
echo User:  user@spequip.com / user123
echo.
echo To start the application:
echo 1. Double-click 'start_spequip.bat' OR
echo 2. Run: python run.py
echo.
echo The application will be available at: http://localhost:5000
echo.
echo For troubleshooting, check the README.md file
echo.
echo Would you like to start the application now? (Y/N)
set /p choice=
if /i "%choice%"=="Y" (
    echo.
    echo Starting SpEquip E-Commerce Platform...
    python run.py
) else (
    echo.
    echo Setup complete! You can start the application anytime using start_spequip.bat
)

pause
