import os
import subprocess
from pathlib import Path

# ==== Custom Names ====
project_name = "Creation"
app_name = "Demo"

# ==== Paths ====
base_dir = r"D:\PythonProjects\Django"
project_path = os.path.join(base_dir, project_name)
venv_python = os.path.join(base_dir, ".venv", "Scripts", "python.exe")

# ==== Step 1: Go to base dir ====
os.chdir(base_dir)

# ==== Step 2: Create Django project ====
subprocess.run(["django-admin", "startproject", project_name])

# ==== Step 3: Move to project folder ====
os.chdir(project_path)

# ==== Step 4: Create app ====
subprocess.run([venv_python, "manage.py", "startapp", app_name])

# ==== Step 5: Create template/static folders ====
template_dir = os.path.join(project_path, "Template", "testapp")
static_css_dir = os.path.join(project_path, "Static", "css")
static_img_dir = os.path.join(project_path, "Static", "image")
os.makedirs(template_dir, exist_ok=True)
os.makedirs(static_css_dir, exist_ok=True)
os.makedirs(static_img_dir, exist_ok=True)
open(os.path.join(template_dir, "index.html"), 'a').close()
open(os.path.join(static_css_dir, "style.css"), 'a').close()

# ==== Step 6: Modify settings.py ====
settings_path = os.path.join(project_path, project_name, "settings.py")
with open(settings_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
htmls_static_added = False
dirs_replaced = False
staticfiles_added = False
installed_app_added = False
pending_static_block = False

for line in lines:
    # Add HTMLS and STATIC below BASE_DIR
    if not htmls_static_added and "BASE_DIR = Path(__file__)" in line:
        new_lines.append(line)
        new_lines.append("HTMLS = BASE_DIR / 'Template'\n")
        new_lines.append("STATIC = BASE_DIR / 'Static'\n")
        htmls_static_added = True
        continue

    # Replace DIRS: [] only once
    if not dirs_replaced and "'DIRS': []" in line:
        new_lines.append("        'DIRS': [HTMLS],\n")
        dirs_replaced = True
        continue

    # Capture STATIC_URL line and flag for next line
    if "STATIC_URL = 'static/'" in line:
        new_lines.append(line)
        pending_static_block = True
        continue

    # Add STATICFILES_DIRS and STATIC_ROOT right after STATIC_URL
    if pending_static_block:
        new_lines.append("STATICFILES_DIRS = [\n    STATIC,\n]\n")
        new_lines.append("STATIC_ROOT = BASE_DIR / 'staticfiles'\n")
        staticfiles_added = True
        pending_static_block = False
        # Don't skip this line, process it as normal
        new_lines.append(line)
        continue

    # Add app to INSTALLED_APPS
    if not installed_app_added and "INSTALLED_APPS = [" in line:
        new_lines.append(line)
        new_lines.append(f"    '{app_name}',\n")
        installed_app_added = True
        continue

    # Default: Keep the line as-is
    new_lines.append(line)

# Write back modified settings.py
with open(settings_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"✅ Django project '{project_name}' with app '{app_name}' and settings patched successfully!")
