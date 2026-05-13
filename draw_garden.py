import math
import os

# --- Configuration ---
WIDTH = 800
HEIGHT = 200
OUTPUT_DIR = "dist"
OUTPUT_FILE = "garden.svg"

# Define the shapes (relative mathematical coordinates)
# A flower with 5 petals
def get_flower_path(cx, cy, size, color):
    petals = 5
    path_data = ""
    for i in range(petals * 2 + 1):
        angle = (i * math.pi * 2) / (petals * 2)
        r = size if i % 2 == 0 else size / 2
        x = cx + r * math.sin(angle)
        y = cy + r * math.cos(angle)
        command = "M" if i == 0 else "L"
        path_data += f"{command} {x:.1f},{y:.1f} "
    path_data += "Z"
    return f'<path d="{path_data}" fill="{color}" stroke="none" />\n'

# A standard heart path (Material Design path)
def get_heart_path(cx, cy, size, color):
    # Base heart path scaled to ~24x24
    base_path = "M 12 21.35 l -1.45 -1.32 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 c 1.74 0 3.41 0.81 4.5 2.09 C 13.09 3.81 14.76 3 16.5 3 c 3.08 0 5.5 2.42 5.5 5.5 c 0 3.78 -3.4 6.86 -8.55 11.54 L 12 21.35 Z"
    # Scaling and translating to requested position and size
    scale_factor = size / 24.0
    return f'<g transform="translate({cx - (12*scale_factor):.1f}, {cy - (12*scale_factor):.1f}) scale({scale_factor:.3f})">\n  <path d="{base_path}" fill="{color}" stroke="none" />\n</g>\n'

# Define the colors for the garden
FLOWERS = [
    {"x": 100, "y": 100, "size": 60, "color": "#FFC0CB"}, # LightPink
    {"x": 250, "y": 70,  "size": 40, "color": "#FF69B4"}, # HotPink
    {"x": 400, "y": 110, "size": 55, "color": "#DDA0DD"}, # Plum
    {"x": 550, "y": 60,  "size": 35, "color": "#DB7093"}, # PaleVioletRed
    {"x": 700, "y": 100, "size": 60, "color": "#FFF0F5"}, # LavenderBlush
]

HEARTS = [
    {"x": 60,  "y": 40,  "size": 30, "color": "#DC143C"}, # Crimson
    {"x": 190, "y": 140, "size": 25, "color": "#FF1493"}, # DeepPink
    {"x": 340, "y": 30,  "size": 35, "color": "#C71585"}, # MediumVioletRed
    {"x": 480, "y": 150, "size": 20, "color": "#FFB6C1"}, # LightPink
    {"x": 620, "y": 130, "size": 30, "color": "#DB7093"}, # PaleVioletRed
    {"x": 750, "y": 40,  "size": 25, "color": "#FF69B4"}, # HotPink
]

# --- Main SVG generation ---
def generate_garden_svg():
    print(f"Drawing the code garden to {OUTPUT_FILE}...")
    
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    
    # SVG Header
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">\n'
    svg_content += '\n'
    # Add a subtle background color if you want, or keep it transparent
    # svg_content += f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#FFF8F8" />\n'

    # Add Hearts (code-calculated paths)
    for heart in HEARTS:
        svg_content += get_heart_path(heart["x"], heart["y"], heart["size"], heart["color"])

    # Add Flowers (code-calculated paths)
    for flower in FLOWERS:
        # Draw the main flower petals
        svg_content += get_flower_path(flower["x"], flower["y"], flower["size"], flower["color"])
        # Draw the center of the flower (a simple circle)
        center_color = "#FFD700" # Gold
        center_size = flower["size"] / 4
        svg_content += f'<circle cx="{flower["x"]:.1f}" cy="{flower["y"]:.1f}" r="{center_size:.1f}" fill="{center_color}" />\n'

    # SVG Footer
    svg_content += "</svg>"

    # Write the file
    with open(output_path, "w") as f:
        f.write(svg_content)
    print("Garden successfully drawn!")

if __name__ == "__main__":
    generate_garden_svg()
