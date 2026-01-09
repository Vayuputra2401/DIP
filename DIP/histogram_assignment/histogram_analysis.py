import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\histogram_assignment'
output_file = os.path.join(output_dir, 'histogram_variants_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Generate Variants
# 1. Dark Image: divide values
img_dark = (img * 0.5).astype(np.uint8)

# 2. Bright Image: add values and clip
img_bright = np.clip(img * 1.5, 0, 255).astype(np.uint8)

# 3. Low Contrast: squish range to [100, 150]
img_low_contrast = (img * (50/255) + 100).astype(np.uint8)

images = [img, img_dark, img_bright, img_low_contrast]
titles = ["Original", "Dark", "Bright", "Low Contrast"]

# Plotting
plt.figure(figsize=(12, 12))

for i in range(4):
    # Image
    plt.subplot(4, 2, i*2 + 1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255) # Fix vmin/vmax for accurate visual comparison
    plt.axis('off')
    
    # Histogram
    plt.subplot(4, 2, i*2 + 2)
    hist = cv2.calcHist([images[i]], [0], None, [256], [0, 256])
    plt.title(f"{titles[i]} Histogram")
    plt.plot(hist)
    plt.xlim([0, 256])

plt.tight_layout()
plt.savefig(output_file)
print(f"Histogram analysis variants saved to {output_file}")
# plt.show()
