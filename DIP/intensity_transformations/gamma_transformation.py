import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\intensity_transformations'
output_file = os.path.join(output_dir, 'gamma_transformation_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Gamma function
def apply_gamma(image, gamma, c=1.0):
    # s = c * r^gamma
    # Normalize to [0, 1] first
    norm_img = image / 255.0
    s = c * (norm_img ** gamma)
    # Scale back to [0, 255]
    s = np.uint8(np.clip(s * 255, 0, 255))
    return s

# Apply Gamma
gamma_bright = 0.5 # Brighten
gamma_dark = 2.0   # Darken

img_bright = apply_gamma(img, gamma_bright)
img_dark = apply_gamma(img, gamma_dark)

# Histograms
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_bright = cv2.calcHist([img_bright], [0], None, [256], [0, 256])
hist_dark = cv2.calcHist([img_dark], [0], None, [256], [0, 256])

# Visualization
plt.figure(figsize=(15, 10))

# Row 1: Images
plt.subplot(2, 3, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title(f"Gamma = {gamma_bright} (Brighten)")
plt.imshow(img_bright, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title(f"Gamma = {gamma_dark} (Darken)")
plt.imshow(img_dark, cmap='gray')
plt.axis('off')

# Row 2: Histograms
plt.subplot(2, 3, 4)
plt.title("Original Histogram")
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(2, 3, 5)
plt.title(f"Gamma = {gamma_bright} Histogram")
plt.plot(hist_bright, color='green')
plt.xlim([0, 256])

plt.subplot(2, 3, 6)
plt.title(f"Gamma = {gamma_dark} Histogram")
plt.plot(hist_dark, color='red')
plt.xlim([0, 256])

plt.tight_layout()
plt.savefig(output_file)
print(f"Gamma transformation result saved to {output_file}")
# plt.show()
