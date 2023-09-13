""""
Implemented by Federico Zocco
Last update: 13 September 2023

This scrit resizes the original images and overwrite them.
The new size, i.e. 128 x 128, fits into the RAM.

This script has been used to generate "InhPoints_50images128x128.npy" for
the training notebook "InhPoints_training.ipynb".  

Refer to "InhPoints_training.ipynb" for more info.
"""

from PIL import Image
import os, sys

path = "your_path_to_folder/InhPoints_images128x128/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((128,128), Image.Resampling.NEAREST)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()
