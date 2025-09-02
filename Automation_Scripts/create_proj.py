import os
import subprocess
import django

# Customize your project and app name here
project_name = "FileManager"
app_name = "Storage"

# Base path (you can change this)
base_dir = r"D:\PythonProjects\Django"

# Full project path
project_path = os.path.join(base_dir, project_name)

# Step 1: Change to base directory
os.chdir(base_dir)

# Step 2: Create Django project
subprocess.run(["django-admin", "startproject", project_name])

# Step 3: Move into project folder
os.chdir(project_path)

# Step 4: Create app
subprocess.run([os.path.join(base_dir, ".venv", "Scripts", "python.exe"), "manage.py", "startapp", app_name])

# Step 5: Create Template structure
template_dir = os.path.join(project_path, "Template", "testapp")
os.makedirs(template_dir, exist_ok=True)
open(os.path.join(template_dir, "index.html"), 'a').close()

# Step 6: Create Static structure
static_css_dir = os.path.join(project_path, "Static", "css")
static_img_dir = os.path.join(project_path, "Static", "image")
os.makedirs(static_css_dir, exist_ok=True)
os.makedirs(static_img_dir, exist_ok=True)
open(os.path.join(static_css_dir, "style.css"), 'a').close()

print(f"Django project '{project_name}' with app '{app_name}' created successfully!")
