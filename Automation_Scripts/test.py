import os

# Base path (change "YourUsername" to your actual username)
base_path = os.path.expandvars(r"C:\Users\Acer\Documents\My Games\Terraria\tModLoader\ModSources\BossManager")

# Folder structure
folders = [
    "Common",
    "Common/Systems",
    "Common/Configs",
    "Common/GlobalItems",
    "Common/GlobalNPCs",
    "Common/UI",
    "Localization"
]

# Files with their relative paths
files = {
    "BossManager.cs": "",
    "build.txt": "",
    "description.txt": "",
    "BossManager.csproj": "",
    "README.md": "Localization",
    "BossControlSystem.cs": "Common/Systems",
    "CommandSystem.cs": "Common/Systems",
    "BossConfig.cs": "Common/Configs",
    "BossSpawnerItem.cs": "Common/GlobalItems",
    "BossNPC.cs": "Common/GlobalNPCs",
    # Placeholder files
    "ConfigSystem.cs": "Common/Systems",
    "ProgressionSystem.cs": "Common/Systems",
    "BossManagerUI.cs": "Common/UI",
    "BossStatusPanel.cs": "Common/UI",
    "en-US_Mods.BossManager.hjson": "Localization"
}

# Placeholder content for hjson file
hjson_content = '''hjson{
  "DisplayName": "Boss Manager",
  "Description": "Comprehensive boss spawning management"
}
'''

# Create folders
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)

# Create files
for file_name, folder in files.items():
    file_path = os.path.join(base_path, folder, file_name)
    if file_name.endswith(".hjson"):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(hjson_content)
    else:
        open(file_path, "a").close()  # Create empty file

print("✅ BossManager mod folder structure and files created successfully.")
