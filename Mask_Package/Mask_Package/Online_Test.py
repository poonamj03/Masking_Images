import cv2
import numpy as np
import os
import concurrent.futures
from glob import glob

# Input directory containing JPG files
input_dir = "./images"
# Output directory for binary mask images
output_dir = "./mask_images"
os.makedirs(output_dir, exist_ok=True)

# Function to process each image
def process_image(file_path):
    # Read the image
    image = cv2.imread(file_path)
    if image is None:
        print(f"Image {file_path} Could not found!")
        return 0

    print(image.shape)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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

    image = cv2.imread("C://Users//Jangid.Poonam//Downloads//Online-test//images//faroe_island_1.png")
    print(image.shape)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # # Get all JPG files from the input directory
    # image_files = glob(os.path.join(input_dir, "*.png")) + glob(os.path.join(input_dir, "*.jpg"))
    
    # total_max_pixels = 0
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     # Process each image in parallel
    #     results = list(executor.map(process_image, image_files))
        
    #     # Sum up all max pixel counts from each image
    #     total_max_pixels = sum(results)
    
    # print(f"Total max pixels across all images: {total_max_pixels}")

if __name__ == "_main_":
    main()

# image = cv2.imread("C://Users//Jangid.Poonam//Downloads//Online-test//images//faroe_island_1.png")
# print(image.shape)
# cv2.imshow("Original Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()