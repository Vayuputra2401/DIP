import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\filters'
output_file = os.path.join(output_dir, 'output_spatial_mean.png')

# Load image
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Convert to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Mean Filter (3x3 Averaging)
# Can use cv2.blur or manually filter2D with ones(3,3)/9
mean_blur = cv2.blur(img, (5, 5)) 

# Save result
cv2.imwrite(output_file, mean_blur)
print(f"Mean filter result saved to {output_file}")

# Display
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Mean Filter (5x5)")
plt.imshow(cv2.cvtColor(mean_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
