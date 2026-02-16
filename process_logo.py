#!/usr/bin/env python3
"""
TechQuest Logo Processor
Removes background, upscales, and creates print-ready variants
"""

from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance
from rembg import remove
import io
import sys

# Paths
SOURCE = "logo.jpg"
ASSETS = "assets"
TRANSPARENT = f"{ASSETS}/logo-transparent.png"
DARK_FABRIC = f"{ASSETS}/logo-print-dark.png"
LIGHT_FABRIC = f"{ASSETS}/logo-print-light.png"

# Target specs
TARGET_SIZE = 3000
TARGET_DPI = 300

print("🎨 TechQuest Logo Processor")
print("=" * 50)

# Step 1: Load and remove background
print("\n1️⃣ Removing background with AI...")
with open(SOURCE, 'rb') as input_file:
    input_data = input_file.read()
    output_data = remove(input_data)

# Convert to PIL Image
img = Image.open(io.BytesIO(output_data)).convert("RGBA")
print(f"   ✓ Background removed (size: {img.size})")

# Step 2: Upscale to 3000x3000 using high-quality resampling
print(f"\n2️⃣ Upscaling to {TARGET_SIZE}x{TARGET_SIZE}px...")
img_upscaled = img.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
print(f"   ✓ Upscaled with LANCZOS resampling")

# Step 3: Save transparent version
print(f"\n3️⃣ Saving transparent version...")
img_upscaled.save(TRANSPARENT, "PNG", dpi=(TARGET_DPI, TARGET_DPI))
print(f"   ✓ Saved: {TRANSPARENT}")

# Step 4: Create dark fabric version (original colors, transparent bg, 300 DPI)
print(f"\n4️⃣ Creating dark fabric version...")
img_upscaled.save(DARK_FABRIC, "PNG", dpi=(TARGET_DPI, TARGET_DPI))
print(f"   ✓ Saved: {DARK_FABRIC}")

# Step 5: Create light fabric version with white outline
print(f"\n5️⃣ Creating light fabric version with white outline...")

# Create a copy for the light version
img_light = img_upscaled.copy()

# Extract alpha channel
alpha = img_light.split()[3]

# Create white outline by dilating the alpha channel
outline_width = 15  # pixels for 3000x3000 image
outline = alpha.filter(ImageFilter.MaxFilter(outline_width))

# Create white base layer
white_layer = Image.new("RGBA", (TARGET_SIZE, TARGET_SIZE), (255, 255, 255, 0))
white_draw = ImageDraw.Draw(white_layer)

# Apply white color to outline
white_layer.putalpha(outline)

# Composite: white outline behind original logo
result = Image.alpha_composite(white_layer, img_light)

# Optionally brighten the logo colors for visibility on light backgrounds
# We'll make the logo slightly lighter/more saturated
enhancer = ImageEnhance.Brightness(result)
result = enhancer.enhance(1.1)  # 10% brighter

result.save(LIGHT_FABRIC, "PNG", dpi=(TARGET_DPI, TARGET_DPI))
print(f"   ✓ Saved: {LIGHT_FABRIC}")

print("\n" + "=" * 50)
print("✅ All variants created successfully!")
print(f"\nOutput files:")
print(f"  • {TRANSPARENT} - Transparent background, full size")
print(f"  • {DARK_FABRIC} - For dark fabrics (300 DPI, {TARGET_SIZE}x{TARGET_SIZE})")
print(f"  • {LIGHT_FABRIC} - For light fabrics with white outline (300 DPI, {TARGET_SIZE}x{TARGET_SIZE})")
