import os
from PIL import Image
import numpy as np

img = Image.open(r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\images\stickers\fire_audit.png")
data = np.array(img)
alpha = data[:,:,3]
print(f"fire_audit.png: shape {data.shape}, max alpha {np.max(alpha)}, mean alpha {np.mean(alpha)}")

img2 = Image.open(r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\images\stickers\fire_truck.png")
data2 = np.array(img2)
alpha2 = data2[:,:,3]
print(f"fire_truck.png: shape {data2.shape}, max alpha {np.max(alpha2)}, mean alpha {np.mean(alpha2)}")

