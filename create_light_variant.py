#!/usr/bin/env python3
"""
Create an improved light fabric variant
"""

from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageChops
import numpy as np

print("🎨 Creating improved light fabric variant...")

# Load the transparent logo
img = Image.open("assets/logo-transparent.png").convert("RGBA")

# Strategy: Create a version with thick white stroke/outline that will show on light backgrounds
# We'll make the outline much more prominent

# Extract alpha
alpha = img.split()[3]

# Create multiple dilations for a thick outline
outline_layers = []
for width in [8, 16, 24, 32, 40]:  # Multiple outline widths
    dilated = alpha.copy()
    for _ in range(width):
        dilated = dilated.filter(ImageFilter.MaxFilter(3))
    outline_layers.append(dilated)

# Combine all outline layers
thick_outline = outline_layers[-1]  # Start with thickest

# Create white outline layer
white_outline = Image.new("RGBA", img.size, (255, 255, 255, 0))
white_outline.putalpha(thick_outline)

# Composite: thick white outline behind original
result = Image.alpha_composite(white_outline, img)

# Save
result.save("assets/logo-print-light.png", "PNG", dpi=(300, 300))
print("✓ Enhanced light version saved with thick white outline")

# Also create a bonus "inverted" version where dark areas become white
print("\n🎨 Creating bonus inverted variant for ultimate visibility on dark backgrounds...")

# Load original again
img2 = Image.open("assets/logo-transparent.png").convert("RGBA")

# Split channels
r, g, b, a = img2.split()

# For pixels that are dark (the interior), make them white
# Convert to numpy for easier manipulation
r_arr = np.array(r)
g_arr = np.array(g)
b_arr = np.array(b)
a_arr = np.array(a)

# Calculate brightness
brightness = (r_arr * 0.299 + g_arr * 0.587 + b_arr * 0.114)

# Where brightness is low (dark areas) and alpha is high (opaque logo parts)
dark_mask = (brightness < 100) & (a_arr > 128)

# Replace dark areas with white
r_arr[dark_mask] = 255
g_arr[dark_mask] = 255
b_arr[dark_mask] = 255

# Reconstruct image
inverted = Image.merge("RGBA", [
    Image.fromarray(r_arr),
    Image.fromarray(g_arr),
    Image.fromarray(b_arr),
    Image.fromarray(a_arr)
])

inverted.save("assets/logo-print-inverted.png", "PNG", dpi=(300, 300))
print("✓ Inverted version saved (dark areas replaced with white)")

print("\n✅ Enhanced variants created!")
print("  • logo-print-light.png - Thick white outline for light fabrics")
print("  • logo-print-inverted.png - Dark areas replaced with white (bonus)")
