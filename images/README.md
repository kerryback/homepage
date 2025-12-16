# AI-Generated Images for Presentation

This folder contains placeholders for AI-generated images to enhance your presentation.

## How to Generate Images

### Using ChatGPT (DALL-E 3)
1. Go to [ChatGPT](https://chat.openai.com)
2. Use the prompts listed below for each image
3. Download the generated images
4. Save them with the exact filenames shown below

### Using Other AI Tools
- **Midjourney**: Use `/imagine` command with the prompts
- **Stable Diffusion**: Use via [DreamStudio](https://beta.dreamstudio.ai/)
- **Adobe Firefly**: Use at [Adobe Firefly](https://firefly.adobe.com/)
- **Microsoft Bing Image Creator**: Free DALL-E 3 access

## Required Images

### 1. intro-placeholder.png
**AI Prompt**: "Abstract colorful visualization of mathematical equations and physics formulas floating in space"

**Additional details**: Modern, professional, vibrant colors, suitable for academic presentation

### 2. normal-dist-placeholder.png
**AI Prompt**: "Beautiful 3D visualization of a normal distribution bell curve with flowing particles"

**Additional details**: Statistical visualization, blue and purple colors, elegant design

### 3. finance-placeholder.png
**AI Prompt**: "Modern financial trading floor with glowing stock charts and data visualizations, professional photography"

**Additional details**: Business professional, realistic or slightly stylized, greens and blues

### 4. calculus-placeholder.png
**AI Prompt**: "Abstract representation of integration and derivatives with flowing curves and mathematical beauty"

**Additional details**: Mathematical aesthetics, smooth curves, gradient colors

### 5. conclusion-placeholder.png
**AI Prompt**: "Futuristic data visualization with mathematical formulas and AI elements, inspiring and professional"

**Additional details**: Technology-forward, inspiring, professional presentation style

## Recommended Image Specifications
- **Format**: PNG (best quality) or JPG
- **Resolution**: 1920x1080 or higher (16:9 aspect ratio preferred)
- **File size**: Keep under 5MB per image for faster rendering

## After Generating Images

1. Save all images to this `images/` folder with the exact filenames listed above
2. Return to the main presentation folder
3. Run: `quarto render sample-presentation.qmd --to pptx`
4. Your PowerPoint will now include both LaTeX math AND AI-generated images!

## Tips for Better Results

- Be specific in your prompts about style (photorealistic, abstract, illustration, etc.)
- Mention colors if you have a specific palette in mind
- Add words like "professional," "high quality," "detailed" for better results
- If the first result isn't perfect, try regenerating or tweaking the prompt
- You can also use the images as placeholders and manually edit in PowerPoint later
