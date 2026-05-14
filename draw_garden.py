import math
import os

# --- Configuration ---
WIDTH = 800
HEIGHT = 200
OUTPUT_DIR = "dist"
OUTPUT_FILE = "garden.svg"

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
    
    # We wrap the flower in a group <g> and apply the "flower" animation class
    # The transform-origin ensures it rotates from its own center
    return f'<g class="flower" style="transform-origin: {cx:.1f}px {cy:.1f}px;">\n  <path d="{path_data}" fill="{color}" stroke="none" />\n  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size/4:.1f}" fill="#FFD700" />\n</g>\n'

# A standard heart path
def get_heart_path(cx, cy, size, color):
    base_path = "M 12 21.35 l -1.45 -1.32 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 c 1.74 0 3.41 0.81 4.5 2.09 C 13.09 3.81 14.76 3 16.5 3 c 3.08 0 5.5 2.42 5.5 5.5 c 0 3.78 -3.4 6.86 -8.55 11.54 L 12 21.35 Z"
    scale_factor = size / 24.0
    
    # The inner path gets the "heart" animation class. 
    # Transform-origin 12px 12px centers the heartbeat on the base path.
    return f'<g transform="translate({cx - (12*scale_factor):.1f}, {cy - (12*scale_factor):.1f}) scale({scale_factor:.3f})">\n  <path class="heart" style="transform-origin: 12px 12px;" d="{base_path}" fill="{color}" stroke="none" />\n</g>\n'

FLOWERS = [
    {"x": 100, "y": 100, "size": 60, "color": "#FFC0CB"}, 
    {"x": 250, "y": 70,  "size": 40, "color": "#FF69B4"}, 
    {"x": 400, "y": 110, "size": 55, "color": "#DDA0DD"}, 
    {"x": 550, "y": 60,  "size": 35, "color": "#DB7093"}, 
    {"x": 700, "y": 100, "size": 60, "color": "#FFF0F5"}, 
]

HEARTS = [
    {"x": 60,  "y": 40,  "size": 30, "color": "#DC143C"}, 
    {"x": 190, "y": 140, "size": 25, "color": "#FF1493"}, 
    {"x": 340, "y": 30,  "size": 35, "color": "#C71585"}, 
    {"x": 480, "y": 150, "size": 20, "color": "#FFB6C1"}, 
    {"x": 620, "y": 130, "size": 30, "color": "#DB7093"}, 
    {"x": 750, "y": 40,  "size": 25, "color": "#FF69B4"}, 
]

def generate_garden_svg():
    print(f"Drawing the animated code garden to {OUTPUT_FILE}...")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">\n'
    
    # --- HERE ARE THE CSS ANIMATIONS ---
    svg_content += """
    <style>
        .heart { animation: pulse 1.5s infinite ease-in-out; }
        .flower { animation: sway 4s infinite alternate ease-in-out; }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); }
        }
        @keyframes sway {
            0% { transform: rotate(-8deg); }
            100% { transform: rotate(8deg); }
        }
    </style>
    """

    for heart in HEARTS:
        svg_content += get_heart_path(heart["x"], heart["y"], heart["size"], heart["color"])

    for flower in FLOWERS:
        svg_content += get_flower_path(flower["x"], flower["y"], flower["size"], flower["color"])

    svg_content += "</svg>"

    with open(output_path, "w") as f:
        f.write(svg_content)
    print("Animated garden successfully drawn!")

if __name__ == "__main__":
    generate_garden_svg()
