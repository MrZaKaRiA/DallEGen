# DallEGen
Generate pictures using open AI DALL-E API

# Image Generator

This Python script, `image_generator.py`, generates images using OpenAI's DALL-E 3 model via a terminal interface. Users can input text prompts to create images, customize image sizes, and save the results locally.

## Features

- Generate high-quality images from text prompts using OpenAI's DALL-E 3 model.
- Interactive terminal interface for entering prompts and commands.
- Supported image sizes: `1024x1024`, `1024x1792`, `1792x1024`.
- Save images to a `generated_images` directory with timestamped filenames.
- Secure API key management using environment variables.

## Prerequisites

- **Python 3.7+** installed.
- An **OpenAI API key** from [OpenAI](https://platform.openai.com/).
- Required Python packages:
  - `openai`
  - `python-dotenv`

## Installation

1. **Clone or download the script**:
   - Clone the repository (if hosted):
     ```bash
     git clone 
     cd 
     ```
   - Or download `image_generator.py` directly.

2. **Install dependencies**:
   ```bash
   pip install openai python-dotenv
	3	Set up your OpenAI API key:
	◦	Create a .env file in the same directory as image_generator.py.
	◦	Add your API key: OPENAI_API_KEY=your-api-key-here
	◦	
	◦	Ensure .env is not shared publicly (e.g., add to .gitignore).
Usage
	1	Run the script: python image_generator.py
	2	
	3	Interact with the terminal interface:
	◦	The script displays: Simple Image Generation
	◦	Type 'quit' or 'exit' to end the program.
	◦	Enter '/size ' to change image size (1024x1024, 1024x1792, 1792x1024).
	◦	Enter '/count ' to set number of images to generate (1).
	◦	--------------------------------------------------
	◦	
	◦	Enter a prompt: Type an image description (e.g., A futuristic city at sunset).
	◦	Change image size: Use /size (e.g., /size 1024x1792).
	◦	Set image count: Use /count 1 (DALL-E 3 supports only one image).
	◦	Exit: Type quit or exit.
	4	Output:
	◦	Images are saved in the generated_images directory with names like image_YYYYMMDD_HHMMSS_N.png (e.g., image_20250506_123456_1.png).
	◦	File paths are printed: Generated 1 image(s) successfully!
	◦	Images saved at:
	◦	- generated_images/image_20250506_123456_1.png
	◦	
Notes
	•	DALL-E 3 Limitations: Only one image per request (n=1) and specific sizes are supported.
	•	API Costs: Image generation incurs costs. Check OpenAI’s pricing.
	•	Error Handling: Handles invalid prompts and missing API keys. Ensure a valid API key and internet connection.
	•	Security: Keep .env secure and exclude from version control.
Troubleshooting
	•	“OPENAI_API_KEY not set”: Verify .env exists with a valid key.
	•	“Invalid size”: Use 1024x1024, 1024x1792, or 1792x1024.
	•	API errors: Check OpenAI account for rate limits or billing issues.
License
MIT License (or specify your license).
Contact
Open an issue on the repository or contact the maintainer for questions.
### How to Use the README

1. Save the content above as `README.md` in the same directory as `image_generator.py`.
2. If hosting on GitHub, replace `` with your repository's URL.
3. Customize the "License" and "Contact" sections as needed (e.g., specify your license or contact details).
4. Ensure the `.env` file is listed in `.gitignore` to prevent accidental sharing.

