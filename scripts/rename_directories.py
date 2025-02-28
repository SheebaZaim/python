import os
from pathlib import Path

def rename_directories():
    # Get project root directory
    project_root = Path(__file__).parent.parent
    
    # Rename directories
    renames = [
        ("front_end", "frontend"),
        ("Backend", "backend")
    ]
    
    for old_name, new_name in renames:
        old_path = project_root / old_name
        new_path = project_root / new_name
        
        if old_path.exists():
            try:
                old_path.rename(new_path)
                print(f"Successfully renamed {old_name} to {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {str(e)}")

    # Update imports in all Python files
    for py_file in project_root.rglob("*.py"):
        try:
            content = py_file.read_text()
            # Replace imports
            updated_content = content.replace("from front_end", "from frontend")
            updated_content = updated_content.replace("from Backend", "from backend")
            updated_content = updated_content.replace("import front_end", "import frontend")
            updated_content = updated_content.replace("import Backend", "import backend")
            
            if content != updated_content:
                py_file.write_text(updated_content)
                print(f"Updated imports in {py_file}")
        except Exception as e:
            print(f"Error updating {py_file}: {str(e)}")

if __name__ == "__main__":
    rename_directories()

