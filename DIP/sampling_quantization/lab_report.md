# Sampling & Quantization Lab Report

## Objective
The objective is to understand the two fundamental processes of digitizing an image: Sampling (Spatial discretization) and Quantization (Amplitude discretization).

## Theory & Implementation

### 1. Image Sampling
Sampling refers to the discretization of the spatial coordinates $(x, y)$. The sampling rate determines the spatial resolution.
- **Method**: Implemented by downsampling the image (taking every $k$-th pixel). To visualize the effect, we upsampled the result back to the original size using Nearest Neighbor interpolation.
- **Observations**: As the sampling factor increases (e.g., from 1 to 32), the spatial resolution decreases. The image becomes "pixelated" or "blocky". By factor 32, fine details like eyes or text become unrecognizable blocks. This creates a "checkerboard" effect.

### 2. Image Quantization
Quantization refers to the discretization of the amplitude (intensity) values. The number of levels determines the color depth.
- **Method**: Implemented by reducing the number of gray levels from 256 (8-bit) down to 2 levels (1-bit).
- **Formula**: $val_{quantized} = floor(val / divisor) \times divisor$.
- **Observations**:
    - **256 Levels**: Smooth gradients.
    - **16 Levels**: "False Contouring" (banding) begins to appear in smooth areas like skin or background.
    - **4 Levels**: The image looks like a poster or cartoon.
    - **2 Levels**: Binary image (Black and White only). All nuance is lost.

## Analysis and Comparison

| Process | Parameter | Visual Artifact | Impact on Quality |
| :--- | :--- | :--- | :--- |
| **Sampling** | Sampling Factor (Stride) | **Pixelation** (Blockiness) | Loss of fine spatial detail / sharpness. |
| **Quantization** | Number of Levels | **False Contouring** (Banding) | Loss of smooth gradients / texture. |

### Insights
- **Sampling** is about *how many* pixels you have. If you have too few, you can't represent small objects (Aliasing).
- **Quantization** is about *how precise* each pixel is. If you have too little precision, smooth transitions look like stairs.
- A high-quality image requires both sufficient sampling rate (to satisfy Nyquist criteria for details) and sufficient quantization levels (typically 8-bit or higher for human vision) to appear "continuous".

## Visual Examples
*Refer to the following generated images in the `sampling_quantization/` directory:*

- **Sampling**: `sampling_quantization/sampling_output.png` (Shows the progression from sharp to blocky).
- **Quantization**: `sampling_quantization/quantization_output.png` (Shows the progression from smooth to banded to binary).

## Conclusion
We successfully demonstrated that reducing spatial resolution leads to pixelation, while reducing intensity resolution leads to false contouring. Balancing these two factors is key to optimizing image storage and transmission while maintaining perceptual quality.
