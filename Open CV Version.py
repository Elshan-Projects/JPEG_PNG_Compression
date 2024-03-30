import os
import cv2

def compress_image(input_path, output_path, file_format):
    """Compress an image using OpenCV and save it to the output path."""
    print(f"Processing {os.path.basename(input_path)}...")  # Print the name of the image being processed
    try:
        # Read the image using OpenCV
        img = cv2.imread(input_path)
        
        # Set compression parameters
        if file_format == 'JPEG':
            # Set JPEG quality (from 0 to 100; higher means better)
            compression_params = [int(cv2.IMWRITE_JPEG_QUALITY), 58]
        elif file_format == 'PNG':
            # Set PNG compression level (from 0 to 9; higher means more compression)
            compression_params = [int(cv2.IMWRITE_PNG_COMPRESSION), 8]
        
        # Save the compressed image
        cv2.imwrite(output_path, img, compression_params)
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def compress_images(directory):
    target_folder = os.path.join(directory, "Compressed Images - OPEN CV")
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            original_path = os.path.join(directory, filename)
            file_format = 'PNG' if filename.lower().endswith('.png') else 'JPEG'
            compressed_path = os.path.join(target_folder, filename)

            compress_image(original_path, compressed_path, file_format)
            print(f"Compressed and saved: {compressed_path}")

# Make sure you have OpenCV installed, otherwise install it using pip:
# pip install opencv-python-headless
directory = "path/to/your/folder"  # Change this to the path of your folder
compress_images(directory)
