#!/usr/bin/env python3
"""
SpEquip E-Commerce Platform Setup Script
This script initializes the database and creates necessary directories.
"""

import os
import sys

def setup_application():
    """Setup the SpEquip application."""
    print("Setting up SpEquip E-Commerce Platform...")
    
    # Add current directory to Python path
    sys.path.insert(0, os.path.abspath('.'))
    
    # Import here to avoid issues with missing modules
    try:
        from app import create_app, db
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Please ensure all dependencies are installed: pip install -r requirements.txt")
        return False
    
    # Create the app instance
    app = create_app()
    
    # Create directories if they don't exist
    directories = [
        'app/static/css',
        'app/static/js',
        'app/static/images/products',
        'app/templates/admin',
        'app/templates/user',
        'app/templates/base',
        'instance'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Initialize the database
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")
    
    print("\nSetup completed successfully!")
    print("Run 'python seed_database.py' to populate with sample data.")
    print("Then run 'python run.py' to start the application.")
    return True

if __name__ == '__main__':
    setup_application()
