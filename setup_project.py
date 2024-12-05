import os
import subprocess
from pathlib import Path
import json

def create_directory_structure(base_path):
    # Base project structure
    directories = [
        'backend/app',
        'backend/migrations',
        'backend/tests',
        'frontend/public',
        'frontend/src/components',
        'frontend/src/pages',
        'frontend/src/services',
        'data/raw',
        'data/processed',
        'data/scripts',
        'docs',
        'docker'
    ]
    
    # Create directories
    for dir_path in directories:
        full_path = Path(base_path) / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        # Create empty .gitkeep file to track empty directories
        (full_path / '.gitkeep').touch()

def create_basic_files(base_path):
    # Backend files
    files = {
        'backend/requirements.txt': 'flask\nflask-sqlalchemy\nflask-migrate\npython-dotenv\nrequests',
        'backend/app/__init__.py': '',
        'backend/app/models.py': '',
        'backend/app/routes.py': '',
        'backend/app/utils.py': '',
        'backend/app/config.py': '',
        'backend/run.py': '',
        
        # Frontend files
        'frontend/public/index.html': '<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8" />\n    <title>Multi-Dimensional Metrics Platform</title>\n  </head>\n  <body>\n    <div id="root"></div>\n  </body>\n</html>',
        'frontend/src/index.js': '',
        'frontend/src/App.js': '',
        'frontend/src/App.css': '',
        
        # Docker files
        'docker/backend.Dockerfile': 'FROM python:3.9\nWORKDIR /app\nCOPY backend/requirements.txt .\nRUN pip install -r requirements.txt\nCOPY backend .\nCMD ["python", "run.py"]',
        'docker/frontend.Dockerfile': 'FROM node:16\nWORKDIR /app\nCOPY frontend/package.json .\nRUN npm install\nCOPY frontend .\nCMD ["npm", "start"]',
        
        # Documentation
        'docs/metrics_explanation.md': '# Metrics Explanation\n\nDetailed explanation of the platform metrics will go here.',
        'docs/user_guide.md': '# User Guide\n\nUser guide for the platform will go here.',
        
        # Root files
        '.gitignore': '''
node_modules/
__pycache__/
*.pyc
.env
.DS_Store
venv/
dist/
build/
''',
        'README.md': '# Multi-Dimensional Metrics Platform\n\nA comprehensive platform for measuring prosperity through integrated economic, social, environmental, and technological metrics.'
    }
    
    # Create package.json for frontend
    package_json = {
        "name": "multi-dimensional-metrics-platform",
        "version": "0.1.0",
        "private": True,
        "dependencies": {
            "@testing-library/jest-dom": "^5.16.5",
            "@testing-library/react": "^13.4.0",
            "@testing-library/user-event": "^13.5.0",
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-scripts": "5.0.1",
            "recharts": "^2.4.3",
            "web-vitals": "^2.1.4"
        },
        "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject"
        }
    }
    
    # Write all files
    for file_path, content in files.items():
        full_path = Path(base_path) / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
    
    # Write package.json with proper formatting
    package_json_path = Path(base_path) / 'frontend/package.json'
    with open(package_json_path, 'w') as f:
        json.dump(package_json, f, indent=2)

def main():
    # Set the base path
    base_path = Path(r'C:\Users\johnv\MultidimensionalMetrics')
    
    # Create the base directory if it doesn't exist
    base_path.mkdir(parents=True, exist_ok=True)
    
    # Create project structure
    print(f"Creating directory structure in {base_path}...")
    create_directory_structure(base_path)
    
    print("Creating basic files...")
    create_basic_files(base_path)
    
    print("\nProject structure created successfully!")
    print(f"Project location: {base_path}")

if __name__ == "__main__":
    main()