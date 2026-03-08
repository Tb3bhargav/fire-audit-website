import os
import glob
import re

html_files = glob.glob(r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\*.html")

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Match the interactive alive script
    script_pattern = re.compile(r'\s*<script>\s*// Interactive Alive Feeling script.*?lucide\.createIcons\(\);\s*</script>\s*', re.DOTALL)
    
    content = script_pattern.sub('\n    <script>\n        lucide.createIcons();\n    </script>\n', content)
    
    content = re.sub(r' +interact-element', '', content)
    content = re.sub(r' +data-speed="[^"]*"', '', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Removed interactivity.")
