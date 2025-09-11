import os
import subprocess
from pathlib import Path

# ==== Custom Names ====
project_name = "EmpManage"
app_name = "EmpDetail"

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

# ==== Step 7: Write simple index.html content ====
index_path = os.path.join(template_dir, "index.html")
index_html = """<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project_name }} - Home</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="container">
        <header>
            <h1>Welcome to {{ project_name }}</h1>
            <p>Your Django project is running successfully!</p>
        </header>

        <main>
            <div class="card">
                <h2>Project Information</h2>
                <ul>
                    <li><strong>Project:</strong> {{ project_name }}</li>
                    <li><strong>App:</strong> {{ app_name }}</li>
                    <li><strong>Django Version:</strong> {{ django_version }}</li>
                    <li><strong>Python Version:</strong> {{ python_version }}</li>
                    <li><strong>Debug Mode:</strong> {{ debug_status|yesno:"ON,OFF" }}</li>
                </ul>
            </div>

            <div class="card">
                <h2>Quick Links</h2>
                <ul>
                    <li><a href="/admin/">Admin Panel</a></li>
                    <li><a href="https://docs.djangoproject.com/" target="_blank">Django Documentation</a></li>
                </ul>
            </div>
        </main>

        <footer>
            <p>Created using Blemmer's Django Automation Script</p>
        </footer>
    </div>
</body>
</html>
"""
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

# ==== Step 8: Write simple style.css content ====
style_css_path = os.path.join(static_css_dir, "style.css")
style_css = """/* Simple, clean styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    margin-bottom: 40px;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
    color: #2c3e50;
    margin-bottom: 10px;
}

header p {
    color: #666;
    font-size: 1.1rem;
}

main {
    display: grid;
    gap: 20px;
    margin-bottom: 40px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.card h2 {
    color: #2c3e50;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #3498db;
}

.card ul {
    list-style: none;
}

.card ul li {
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}

.card ul li:last-child {
    border-bottom: none;
}

.card a {
    color: #3498db;
    text-decoration: none;
    font-weight: 500;
}

.card a:hover {
    text-decoration: underline;
}

footer {
    text-align: center;
    padding: 20px;
    color: #666;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Responsive */
@media (max-width: 768px) {
    .container {
        padding: 15px;
    }

    .card {
        padding: 20px;
    }
}
"""
with open(style_css_path, 'w', encoding='utf-8') as f:
    f.write(style_css)

# Step 9: Create simple views.py content
views_path = os.path.join(project_path, app_name, "views.py")
views_code = f"""from django.shortcuts import render
from django.conf import settings
import django
import sys

def debug(request):
    \"\"\"
    Simple debug view with basic project information
    \"\"\"
    context = {{
        'project_name': '{project_name}',
        'app_name': '{app_name}',
        'django_version': django.get_version(),
        'python_version': f"{{sys.version_info.major}}.{{sys.version_info.minor}}.{{sys.version_info.micro}}",
        'debug_status': settings.DEBUG,
    }}

    return render(request, 'testapp/index.html', context)
"""

with open(views_path, "w") as f:
    f.write(views_code.strip())

# Step 10: Update urls.py to include debug path
urls_path = os.path.join(project_path, project_name, "urls.py")
with open(urls_path, "r") as f:
    urls_content = f.read()

if f"from {app_name} import views" not in urls_content:
    urls_content = urls_content.replace(
        "from django.urls import path",
        f"from django.urls import path\nfrom {app_name} import views"
    )

# Add path only if not already added
if "path('debug/', views.debug" not in urls_content:
    insert_point = urls_content.find("urlpatterns = [")
    start = urls_content[:insert_point]
    rest = urls_content[insert_point:]
    new_path = "    path('debug/', views.debug, name='debug'),\n"
    urls_content = start + rest.replace("urlpatterns = [", f"urlpatterns = [\n{new_path}", 1)

with open(urls_path, "w") as f:
    f.write(urls_content)

print(f"✅ Django project '{project_name}' with app '{app_name}' created successfully!")
print(f"🌐 Run 'python manage.py runserver' and visit http://127.0.0.1:8000/debug/ to see your project")
print(f"🔐 Visit http://127.0.0.1:8000/admin/ for the admin panel (run 'python manage.py migrate' first if needed)")