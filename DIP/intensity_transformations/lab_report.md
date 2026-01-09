# Intensity Transformations Lab Report

## Objective
The objective of this assignment is to explore intensity transformations in digital images. We implemented various techniques to manipulate the pixel intensities and analyzed their effects using histograms.

## Theory & Implementation

### 1. Histogram Analysis
A histogram represents the distribution of pixel intensities in an image.
- **X-axis**: Pixel intensity values (0-255).
- **Y-axis**: Frequency (count) of pixels with that intensity.
- **Relevance**: It gives insight into contrast, brightness, and dynamic range. A histogram skewed to the left indicates a dark image; to the right, a bright image.

### 2. Photographic Negative
**Transformation**: $s = L - 1 - r$  
where $r$ is the input pixel value, $s$ is the output, and $L$ is the number of gray levels (256).
- **Effect**: Inverts the image. Black becomes White, White becomes Black.
- **Histogram**: The histogram is reversed horizontally.
- **Application**: Enhancing white or gray details embedded in dark regions, especially in medical imaging (e.g., mammograms).

### 3. Gamma Transformation (Power-Law)
**Transformation**: $s = c \cdot r^\gamma$  
- **$\gamma < 1$**: Maps a narrow range of dark input values to a wider range of output values. **Brightens** the image.
- **$\gamma > 1$**: Maps a narrow range of bright input values to a wider range of output values. **Darkens** the image.
- **Histogram**:
    - $\gamma < 1$: Histogram shifts to the right (brighter).
    - $\gamma > 1$: Histogram shifts to the left (darker).
- **Application**: Gamma correction for display devices, contrast manipulation.

### 4. Logarithmic Transformation
**Transformation**: $s = c \cdot \log(1 + r)$  
- **Effect**: Expands the values of dark pixels (low intensities) into a wider range of output levels. Highly compresses the high-level values.
- **Histogram**: Significant shift towards the right, as dark pixels are boosted.
- **Application**: Displaying Fourier spectra (which have high dynamic range), enhancing details in dark areas.

## Analysis and Comparison

| Transformation | Visual Effect | Histogram Change | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Negative** | Inverted colors | Horizontally flipped | Analyzing details in dark backgrounds. |
| **Gamma ($\gamma < 1$)** | Brightens image | Shifts Right (spreads low values) | Correcting underexposed images. |
| **Gamma ($\gamma > 1$)** | Darkens image | Shifts Left (spreads high values) | Correcting overwashed/bright images. |
| **Log** | Drastic Brightening | Shifts Right (strong compression of highs) | High dynamic range data (e.g., Fourier). |

## Visual Examples
*Refer to the following generated images in the `intensity_transformations/` directory:*

- **Histogram**: `intensity_transformations/histogram_analysis_output.png`
- **Negative**: `intensity_transformations/negative_transformation_output.png`
- **Gamma**: `intensity_transformations/gamma_transformation_output.png`
- **Log**: `intensity_transformations/log_transformation_output.png`

## Conclusion
Intensity transformations are fundamental tools for image enhancement. By manipulating the pixel values based on a transfer function, we can correct exposure, improve contrast, and highlight specific features. The histogram serves as a critical diagnostic tool to verify the effects of these transformations.
