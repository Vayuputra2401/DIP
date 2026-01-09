# Histogram & Contrast Stretching Lab Report

## Objective
The objective is to analyze image histograms, understand their relationship to contrast and brightness, and implement contrast stretching and histogram equalization techniques to enhance images.

## Theory & Implementation

### 1. Histogram Analysis
The histogram $P(r_k) = n_k / n$ represents the frequency distribution of pixel intensities.
- **Dark Image**: Histogram concentrated on the left (low values).
- **Bright Image**: Histogram concentrated on the right (high values).
- **Low Contrast**: Histogram concentrated in a narrow range (middle or elsewhere).
- **High Contrast**: Histogram covers the full dynamic range [0, 255].

### 2. Contrast Stretching
Contrast stretching (linear) expands the range of intensity levels effectively used by an image.
**Formula**:  
$$ s = \frac{r - r_{min}}{r_{max} - r_{min}} \times (L-1) $$
- **Goal**: Map the minimum intensity ($r_{min}$) to 0 and the maximum ($r_{max}$) to 255.
- **Effect**: Increases the dynamic range, making details more visible, especially in washed-out (low contrast) images.

### 3. Histogram Equalization
A more sophisticated method that flattens the histogram.
**Algorithm**:
1.  Compute the histogram $H(r)$.
2.  Compute the Cumulative Distribution Function (CDF): $CDF(r_k) = \sum_{j=0}^{k} P(r_j)$.
3.  Map new values: $s_k = floor((L-1) \times CDF(r_k))$.
- **Effect**: Spreads out the most frequent intensity values. This maximizes the global contrast of the image. The resulting histogram is roughly uniform (flat).

## Analysis and Comparison

| Technique | Method | Visual Effect | Histogram Effect |
| :--- | :--- | :--- | :--- |
| **Original (Low Contrast)** | N/A | Washed out, grey. | Narrow peak in the middle. |
| **Contrast Stretching** | Linear scaling | Better contrast, clear details. | Widens the peak to cover [0, 255]. Relative shape preserved. |
| **Histogram Equalization**| Non-linear mapping | Maximum contrast. Can look "harsh" or unnatural. | Flattens the distribution. Shape changes significantly. |

### Insights
- **Stretching** is best when the histogram is just "squashed" but has a good shape. It linearly rescales values.
- **Equalization** is powerful for images with bad lighting or very poor global contrast. However, valid flat areas (like a distinct background) might get noisy because equalization tries to force them to spread out.

## Visual Examples
*Refer to the following generated images in the `histogram_assignment/` directory:*

- **Variants Analysis**: `histogram_assignment/histogram_variants_output.png` (Shows Dark, Bright, Low Contrast histograms).
- **Contrast Stretching**: `histogram_assignment/contrast_stretching_output.png` (Demonstrates restoring a low-contrast image).
- **Equalization**: `histogram_assignment/histogram_equalization_output.png` (Shows the flattening of the histogram and the resulting highly contrasted image).

## Conclusion
Histograms provide a "fingerprint" of an image's exposure. Contrast stretching helps utilize the full bit-depth of the image, while histogram equalization completely remodels the intensity distribution to maximize information visibility. Both are essential pre-processing steps for computer vision tasks.
