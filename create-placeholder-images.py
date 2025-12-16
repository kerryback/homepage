"""
Create simple placeholder images so the presentation renders without errors.
These can be replaced with AI-generated images later.

Requirements:
    pip install pillow

Usage:
    python create-placeholder-images.py
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Image specifications
IMAGES = {
    "intro-placeholder.png": "Math & Physics",
    "normal-dist-placeholder.png": "Normal Distribution",
    "finance-placeholder.png": "Financial Markets",
    "calculus-placeholder.png": "Calculus",
    "conclusion-placeholder.png": "Conclusion"
}

def create_placeholder(filename, text):
    """Create a simple placeholder image with text."""

    # Create image (16:9 aspect ratio)
    width, height = 1920, 1080

    # Create gradient background
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Draw gradient
    for y in range(height):
        r = int(70 + (185 * y / height))
        g = int(130 + (125 * y / height))
        b = int(180 + (75 * y / height))
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

    # Add text
    try:
        # Try to use a larger font
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        # Fallback to default font
        font = ImageFont.load_default()

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center text
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw text with shadow
    draw.text((x+5, y+5), text, fill=(0, 0, 0, 128), font=font)
    draw.text((x, y), text, fill=(255, 255, 255), font=font)

    # Add subtitle
    subtitle = "[Replace with AI-generated image]"
    try:
        subtitle_font = ImageFont.truetype("arial.ttf", 40)
    except:
        subtitle_font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sub_width = bbox[2] - bbox[0]
    sub_x = (width - sub_width) // 2
    sub_y = y + text_height + 30

    draw.text((sub_x, sub_y), subtitle, fill=(255, 255, 255, 200), font=subtitle_font)

    return img

def main():
    """Create all placeholder images."""

    # Create images directory if it doesn't exist
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)

    print("Creating placeholder images...")
    print("="*60)

    for filename, text in IMAGES.items():
        output_path = images_dir / filename
        print(f"Creating {filename}...")

        img = create_placeholder(filename, text)
        img.save(output_path, "PNG")

        print(f"[OK] Saved to {output_path}")

    print("="*60)
    print("Placeholder images created!")
    print("\nNext steps:")
    print("1. Generate AI images using ChatGPT, DALL-E, or Midjourney")
    print("2. Replace placeholders in images/ folder")
    print("3. Run: quarto render sample-presentation.qmd --to pptx")
    print("\nSee images/README.md for AI prompts and instructions")

if __name__ == "__main__":
    main()
