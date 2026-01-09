import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\histogram_assignment'
output_file = os.path.join(output_dir, 'histogram_equalization_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Custom Implementation of Histogram Equalization
# 1. Calculate Histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# 2. Probability Distribution Function (PDF)
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max() # Normalized for plotting

# 3. CDF Mask
cdf_m = np.ma.masked_equal(cdf, 0)

# 4. Equalization Formula
# s = (CDF(r) - CDF_min) / ((TotalPixels - CDF_min) * (L-1))
# Simple version: s = CDF(r) scaled to 255
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')

# 5. Map original values to new values
img_eq = cdf_final[img]

# OpenCV implementation for verification (and robustness)
# img_eq_cv2 = cv2.equalizeHist(img) 

# Histograms
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])

# Visualization
plt.figure(figsize=(12, 12))

# Original
plt.subplot(3, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.title("Original Histogram & CDF")
plt.plot(hist_original, color='blue', label='Histogram')
# Scale CDF to fit plot for visualization
plt.plot(cdf_normalized, color = 'b', linestyle='--', label='CDF') 
plt.legend(loc = 'upper left')
plt.xlim([0, 256])

# Equalized
plt.subplot(3, 2, 3)
plt.title("Equalized Image (Custom Impl)")
plt.imshow(img_eq, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.title("Equalized Histogram")
plt.plot(hist_eq, color='green')
plt.xlim([0, 256])

# CDF Comparison plot
plt.subplot(3, 2, 5)
plt.title("Transformation Function (CDF)")
plt.plot(cdf_final, color='black')
plt.xlabel("Input Pixel Value (r)")
plt.ylabel("Output Pixel Value (s)")
plt.grid(True)

plt.tight_layout()
plt.savefig(output_file)
print(f"Histogram equalization result saved to {output_file}")
# plt.show()
