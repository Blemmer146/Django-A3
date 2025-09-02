import os
import subprocess
from pathlib import Path

# ==== Default Names ====
default_project_name = "Career_Development_Platform"
default_app_name = "Login_Form"


# ==== Interactive Input ====
def get_user_input():
    """Get user input for project configuration"""
    print("=== Django Project Setup ===")

    # Get project name
    project_name = input(f"Enter project name (default: {default_project_name}): ").strip()
    if not project_name:
        project_name = default_project_name

    # Ask about multiple apps
    create_multiple = input("Do you want to create multiple apps? (y/n, default: n): ").strip().lower()

    apps = []
    if create_multiple in ['y', 'yes']:
        try:
            num_apps = int(input("How many apps do you want to create? "))
            if num_apps <= 0:
                print("Invalid number. Creating default app.")
                apps = [default_app_name]
            else:
                for i in range(num_apps):
                    app_name = input(f"Enter name for app {i + 1}: ").strip()
                    if app_name:
                        apps.append(app_name)
                    else:
                        apps.append(f"app{i + 1}")
        except ValueError:
            print("Invalid input. Creating default app.")
            apps = [default_app_name]
    else:
        # Single app - ask for name or use default
        single_app_name = input(f"Enter app name (default: {default_app_name}): ").strip()
        apps = [single_app_name if single_app_name else default_app_name]

    return project_name, apps


def create_app_structure(project_path, app_name, project_name):
    """Create directory structure and files for a single app"""
    # Create template and static folders for each app
    template_dir = os.path.join(project_path, "Template", app_name.lower())
    static_css_dir = os.path.join(project_path, "Static", "css")
    static_img_dir = os.path.join(project_path, "Static", "image")

    os.makedirs(template_dir, exist_ok=True)
    os.makedirs(static_css_dir, exist_ok=True)
    os.makedirs(static_img_dir, exist_ok=True)

    # Create index.html for this app
    index_path = os.path.join(template_dir, "index.html")
    index_html = f"""<!DOCTYPE html>
{{% load static %}}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{{{ project_name }}}} - {app_name}</title>
    <link rel="stylesheet" href="{{% static 'css/style.css' %}}">
</head>
<body>
    <div class="container">
        <header>
            <h1>Welcome to {{{{ project_name }}}}</h1>
            <h2>{app_name} App</h2>
            <p>Your Django project is running successfully!</p>
        </header>

        <main>
            <div class="card">
                <h2>App Information</h2>
                <ul>
                    <li><strong>Project:</strong> {{{{ project_name }}}}</li>
                    <li><strong>Current App:</strong> {app_name}</li>
                    <li><strong>Django Version:</strong> {{{{ django_version }}}}</li>
                    <li><strong>Python Version:</strong> {{{{ python_version }}}}</li>
                    <li><strong>Debug Mode:</strong> {{{{ debug_status|yesno:"ON,OFF" }}}}</li>
                </ul>
            </div>

            <div class="card">
                <h2>All Apps in Project</h2>
                <ul>
                    {{% for app in all_apps %}}
                    <li><a href="/{{% if app != '{app_name}' %}}{{{{ app }}}}/{{% endif %}}">{{{{ app }}}}</a></li>
                    {{% endfor %}}
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


def create_app_views(project_path, app_name, project_name, all_apps):
    """Create views.py for a single app"""
    views_path = os.path.join(project_path, app_name, "views.py")
    views_code = f"""from django.shortcuts import render
from django.conf import settings
import django
import sys

def index(request):
    \"\"\"
    Simple index view for {app_name} app
    \"\"\"
    context = {{
        'project_name': '{project_name}',
        'app_name': '{app_name}',
        'all_apps': {all_apps},
        'django_version': django.get_version(),
        'python_version': f"{{sys.version_info.major}}.{{sys.version_info.minor}}.{{sys.version_info.micro}}",
        'debug_status': settings.DEBUG,
    }}

    return render(request, '{app_name.lower()}/index.html', context)
"""

    with open(views_path, "w") as f:
        f.write(views_code.strip())


def create_app_urls(project_path, app_name):
    """Create urls.py for a single app"""
    app_urls_path = os.path.join(project_path, app_name, "urls.py")
    urls_code = f"""from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
    path('', views.index, name='index'),
]
"""

    with open(app_urls_path, "w") as f:
        f.write(urls_code.strip())


def update_main_urls(project_path, project_name, apps):
    """Update main urls.py to include all app URLs"""
    urls_path = os.path.join(project_path, project_name, "urls.py")

    urls_content = f"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
"""

    # Add URL patterns for each app
    for i, app in enumerate(apps):
        if i == 0:  # First app gets root URL
            urls_content += f"    path('', include('{app}.urls')),\n"
        urls_content += f"    path('{app}/', include('{app}.urls')),\n"

    urls_content += "]\n"

    with open(urls_path, "w") as f:
        f.write(urls_content)


# ==== Main Execution ====
project_name, apps = get_user_input()

# ==== Paths ====
base_dir = r"D:\PythonProjects\Django"
project_path = os.path.join(base_dir, project_name)
venv_python = os.path.join(base_dir, ".venv", "Scripts", "python.exe")

print(f"\n📁 Creating project: {project_name}")
print(f"📱 Creating apps: {', '.join(apps)}")
print("=" * 50)

# ==== Step 1: Go to base dir ====
os.chdir(base_dir)

# ==== Step 2: Create Django project ====
print("🔧 Creating Django project...")
subprocess.run(["django-admin", "startproject", project_name])

# ==== Step 3: Move to project folder ====
os.chdir(project_path)

# ==== Step 4: Create all apps ====
print("📱 Creating Django apps...")
for app in apps:
    print(f"   - Creating {app}...")
    subprocess.run([venv_python, "manage.py", "startapp", app])

# ==== Step 5: Create shared static folder and CSS ====
print("📁 Creating static folders...")
static_css_dir = os.path.join(project_path, "Static", "css")
static_img_dir = os.path.join(project_path, "Static", "image")
os.makedirs(static_css_dir, exist_ok=True)
os.makedirs(static_img_dir, exist_ok=True)

# Create shared CSS file
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

header h2 {
    color: #3498db;
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

# ==== Step 6: Modify settings.py ====
print("⚙️  Configuring settings.py...")
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
        new_lines.append(line)
        continue

    # Add all apps to INSTALLED_APPS
    if not installed_app_added and "INSTALLED_APPS = [" in line:
        new_lines.append(line)
        for app in apps:
            new_lines.append(f"    '{app}',\n")
        installed_app_added = True
        continue

    # Default: Keep the line as-is
    new_lines.append(line)

# Write back modified settings.py
with open(settings_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# ==== Step 7: Create structure for each app ====
print("📄 Creating app templates and views...")
for app in apps:
    print(f"   - Setting up {app}...")
    create_app_structure(project_path, app, project_name)
    create_app_views(project_path, app, project_name, apps)
    create_app_urls(project_path, app)

# ==== Step 8: Update main URLs ====
print("🔗 Configuring URL routing...")
update_main_urls(project_path, project_name, apps)

print("=" * 50)
print(f"✅ Django project '{project_name}' created successfully!")
print(f"📱 Created {len(apps)} app(s): {', '.join(apps)}")
print(f"🌐 Run 'python manage.py runserver' to start your project")
print(f"🔗 Visit http://127.0.0.1:8000/ to see the main app")
for app in apps:
    if app != apps[0]:  # Don't show URL for first app since it's at root
        print(f"🔗 Visit http://127.0.0.1:8000/{app}/ to see the {app} app")
print(f"🔐 Visit http://127.0.0.1:8000/admin/ for the admin panel")
print(f"💡 Run 'python manage.py migrate' if you plan to use the database")