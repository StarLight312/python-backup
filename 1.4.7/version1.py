from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw    
from PIL import Image, ImageOps
import os, sys

def change_shoe(original_picture):
    directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
    filename = os.path.join(directory, 'redshoe.jpg')
# Read the image data into an array
    img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
    fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
    ax.imshow(img, interpolation='none')
    
    height = len(img)
    width = len(img[0])
    for row in range(300):
        for column in range(width):
            if sum(img[row][column]) < 400:
                # brightness R+G+B goes up to 3*255=765
                img[row][column]=[0,0,255] # R + B = magenta

    img.save('blue_shoes')

    '''
def add_border(input_image, output_image, border, color=0):
    img = Image.open(input_image)
 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
 
    bimg.save(output_image)
 
if __name__ == '__main__':
    in_img = 'blue_shoes.png'
 
    add_border(in_img,
               output_image='border_blueshoe.png',
               border=25,
               color='black')
               '''
               
change_shoe('redshoe.jpg')