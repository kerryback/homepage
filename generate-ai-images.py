"""
Script to generate AI images for the presentation using OpenAI's DALL-E API.

Requirements:
    pip install openai pillow

Usage:
    1. Set your OpenAI API key: export OPENAI_API_KEY='your-key-here'
    2. Run: python generate-ai-images.py

The script will generate all 5 images needed for the presentation.
"""

import os
from openai import OpenAI
import requests
from pathlib import Path

# Image specifications
IMAGES = {
    "intro-placeholder.png": {
        "prompt": "Abstract colorful visualization of mathematical equations and physics formulas floating in space, modern, professional, vibrant colors, suitable for academic presentation",
        "size": "1792x1024"
    },
    "normal-dist-placeholder.png": {
        "prompt": "Beautiful 3D visualization of a normal distribution bell curve with flowing particles, statistical visualization, blue and purple colors, elegant design",
        "size": "1792x1024"
    },
    "finance-placeholder.png": {
        "prompt": "Modern financial trading floor with glowing stock charts and data visualizations, professional photography, business professional, greens and blues",
        "size": "1792x1024"
    },
    "calculus-placeholder.png": {
        "prompt": "Abstract representation of integration and derivatives with flowing curves and mathematical beauty, smooth curves, gradient colors",
        "size": "1792x1024"
    },
    "conclusion-placeholder.png": {
        "prompt": "Futuristic data visualization with mathematical formulas and AI elements, inspiring and professional, technology-forward, professional presentation style",
        "size": "1792x1024"
    }
}

def load_env_file(filepath):
    """Load environment variables from a .ENV file."""
    env_vars = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
        return env_vars
    except Exception as e:
        print(f"Error loading .ENV file: {e}")
        return {}

def generate_images():
    """Generate all images using DALL-E 3."""

    # Try to load from .ENV file first
    env_file_path = r"C:\users\kerry\dropbox\.ENV"
    env_vars = load_env_file(env_file_path)

    api_key = env_vars.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY not found")
        print(f"Checked: {env_file_path} and environment variables")
        return

    print(f"[OK] API key loaded successfully")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Create images directory if it doesn't exist
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)

    # Generate each image
    for filename, specs in IMAGES.items():
        output_path = images_dir / filename

        print(f"\nGenerating {filename}...")
        print(f"Prompt: {specs['prompt'][:80]}...")

        try:
            # Generate image using DALL-E 3
            response = client.images.generate(
                model="dall-e-3",
                prompt=specs["prompt"],
                size=specs["size"],
                quality="standard",
                n=1,
            )

            # Download the image
            image_url = response.data[0].url
            image_data = requests.get(image_url).content

            # Save to file
            with open(output_path, 'wb') as f:
                f.write(image_data)

            print(f"[OK] Saved to {output_path}")

        except Exception as e:
            print(f"[ERROR] Error generating {filename}: {e}")

    print("\n" + "="*60)
    print("Image generation complete!")
    print("Run: quarto render sample-presentation.qmd --to pptx")
    print("="*60)

if __name__ == "__main__":
    print("="*60)
    print("AI Image Generator for Quarto Presentation")
    print("="*60)
    generate_images()
