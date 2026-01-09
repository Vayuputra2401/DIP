import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\histogram_assignment'
output_file = os.path.join(output_dir, 'contrast_stretching_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Create a low contrast image for demonstration
# Map [0, 255] -> [r_min, r_max] = [80, 150]
r_min, r_max = 80, 150
img_low = ((img / 255.0) * (r_max - r_min) + r_min).astype(np.uint8)

# Contrast Stretching Implementation
# s = ((r - r_min) / (r_max - r_min)) * (L - 1)
# Note: In practice, we take actual min/max of the image, not theoretical input bounds.
actual_min = np.min(img_low)
actual_max = np.max(img_low)

# Apply stretching
# Epsilon to avoid division by zero
epsilon = 1e-5
img_stretched = ((img_low - actual_min) / (actual_max - actual_min + epsilon)) * 255
img_stretched = np.clip(img_stretched, 0, 255).astype(np.uint8)

# Histograms
hist_low = cv2.calcHist([img_low], [0], None, [256], [0, 256])
hist_stretched = cv2.calcHist([img_stretched], [0], None, [256], [0, 256])

# Visualization
plt.figure(figsize=(10, 8))

# Images
plt.subplot(2, 2, 1)
plt.title(f"Low Contrast Image\n(Range: {actual_min}-{actual_max})")
plt.imshow(img_low, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title(f"Contrast Stretched Image\n(Range: {np.min(img_stretched)}-{np.max(img_stretched)})")
plt.imshow(img_stretched, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

# Histograms
plt.subplot(2, 2, 3)
plt.title("Low Contrast Histogram")
plt.plot(hist_low, color='red')
plt.xlim([0, 256])

plt.subplot(2, 2, 4)
plt.title("Stretched Histogram")
plt.plot(hist_stretched, color='green')
plt.xlim([0, 256])

plt.tight_layout()
plt.savefig(output_file)
print(f"Contrast stretching result saved to {output_file}")
# plt.show()
