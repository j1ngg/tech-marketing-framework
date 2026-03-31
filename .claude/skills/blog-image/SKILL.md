---
name: blog-image
description: Generates blog featured images using Google's Nano Banana 2 model. Reads brand guidelines and blog content to create on-brand visuals. Outputs PNG at 1200x627 with alt text.
autoload: false
---

# Blog Featured Image Generator

This skill generates featured images for blog posts using Google's Nano Banana 2 (Gemini 3.1 Flash Image) model. It reads your brand guidelines and blog content to create visually relevant, on-brand images.

## Prerequisites

**Required:** Google Gemini API key with image generation access.

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Required Python packages:**
```bash
pip install google-genai pillow
```

---

## Step 1: Check Brand Guidelines

Before generating any images, check if `docs/inputs/brand_guidelines.md` exists.

**If it exists:** Read it and extract visual style preferences.

**If it does not exist:** Guide the user to create one.

Say:

> "I don't see brand guidelines at `docs/inputs/brand_guidelines.md`. Consistent featured images require defined visual standards."
>
> "Would you like me to help you create brand guidelines now? I'll ask a few questions about your visual style."

If user wants to create guidelines, walk through:

1. **Visual style** — What aesthetic describes your brand? (e.g., minimalist tech, abstract data visualization, bold geometric, editorial illustration)
2. **Color palette** — What are your primary and secondary brand colors? (hex codes preferred)
3. **Mood** — What feeling should images evoke? (e.g., professional, innovative, approachable, bold)
4. **Elements to include** — What visual motifs represent your brand? (e.g., circuit patterns, flowing data, geometric shapes)
5. **Elements to avoid** — What should never appear? (e.g., stock photo aesthetic, cartoonish style, busy backgrounds)

Save the answers to `docs/inputs/brand_guidelines.md` using this template:

```markdown
# Brand Visual Guidelines

## Visual Style
[User's answer]

## Color Palette
- Primary: [hex code]
- Secondary: [hex code]
- Accent: [hex code]

## Mood
[User's answer]

## Visual Motifs
- [Element 1]
- [Element 2]
- [Element 3]

## Restrictions
- [Avoid 1]
- [Avoid 2]
- No text in images
- No photorealistic human faces
- No competitor logos or products
```

Wait for brand guidelines to exist before proceeding to image generation.

---

## Step 2: Gather Inputs

**Read automatically:**
- `docs/inputs/brand_guidelines.md` — Visual style, colors, mood, motifs

**Ask the user:**

1. **Blog content** — Provide the blog to create an image for:
   - File path (e.g., `output/blog/feature-announcement.md`)
   - URL to fetch
   - Or paste the blog title and TLDR

2. **Reference image** — (Optional) Do you have a reference image for style matching?
   - If yes, provide the file path
   - If no, we'll use text prompts only (default)

Wait for answers before proceeding.

---

## Step 3: API Key Setup

**SECURITY CRITICAL:** The API key must be handled securely.

Say:

> "I need your Gemini API key to generate images."
>
> "**Do NOT paste your API key in this chat.** Instead, set it as an environment variable:"
>
> ```bash
> export GEMINI_API_KEY="your-key-here"
> ```
>
> "Once set, type 'ready' and I'll proceed."

**Security rules (enforced by skill):**
- Never accept API key as chat input
- Never log, echo, or display the API key
- Never write the API key to any file
- Access only via `os.environ.get("GEMINI_API_KEY")`
- If key is not set, provide setup instructions and wait

Verify the key is set:

```python
import os
if not os.environ.get("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY environment variable not set")
```

---

## Step 4: Generate Image

### Construct the Prompt

Build the image generation prompt using this structure:

```
[Brand style descriptors from guidelines]

[Visual concept derived from blog content]

Blog featured image, horizontal composition, 1200x627 pixels.

No text, no words, no letters, no typography.
No photorealistic human faces.
Clean composition with clear focal point.
```

**Prompt construction rules:**

| Section | Source | Example |
|---------|--------|---------|
| Style | Brand guidelines | "Minimalist tech illustration style, cool blue and white color palette, professional and innovative mood" |
| Concept | Blog content | "Abstract visualization of cryptographic key binding between a device and an identity" |
| Format | Fixed | "Blog featured image, horizontal composition, 1200x627 pixels" |
| Restrictions | Fixed + guidelines | "No text, no words, no photorealistic faces, no busy backgrounds" |

### Execute Generation

Run the following Python script:

```python
#!/usr/bin/env python3
"""
Blog Featured Image Generator
Uses Nano Banana 2 (Gemini 3.1 Flash Image) for generation.
"""

import os
import sys
import time
import base64
from pathlib import Path

# Security: Only access key from environment
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("ERROR: GEMINI_API_KEY environment variable not set")
    sys.exit(1)

try:
    from google import genai
    from google.genai import types
    from PIL import Image
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Run: pip install google-genai pillow")
    sys.exit(1)

def generate_image(prompt: str, output_path: str, max_retries: int = 3):
    """
    Generate an image using Nano Banana 2.

    Args:
        prompt: The image generation prompt
        output_path: Where to save the PNG
        max_retries: Number of retry attempts on failure
    """
    client = genai.Client(api_key=API_KEY)

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                )
            )

            # Extract and save the image
            for part in response.parts:
                if part.inline_data:
                    image = part.as_image()

                    # Resize to exact dimensions
                    image = image.resize((1200, 627), Image.LANCZOS)

                    # Ensure output directory exists
                    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

                    # Save as PNG
                    image.save(output_path, "PNG")
                    print(f"Image saved to: {output_path}")
                    return True

            print("ERROR: No image in response")
            return False

        except Exception as e:
            wait_time = 2 ** attempt  # Exponential backoff: 1, 2, 4 seconds
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("ERROR: All retry attempts failed")
                return False

    return False


def generate_with_reference(prompt: str, reference_path: str, output_path: str, max_retries: int = 3):
    """
    Generate an image using a reference image for style matching.

    Args:
        prompt: The image generation prompt
        reference_path: Path to reference image
        output_path: Where to save the PNG
        max_retries: Number of retry attempts on failure
    """
    client = genai.Client(api_key=API_KEY)

    # Load reference image
    ref_image = Image.open(reference_path)

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[
                    ref_image,
                    f"Using the style and aesthetic of this reference image, create: {prompt}"
                ],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                )
            )

            for part in response.parts:
                if part.inline_data:
                    image = part.as_image()
                    image = image.resize((1200, 627), Image.LANCZOS)
                    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                    image.save(output_path, "PNG")
                    print(f"Image saved to: {output_path}")
                    return True

            print("ERROR: No image in response")
            return False

        except Exception as e:
            wait_time = 2 ** attempt
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("ERROR: All retry attempts failed")
                return False

    return False


if __name__ == "__main__":
    # Example usage (values replaced by skill at runtime)
    PROMPT = """{{PROMPT}}"""
    OUTPUT_PATH = "{{OUTPUT_PATH}}"
    REFERENCE_PATH = "{{REFERENCE_PATH}}"  # Empty string if no reference

    if REFERENCE_PATH:
        success = generate_with_reference(PROMPT, REFERENCE_PATH, OUTPUT_PATH)
    else:
        success = generate_image(PROMPT, OUTPUT_PATH)

    sys.exit(0 if success else 1)
```

**Execution:**
1. Replace `{{PROMPT}}`, `{{OUTPUT_PATH}}`, and `{{REFERENCE_PATH}}` with actual values
2. Save script to a temporary file
3. Execute with Python
4. Delete temporary script after execution

---

## Step 5: Review and Refine

After generating the image, present it to the user:

> "Here's the generated featured image:"
>
> **Saved to:** `output/images/[blog-slug]-featured.png`
>
> **Prompt used:**
> ```
> [The full prompt]
> ```
>
> **Alt text:** [Generated alt text describing the image]
>
> "Are you happy with this image, or would you like to refine it?"

### Refinement Loop

If the user wants changes, ask:

> "What would you change about this image?"

Take their feedback and adjust the prompt. Common refinements:

| Feedback | Prompt Adjustment |
|----------|-------------------|
| "Too busy" | Add "minimal elements, clean negative space, simple composition" |
| "Too dark" | Add "bright, well-lit, light color palette" |
| "Not technical enough" | Add more technical motifs from brand guidelines |
| "Wrong colors" | Explicitly specify hex codes in prompt |
| "Too abstract" | Add "clear recognizable shapes, concrete visual metaphor" |

**Maximum 5 refinement rounds.** After 5 attempts, say:

> "We've done 5 refinement rounds. If the results still aren't right, I recommend:"
>
> 1. Updating your brand guidelines with more specific visual direction
> 2. Providing a reference image that captures your desired style
> 3. Trying a different visual concept for this blog

---

## Step 6: Generate Alt Text

After the image is approved, generate SEO-friendly alt text:

**Alt text rules:**
- Describe what is visually in the image, not the blog topic
- 125 characters or fewer
- No "image of" or "picture of" prefix
- Include key visual elements and colors

**Example:**
```
Blog: "Eliminating Phishable MFA with Cryptographic Device Binding"
Image: Abstract illustration of a shield connected to a laptop by glowing blue lines
Alt text: "Abstract blue shield connected to laptop by glowing lines on dark background"
```

---

## Output Format

After successful generation, output:

```markdown
## Generated Featured Image

**File:** `output/images/[blog-slug]-featured.png`
**Dimensions:** 1200x627px
**Format:** PNG

**Alt text:** [Description for SEO]

**Prompt used:**
```
[Full prompt for reference/iteration]
```

**Note:** This image contains an invisible SynthID watermark identifying it as AI-generated.
```

---

## Error Handling

### API Key Not Set

```
ERROR: GEMINI_API_KEY environment variable not set.

To set your API key:

1. Get a key from https://aistudio.google.com/apikey
2. Run: export GEMINI_API_KEY="your-key-here"
3. Try again
```

### API Rate Limit

```
ERROR: Rate limit exceeded. Waiting before retry...

If this persists, you may have hit your daily quota.
Check your usage at https://aistudio.google.com/
```

### Generation Failed After Retries

```
ERROR: Image generation failed after 3 attempts.

Possible causes:
- API service disruption (check status.cloud.google.com)
- Prompt triggered content filter (try simpler description)
- Network connectivity issue

Fallback options:
1. Try again in a few minutes
2. Use a simpler prompt
3. Create the image manually using the prompt as guidance
```

### Missing Dependencies

```
ERROR: Required packages not installed.

Run:
pip install google-genai pillow

Then try again.
```

---

## Review Checklist

Before delivering the image, verify:

### Technical
- [ ] Image saved to `output/images/` directory
- [ ] Dimensions are exactly 1200x627px
- [ ] Format is PNG
- [ ] File name matches blog slug

### Quality
- [ ] Image visually relates to blog content
- [ ] Style matches brand guidelines
- [ ] No text or typography in image
- [ ] No photorealistic human faces
- [ ] Clean composition with clear focal point

### Deliverables
- [ ] Alt text generated (under 125 chars)
- [ ] Prompt documented for future reference
- [ ] SynthID watermark disclosure included

### Security
- [ ] API key was never displayed in output
- [ ] API key was never written to any file
- [ ] Temporary script deleted after execution

---

## Adaptation Notes

**When brand guidelines are sparse:**
- Use sensible defaults: clean, professional, tech-focused
- Suggest the user add more detail for better results

**When blog content is very technical:**
- Focus on abstract representations of concepts
- Avoid trying to literally illustrate complex technical processes

**When generation consistently fails content filters:**
- Simplify the concept
- Remove any potentially sensitive terms
- Focus on abstract shapes and colors

**When user wants text in the image:**
- Explain that AI-generated text often renders poorly
- Suggest adding text overlay in post-production (Figma, Canva)
- Offer to leave space in composition for text overlay

**When user provides reference image:**
- Use the reference for style only, not content
- Explain that the generated image will capture the aesthetic, not copy the reference
