from setuptools import setup, find_packages

setup(
    name="Mask_Package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python-headless", 
        "numpy",  
    ],
    entry_points={
        "console_scripts": [
            "Masking_images=Mask_Package.Online_Test:main",
        ],
    },
)