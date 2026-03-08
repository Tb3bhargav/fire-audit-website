import glob

for f in glob.glob(r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\*.html"):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add cache-buster to sticker images
    content = content.replace('.png" alt="" class="absolute z-10', '.png?v=2" alt="" class="absolute z-10')
    content = content.replace('.png" alt="" class="absolute z-30', '.png?v=2" alt="" class="absolute z-30')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Cache buster added.")
