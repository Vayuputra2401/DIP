# Image Enhancement Lab Report

## Objective
To understand the concept of image enhancement using spatial filtering techniques and frequency domain filtering techniques for image processing.

## Theory

### Spatial Filtering
Spatial filtering operations are performed directly on the pixels of an image. The process consists of moving a filter mask (kernel) from point to point in an image. At each point (x,y), the response is calculated using a predefined relationship.

**Linear Filters**: The response is a sum of products of the filter coefficients and the corresponding image pixels.
- **Smoothing (Lowpass) Filters**: Used for blurring and noise reduction. Output is the average of pixels in the neighborhood.
- **Sharpening (Highpass) Filters**: Enhance edges and details.

**Non-Linear Filters**: Response is based on ordering pixels (e.g., Median filter).

#### 1. Identity Filter
- **Theory**: The impulse response is a unit impulse. Convolving an image with an identity kernel leaves the image unchanged.
- **Kernel**: center=1, others=0.
- **Use Case**: Baseline comparison, system integrity check.

#### 2. Mean Filter (Averaging)
- **Theory**: Replaces each pixel with the average of its neighbors.
- **Effect**: Blurs the image, reduces random noise.
- **Drawback**: Blurs edges significantly.

#### 3. Gaussian Filter
- **Theory**: Uses a Gaussian kernel where weights decrease with distance from the center.
- **Effect**: smoother blur than mean filter, preserves edges better than mean filter.
- **Use Case**: Pre-processing for edge detection, noise reduction.

#### 4. Laplacian Filter
- **Theory**: A second-derivative operator. It is isotropic (rotation invariant).
- **Effect**: Highlights regions of rapid intensity change (edges).
- **Use Case**: Edge detection, image sharpening (when added back to original).

#### 5. Sobel Filter
- **Theory**: Uses two 3x3 kernels (Gx and Gy) to calculate approximations of the derivatives - one for horizontal changes, one for vertical.
- **Effect**: Detects edges. Combines vertical and horizontal edge information.
- **Use Case**: robust edge detection.

### Frequency Domain Filtering
Based on the Fourier Transform. The image is converted to the frequency domain, multiplied by a filter transfer function $H(u,v)$, and then converted back to the spatial domain.

$$ G(u,v) = H(u,v) \cdot F(u,v) $$

#### 1. Ideal Filters (Lowpass & Highpass)
- **Theory**: A sharp cutoff at frequency $D_0$. 
    - **Lowpass**: Passes all frequencies inside circle $D_0$.
    - **Highpass**: Blocks all frequencies inside circle $D_0$.
- **Effect**: 
    - **Lowpass**: Blurring. **Ringing effect** (Gibbs phenomenon) is very prominent.
    - **Highpass**: Sharpening. Rings are also present.

#### 2. Butterworth Filters (Lowpass & Highpass)
- **Theory**: Introduce a transition band between passband and stopband. Order $n$ controls the steepness.
- **Effect**: Reduced ringing compared to Ideal filter. Smoother transition.

#### 3. Gaussian Filters (Lowpass & Highpass)
- **Theory**: The Fourier transform of a Gaussian is also a Gaussian. No sharp cutoff.
- **Effect**: No ringing at all. 
    - **Lowpass**: Smooth blur.
    - **Highpass**: Smooth sharpening/edge extraction.

## Analysis and Comparison

| Filter Type | Enhancement Effect | Frequency Content Affected | Noise Reduction | Key/Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Spatial Mean** | Blurring | Attenuates High Frequencies | High | Blurs edges strongly. |
| **Spatial Gaussian** | Smooth Blurring | Attenuates High Frequencies | High | Better edge preservation than Mean. |
| **Spatial Laplacian**| Edge Highlighting| Enhances High Frequencies | Negative (Amplifies noise) | Very sensitive to noise. |
| **Spatial Sobel** | Edge Detection | Enhances High Frequencies | Low | Good for gradient edges. |
| **Freq Ideal Low** | Blurring | Removes High Frequencies > $D_0$| High | **Ringing artifacts** visible. |
| **Freq Butter Low** | Smooth Blurring | Attenuates High Frequencies | High | Less ringing than Ideal. |
| **Freq Gauss Low** | Smooth Blurring | Attenuates High Frequencies | High | **No ringing**. Natural blur. |
| **Freq Ideal High** | Sharpening/Edges | Removes Low Frequencies < $D_0$ | None | Ringing artifacts. Background removed. |
| **Freq Butter High**| Sharpening/Edges | Attenuates Low Frequencies | None | Less ringing coverage. |
| **Freq Gauss High** | Sharpening/Edges | Attenuates Low Frequencies | None | No ringing. Smooth edge extraction. |

## Scenarios and Applications

1.  **Noise Removal**:
    *   **Salt & Pepper Noise**: Median filter (Spatial non-linear) is best (not implemented here but worth noting).
    *   **Gaussian Noise**: Gaussian Lowpass (Spatial or Frequency) is effective.
2.  **Edge Detection**:
    *   **Sobel**: Good for finding object boundaries in machine vision.
    *   **Laplacian**: Used for finding fine details, but requires a low-noise image.
3.  **Image Sharpening**:
    *   Adding a scaled highpass result back to the original image (Unsharp masking).
4.  **Preprocessing**:
    *   **Gaussian Blur**: Commonly used before edge detection (like Canny) to reduce false positives from noise.

## Visual Examples
*Refer to the generated output images in the `filters/` directory for visual confirmation of these effects using `profile pic.jpg`.*

- `filters/output_spatial_identity.png`: No change.
- `filters/output_spatial_mean.png`: Visible blurring.
- `filters/output_freq_ideal_lowpass.png`: Blur with wave-like ringing patterns.
- `filters/output_freq_gaussian_highpass.png`: Dark image with only edges/high-contrast areas visible, no ringing.
