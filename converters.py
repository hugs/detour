import os

import Image
import ImageFont
import ImageDraw
from visual import materials

TOP_MARGIN    = 20
LINE_HEIGHT   = 25
BOTTOM_MARGIN = 20
FONT_PATH     = "/System/Library/Fonts/Monaco.dfont"

def file_to_image(filepath):
    lines = open(filepath,'r').readlines()
    image_size = TOP_MARGIN + len(lines)*LINE_HEIGHT + BOTTOM_MARGIN
    
    #image = Image.new("RGB", (1250, image_size), (255, 255, 255))
    image = Image.new("RGB", (1024, 512), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, 20,  encoding="unic")
    
    for line_number, line in enumerate(lines):
        draw.text( (20, TOP_MARGIN + (line_number*LINE_HEIGHT) ), line, font=font, fill="black")
    
    return image 

def image_to_texture(image):
    return materials.texture(data=image, mapping="sign")

def file_to_texture(filepath):
    image = file_to_image(filepath) 
    texture = image_to_texture(image)
    return texture

def file_to_jpeg(textfilepath,imagefilepath):
    image = file_to_image(textfilepath) 
    image.save(imagefilepath, "JPEG", quality=90)

def jpeg_to_tga(jpegfilepath, name):
    from visual import materials
    image = Image.open(jpegfilepath)
    materials.saveTGA(name,image)

def get_file_parts(filepath):
    '''Derive file name parts for a given filepath'''
    path, filename = os.path.split(filepath)
    name = os.path.splitext(filename)[0]
    return path, filename, name
