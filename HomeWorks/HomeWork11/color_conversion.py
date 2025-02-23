import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image

#  ------- Conversion Functions  ------- 
def rgb_to_cmyk(r, g, b):
    k = 1 - max(r, g, b)
    if k == 1:
        return (0, 0, 0, 1)  # Pure black case
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return (c, m, y, k)

# Function to convert CMYK to Pillow format (0-255 scale)
def cmyk_to_pillow(c, m, y, k):
    return (int(c * 255), int(m * 255), int(y * 255), int(k * 255))

#  ------- Define vectors sets  ------- 
RGB_basis = np.array([
    [0.3,0.2, 0],  # color 1
    [1, 1, 0],  # color 2
    [1, 1, 0]   # color 3
])

#  ------- Display Vectors in CMYK  -------
CMYK_basis = np.array([rgb_to_cmyk(*color) for color in RGB_basis])
print("CMYK vectors:")
print(CMYK_basis)

CMYK_colors_pillow = [cmyk_to_pillow(*color) for color in CMYK_basis]

# ------- Plot of colors ------- 
img_cmyk = Image.new("CMYK", (300, 100))  # 3 colors, each 100 pixels wide
for i, color in enumerate(CMYK_colors_pillow):
    img_cmyk.paste(Image.new("CMYK", (100, 100), color), (i * 100, 0))
img_cmyk.save("cmyk_colors.jpg", "JPEG")


fig, ax = plt.subplots(figsize=(6, 2))
ax.set_title("RGB Color Space")

for i, color in enumerate(RGB_basis):
    ax.add_patch(Rectangle((i, 0), 1, 1, color=color))

# Adjust layout
ax.set_xlim(0, 3)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.savefig("rgb_colors.jpg", dpi=300)


def cmyk_to_rgb(c, m, y, k):
    r = 1 - min(1, c * (1 - k) + k)
    g = 1 - min(1, m * (1 - k) + k)
    b = 1 - min(1, y * (1 - k) + k)
    return (r, g, b)

# Define a CMYK color that is difficult to represent in RGB
cmyk_color = (0.3, 0.26, 0.15, 0.11)  # Pure cyan and magenta

# Convert the CMYK color to RGB
rgb_color = cmyk_to_rgb(*cmyk_color)

# Print the RGB values
print("CMYK color:", cmyk_color)
print("Converted RGB color:", rgb_color)

# Check if the RGB values are within the valid range (0-1)
if any(value < 0 or value > 1 for value in rgb_color):
    print("The RGB color space cannot represent this CMYK color.")
else:
    print("The RGB color space can represent this CMYK color.")


    plt.savefig("cmyk_to_rgb.jpg", dpi=300)