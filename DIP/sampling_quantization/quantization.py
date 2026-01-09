import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\sampling_quantization'
output_file = os.path.join(output_dir, 'quantization_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Quantization levels to test
levels_list = [256, 32, 16, 8, 4, 2]

plt.figure(figsize=(15, 10))

for i, levels in enumerate(levels_list):
    # Calculate quantization step size
    # 256 / levels. e.g. for 4 levels, dim is 64.
    # We map [0-63] -> 0, [64-127] -> 1, etc.
    div = 256 // levels
    
    # Quantize
    # This integer division floors values to the nearest bin index
    q_vals = img // div
    
    # Map back to 0-255 range to see the image (reconstruction)
    # We map to the minimal value of the bin (q_vals * div) 
    # or better, the center of the bin: (q_vals * div) + div/2 
    # to maintain average brightness.
    img_quantized = np.uint8(q_vals * div)
    
    
    plt.subplot(2, 3, i + 1)
    plt.title(f"Quantization Levels: {levels}\nBits: {int(np.log2(levels))}")
    plt.imshow(img_quantized, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

plt.tight_layout()
plt.savefig(output_file)
print(f"Quantization result saved to {output_file}")
# plt.show()
