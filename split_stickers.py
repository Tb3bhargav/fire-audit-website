import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import glob

brain_dir = r"C:\Users\nj322ws\.gemini\antigravity\brain\f1894594-9fd7-4b4d-b9db-1f7bd9e32803"
out_dir = r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\images\stickers"

files = glob.glob(os.path.join(brain_dir, "*.*"))

def remove_bg(img):
    img = img.convert("RGBA")
    w, h = img.size
    # Add a border so floodfill can go around
    img_b = Image.new("RGBA", (w+2, h+2), (255, 255, 255, 255))
    img_b.paste(img, (1, 1))
    
    # Floodfill from top-left with magenta
    ImageDraw.floodfill(img_b, (0, 0), (255, 0, 255, 255), thresh=40)
    
    img = img_b.crop((1, 1, w+1, h+1))
    
    data = np.array(img)
    r,g,b = data[:,:,0], data[:,:,1], data[:,:,2]
    # mask where it's magenta
    mask = (r == 255) & (g == 0) & (b == 255)
    
    data[mask, 3] = 0
    data[mask, 0] = 255
    data[mask, 1] = 255
    data[mask, 2] = 255
    
    return Image.fromarray(data)

with open(r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\analyze_images.txt", "w") as out:
    for idx, f in enumerate(sorted(files)):
        img = Image.open(f)
        w, h = img.size
        out.write(f"Image {idx}: {os.path.basename(f)}, {w}x{h}\n")
        
        # Check if it should be split
        if h > w * 1.5:
            out.write("  -> Splitting into top and bottom it seems.\n")
            top = img.crop((0, 0, w, h//2))
            bottom = img.crop((0, h//2, w, h))
            remove_bg(top).save(os.path.join(out_dir, f"split_{idx}_top.png"))
            remove_bg(bottom).save(os.path.join(out_dir, f"split_{idx}_bottom.png"))
        else:
            remove_bg(img).save(os.path.join(out_dir, f"img_{idx}.png"))
