import os
import re

# Root folder for your EA export
root_dir = "RDP/EARoot"  # <-- update this to match your folder

# Regex to match target="_self" in <area> tags
pattern = re.compile(r'(<area\b[^>]*?)\s+target="_self"', re.IGNORECASE)

# Walk through all subfolders and files
for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".htm") or filename.endswith(".html"):
            filepath = os.path.join(foldername, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            # Replace only in area tags
            new_content = pattern.sub(r'\1 target="content"', content)

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"✅ Updated: {filepath}")
