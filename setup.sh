#!/bin/bash
# SpEquip E-Commerce Platform Setup Script for Unix/Linux/Mac
# This script sets up the entire application automatically

echo "===================================="
echo "SpEquip E-Commerce Platform Setup"
echo "===================================="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed."
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/6] Checking Python installation..."
python3 --version

# Create virtual environment
echo
echo "[2/6] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Removing old one..."
    rm -rf venv
fi
python3 -m venv venv

# Activate virtual environment
echo
echo "[3/6] Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo
echo "[4/6] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run setup script
echo
echo "[5/6] Setting up database and directories..."
python setup.py

# Seed database
echo
echo "[6/6] Seeding database with sample data..."
python seed_database.py

echo
echo "===================================="
echo "Setup completed successfully!"
echo "===================================="
echo
echo "To start the application:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run the application: python run.py"
echo "3. Open your browser to: http://localhost:5000"
echo
echo "Demo Credentials:"
echo "Admin: admin@spequip.com / admin123"
echo "User:  user@spequip.com / user123"
echo
echo "Press Enter to start the application now..."
read

# Start the application
echo "Starting SpEquip application..."
python run.py
