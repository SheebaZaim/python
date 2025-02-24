from pathlib import Path
import shutil
import os

def setup_project():
    # Define project structure
    project_root = Path(__file__).parent.parent
    directories = [
        "front_end/assets",
        "front_end/data",
        "front_end/utils",
        "backend/data",
        "scripts"
    ]
    
    # Create directories
    for directory in directories:
        (project_root / directory).mkdir(parents=True, exist_ok=True)
    
    # Generate logo
    from generate_logo import create_logo
    create_logo()
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    setup_project()

