from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

def create_logo():
    # Create a new image with a white background
    width = 500
    height = 500
    background_color = (255, 255, 255)
    logo = Image.new('RGBA', (width, height), background_color)
    
    # Create a drawing object
    draw = ImageDraw.Draw(logo)
    
    # Draw a circle
    circle_color = (76, 175, 80)  # Green color (#4CAF50)
    draw.ellipse([100, 100, 400, 400], fill=circle_color)
    
    # Draw atom-like circles
    draw.ellipse([150, 150, 350, 350], outline='white', width=5)
    draw.ellipse([200, 200, 300, 300], outline='white', width=5)
    
    # Save the logo
    assets_dir = Path(__file__).parent.parent / "frontend" / "assets"
    assets_dir.mkdir(exist_ok=True)
    logo.save(assets_dir / "logo.png")

if __name__ == "__main__":
    create_logo()