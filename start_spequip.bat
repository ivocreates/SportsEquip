@echo off
setlocal enabledelayedexpansion

:: SpEquip E-Commerce Platform Startup Script
:: This script starts the application server

cd /d "%~dp0"

echo.
echo ====================================================
echo    SpEquip E-Commerce Platform - Starting Server
echo ====================================================
echo.

:: Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first to set up the application.
    echo.
    pause
    exit /b 1
)

:: Check if database exists
if not exist "instance\spequip.db" (
    echo WARNING: Database not found!
    echo Setting up database and sample data...
    echo.
    
    :: Activate virtual environment
    call venv\Scripts\activate.bat
    
    :: Setup database
    python setup.py
    if %errorlevel% neq 0 (
        echo ERROR: Failed to setup database
        pause
        exit /b 1
    )
    
    :: Seed database
    python seed_database.py
    if %errorlevel% neq 0 (
        echo ERROR: Failed to seed database
        pause
        exit /b 1
    )
    
    echo Database setup completed ✓
    echo.
) else (
    :: Just activate virtual environment
    call venv\Scripts\activate.bat
)

:: Check if Flask app can be imported
echo Checking application integrity...
python -c "from app import create_app; app = create_app(); print('Application ready ✓')" 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Application cannot start properly
    echo This might be due to missing dependencies or corrupted installation
    echo Please run setup.bat to reinstall the application
    echo.
    pause
    exit /b 1
)

:: Get local IP for network access
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    for /f "tokens=1" %%b in ("%%a") do (
        set LOCAL_IP=%%b
    )
)

echo.
echo Server starting...
echo.
echo ====================================================
echo              SERVER INFORMATION
echo ====================================================
echo.
echo Local access:     http://localhost:5000
echo Local access:     http://127.0.0.1:5000
if defined LOCAL_IP (
    echo Network access:   http://!LOCAL_IP!:5000
)
echo.
echo ====================================================
echo              DEMO CREDENTIALS
echo ====================================================
echo.
echo Admin Account:
echo   Email:    admin@spequip.com
echo   Password: admin123
echo.
echo Customer Account:
echo   Email:    user@spequip.com
echo   Password: user123
echo.
echo ====================================================
echo              CONTROLS
echo ====================================================
echo.
echo Press Ctrl+C to stop the server
echo Close this window to stop the server
echo.
echo Starting Flask development server...
echo.

:: Start the Flask application
python run.py

:: If we reach here, the server has stopped
echo.
echo ====================================================
echo Server has stopped.
echo ====================================================
echo.
pause
