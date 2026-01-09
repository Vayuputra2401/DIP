import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\filters'
output_file = os.path.join(output_dir, 'output_freq_ideal_lowpass.png')

# Load image in grayscale
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# DFT
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

# Ideal Low Pass Filter Mask
d0 = 30 # Cut-off frequency
mask = np.zeros((rows, cols, 2), np.uint8)
for i in range(rows):
    for j in range(cols):
        distance = np.sqrt((i-crow)**2 + (j-ccol)**2)
        if distance <= d0:
            mask[i, j] = 1

# Apply mask and inverse DFT
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

# Normalize result for display
cv2.normalize(img_back, img_back, 0, 255, cv2.NORM_MINMAX)
img_back = np.uint8(img_back)

# Save result
cv2.imwrite(output_file, img_back)
print(f"Ideal Lowpass filter result saved to {output_file}")

# Display
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Grayscale")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Ideal Lowpass Filter")
plt.imshow(img_back, cmap='gray')
plt.axis('off')

plt.show()
