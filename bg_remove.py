import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def process():
    in_path = r"C:\Users\nj322ws\.gemini\antigravity\brain\2f16a523-55e7-4f56-ae5c-3cc8f71c78c4\media__1772875553324.png"
    out_path = r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\prem_singh_dahiya.png"
    img = Image.open(in_path).convert("RGBA")
    
    w, h = img.size
    img_b = Image.new("RGBA", (w+2, h+2), (255, 255, 255, 255))
    img_b.paste(img, (1, 1))
    
    ImageDraw.floodfill(img_b, (0, 0), (255, 0, 255, 255), thresh=30)
    
    img = img_b.crop((1, 1, w+1, h+1))
    
    data = np.array(img)
    r,g,b = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (r == 255) & (g == 0) & (b == 255)
    
    data[mask, 3] = 0
    data[mask, 0] = 255 # reset color to white
    data[mask, 1] = 255
    data[mask, 2] = 255
    
    alpha_img = Image.fromarray(data[:,:,3])
    alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(radius=1.5))
    data[:,:,3] = np.minimum(np.array(alpha_img), data[:,:,3]) # Don't increase alpha inside
    
    Image.fromarray(data).save(out_path)

process()
