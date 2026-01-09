import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\sampling_quantization'
output_file = os.path.join(output_dir, 'sampling_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Sampling parameters
factors = [1, 2, 4, 8, 16, 32]

plt.figure(figsize=(15, 10))

for i, f in enumerate(factors):
    # Downsample
    # We can use slicing [::f, ::f] which is equivalent to nearest neighbor sampling
    # or cv2.resize for different interpolations. Slicing is the purest "sampling".
    h, w = img.shape
    new_h, new_w = h // f, w // f
    # img_sampled = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_NEAREST)
    img_sampled = img[::f, ::f]
    
    # Upsample back to original size for visualization of the "pixelation" effect
    img_display = cv2.resize(img_sampled, (w, h), interpolation=cv2.INTER_NEAREST)
    
    plt.subplot(2, 3, i + 1)
    plt.title(f"Sampling Factor: {f}\nRes: {new_w}x{new_h}")
    plt.imshow(img_display, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.savefig(output_file)
print(f"Sampling result saved to {output_file}")
# plt.show()
