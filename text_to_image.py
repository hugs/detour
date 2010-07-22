#!/usr/local/bin/python

import os
import sys

from detour.converters import get_file_parts
from detour.converters import file_to_jpeg
from detour.converters import jpeg_to_tga

if __name__ == '__main__':
    if len(sys.argv) > 1:
        textfilepath = sys.argv[1]
        path, filename, name = get_file_parts(textfilepath)       
 
        # Create jpeg file
        jpegfilepath = os.path.join(path, name + '.jpg')
        file_to_jpeg(textfilepath, jpegfilepath)
        
        # Create tga file 
        tgafilepath = os.path.join(path, name)
        jpeg_to_tga(jpegfilepath, tgafilepath)
    else:
        print """
  Text to Image Converter 
  Usage: 
    $ python text_to_image.py <file-name> 
  Output:
    filename.jpg and filename.tga will be created in the directory as <file-name>
    """
