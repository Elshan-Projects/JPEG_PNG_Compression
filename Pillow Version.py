from PIL import Image, ImageOps
import os

def compress_image(input_path, output_path, file_format):
    """Compress an image using Pillow and save it to the output path."""
    print(f"Processing {os.path.basename(input_path)}...")  # Print the name of the image being processed
    try:
        with Image.open(input_path) as img:
            if file_format == 'JPEG':
                # Compress JPEG by adjusting quality
                img.save(output_path, 'JPEG', quality=35, optimize=True)
            elif file_format == 'PNG':
                # Attempt to reduce the image size by converting it to P mode (palette-based)
                img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
                img.save(output_path, 'PNG', optimize=True)
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def compress_images(directory):
    target_folder = os.path.join(directory, "Compressed Images - Pillow")
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            original_path = os.path.join(directory, filename)
            file_format = 'PNG' if filename.lower().endswith('.png') else 'JPEG'
            compressed_path = os.path.join(target_folder, filename)

            compress_image(original_path, compressed_path, file_format)
            print(f"Compressed and saved: {compressed_path}")

# Example usage
directory = "path/to/your/folder"  # Change this to the path of your folder
compress_images(directory)
