import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\intensity_transformations'
output_file = os.path.join(output_dir, 'log_transformation_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Log Transformation: s = c * log(1 + r)
# c = 255 / log(1 + max_pixel_value)
c = 255 / np.log(1 + np.max(img))
log_img = c * (np.log(1 + img.astype(np.float32)))
log_img = np.array(log_img, dtype=np.uint8)

# Histograms
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_log = cv2.calcHist([log_img], [0], None, [256], [0, 256])

# Visualization
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Log Transformed Image")
plt.imshow(log_img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Original Histogram")
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(2, 2, 4)
plt.title("Log Transform Histogram")
plt.plot(hist_log, color='purple')
plt.xlim([0, 256])

plt.tight_layout()
plt.savefig(output_file)
print(f"Log transformation result saved to {output_file}")
# plt.show()
