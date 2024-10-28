# Image Masking with OpenCV

This project processes a set of JPEG images to create binary mask images. The binary masks are generated based on the condition that all three channels of a pixel must be above 200. The resulting masks are saved as PNG files (lossless format), and the total count of pixels meeting this condition across all images is logged.

### Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required libraries using pip:

```bash
pip install opencv-python numpy
```
### Project Structure
```

/Masking_Images
│
├── Mask_ImagesScript
│    ├── images/            # Directory containing input JPG files
│    ├── mask_images/       # Directory to save output mask images
│    ├── Masking_Image.py   # Main script to process images
├── Mask_Package
│    ├── Mask_Package
|    |    ├── Online_Test.py  # Main script to process images
|    |    ├── __init__.py
│    ├── images/            # Directory containing input JPG files
│    ├── mask_images/       # Directory to save output mask images
│    ├── setup.py                      
└── README.md               # Project documentation

```
Project structure contains two folders, 1. Mask_ImagesScript : to run script directly and 2. Mask_Package : to run as a package. 

### Mask_Package Usage

1. Place your JPEG images in the images/ directory.
2. Update the paths in the Online_Test.py file for the input_dir and output_dir variables to point to respective directories.
3. Run the script:
    python Online_Test.py
4. The binary masks will be saved in the mask_images/ directory, and the total number of max pixels will be printed in the console.


### Functionality

* Parallel Processing: The script utilizes Python's concurrent.futures to process multiple images in parallel, improving performance for large datasets.
* Binary Mask Generation: Masks are created where a pixel is set to 255 (white) if all three color channels (R, G, B) are greater than 200.
* Logging: The total count of pixels meeting the mask condition is logged for reference.
