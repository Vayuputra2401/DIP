import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\intensity_transformations'
output_file = os.path.join(output_dir, 'histogram_analysis_output.png')

# Load image
img = cv2.imread(image_path, 0) # Load as grayscale for intensity analysis
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Calculate Histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image (Grayscale)")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Intensity Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist)
plt.xlim([0, 256])

# Save and show
plt.savefig(output_file)
print(f"Histogram analysis saved to {output_file}")
# plt.show() # Commented out for batch execution
