import cv2
import numpy as np
import os
import concurrent.futures
from glob import glob
import time

# Input directory containing JPG files
input_dir = "C:\\Users\\Jangid.Poonam\\Downloads\\My_Package\\images"
# Output directory for binary mask images
output_dir = "C:\\Users\\Jangid.Poonam\\Downloads\\My_Package\\mask_images"
os.makedirs(output_dir, exist_ok=True)

# Function to process each image
def process_image(file_path):
    # Read the image

    image = cv2.imread(file_path)
    print(f"Reading {file_path}")

    if image is None:
        print(f"Image {file_path} Could not found!")
        return 0

    print(image.shape)
    # cv2.imshow("Original Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Create a binary mask where all channels are above 200
    mask = np.all(image > 200, axis=2).astype(np.uint8) * 255  # 255 for binary mask
    
    # Save the mask as a PNG file (lossless format)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_mask.png")
    cv2.imwrite(output_path, mask)
    
    # Count max pixels in the mask
    max_pixel_count = np.sum(mask == 255)
    return max_pixel_count

def main():
    # Get all JPG files from the input directory
    image_files = glob(os.path.join(input_dir, "*.png")) + glob(os.path.join(input_dir, "*.jpg"))
    
    total_max_pixels = 0
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Process each image in parallel
        results = list(executor.map(process_image, image_files))
        
        # Sum up all max pixel counts from each image
        total_max_pixels = sum(results)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total max pixels across all images: {total_max_pixels}")
    print(f"Time Taken for processing : {elapsed_time:.6f} seconds")
    print(f"Number of threads used : {executor._max_workers}")

main()