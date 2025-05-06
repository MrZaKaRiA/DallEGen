import os
import sys
import base64
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

def generate_image(client, prompt, size="1024x1024", model="dall-e-3", num_images=1):
    """Generate images using OpenAI's DALL-E model."""
    try:
        print(f"Generating image with prompt: '{prompt}' ...")
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality="standard",  # 'standard' or 'hd' for DALL-E 3
            n=num_images
        )
        # Return the base64 data of images
        return [img.b64_json for img in response.data if img.b64_json]
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def save_base64_images(image_data_list, output_dir="generated_images"):
    """Save base64 encoded images to the local filesystem."""
    saved_files = []
    try:
        # Create output directory if it doesn't exist
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Create a base filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_base_filename = f"image_{timestamp}"

        # Loop through image data and save each
        for i, image_base64 in enumerate(image_data_list):
            # Decode base64 data
            image_bytes = base64.b64decode(image_base64)
            # Create filename with index
            final_filename = f"{safe_base_filename}_{i+1}.png"
            file_path = output_path / final_filename
            # Save to file
            with open(file_path, "wb") as f:
                f.write(image_bytes)
            saved_files.append(str(file_path))
        return saved_files
    except Exception as e:
        print(f"Error saving images: {e}")
        return []

def main():
    """Runs a simple terminal interface for image generation."""
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set the variable in a .env file and try again.")
        print("Example: OPENAI_API_KEY=your-api-key-here")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    print("Simple Image Generation")
    print("Type 'quit' or 'exit' to end the program.")
    print("Enter '/size <size>' to change image size (1024x1024, 1024x1792, 1792x1024).")
    print("Enter '/count <number>' to set number of images to generate (1).")
    print("-" * 50)

    size = "1024x1024"  # Default size
    num_images = 1  # Default number of images (DALL-E 3 supports 1 image)

    while True:
        try:
            user_input = input("Enter image prompt: ")

            # Handle exit commands
            if user_input.lower() in ["quit", "exit"]:
                print("Exiting program.")
                break

            # Handle size change command
            if user_input.startswith("/size "):
                new_size = user_input[6:].strip()
                if new_size in ["1024x1024", "1024x1792", "1792x1024"]:
                    size = new_size
                    print(f"Image size set to: {size}")
                else:
                    print("Invalid size. Use 1024x1024, 1024x1792, or 1792x1024.")
                continue

            # Handle count change command
            if user_input.startswith("/count "):
                try:
                    count = int(user_input[7:].strip())
                    if count == 1:  # DALL-E 3 supports only 1 image
                        num_images = count
                        print(f"Number of images to generate: {num_images}")
                    else:
                        print("Invalid count. DALL-E 3 supports only 1 image.")
                except ValueError:
                    print("Invalid count. Please enter a number.")
                continue

            # Skip empty prompts
            if not user_input.strip():
                continue

            # Generate the images
            image_data_list = generate_image(client, user_input, size=size, num_images=num_images)
            if image_data_list and len(image_data_list) > 0:
                print(f"Generated {len(image_data_list)} image(s) successfully!")
                # Save the images
                saved_paths = save_base64_images(image_data_list)
                if saved_paths:
                    print("Images saved at:")
                    for path in saved_paths:
                        print(f"- {path}")
                else:
                    print("Failed to save the images.")
            else:
                print("Failed to generate images. Please try again with a different prompt.")

        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
