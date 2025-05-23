import os 
import json

def is_react_project(base_path = "."):

    package_json_path = os.path.join(base_path, 'package.json')

    if not os.path.exists(package_json_path):
        return False
    
    try: 
        with open(package_json_path, 'r') as f:
            package_data = json.load(f)
            dependencies = package_data.get("dependencies", {})
            dev_dependencies = package_data.get("devDependencies", {})
            return 'react' in dependencies or 'react' in dev_dependencies
    
    except Exception as e:
        print(f"Error reading package.json: {e}")
        return False
    
    
def detect_typescript(base_path="."):
    if os.path.exists(os.path.join(base_path, "tsconfig.json")):
        return True
    for root, _, files in os.walk(os.path.join(base_path, "src")):
        for file in files:
            if file.endswith(".ts") or file.endswith(".tsx"):
                return True
    return False