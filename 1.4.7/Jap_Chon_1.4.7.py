from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw    
from PIL import Image, ImageOps
import os, sys

'''
path = ('/home/ubuntu/workspace/1.4.7/Project_images')
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((500,500), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

directory = os.path.dirname(os.path.abspath(__file__))  
basketball_file = os.path.join(directory, 'Project_images/nike_basketball.jpg')
'''


'''
# Open and show the student image in a new Figure window
nike_basketball = PIL.Image.open(basketball_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(nike_basketball, interpolation='none')

# Open, resize, and display earth
nike_logo = os.path.join(directory, 'Project_images/nike_logo.jpg')
nike_img = PIL.Image.open(nike_logo)
nike_small = nike_img.resize((100, 100)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(nike_img)
axes2[1].imshow(nike_small)
fig2.savefig('small_logo')


# Paste earth into right eye and display
# Uses alpha from mask
nike_basketball.paste(nike_small, (1300, 1300), mask=nike_small)
# Display
fig3, axes3 = plt.subplots(1, 1)
axes3[0].imshow(nike_basketball, interpolation='none')
fig3.savefig('logo_test')

nike_small.save('smallLogo.png')


# Display

fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(nike_basketball, interpolation='none')
axes3[1].imshow(nike_basketball, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('logo_in_basketball')
'''


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

    fig.savefig('blue_shoes')
    
def change_jersey(original_picture):
    directory = os.path.dirname(os.path.abspath(__file__)) 
    filename = os.path.join(directory, 'basketball_jersey.jpg')
    img = plt.imread(filename)

    fig, ax = plt.subplots(1, 1)
    ax.imshow(img, interpolation='none')
    
    height = len(img)
    width = len(img[0])
    for row in range(700):
        for column in range(width):
            if sum(img[row][column]) > 0 and sum(img[row][column]) < 400: # brightness R+G+B goes up to 3*255=765
                img[row][column]=[0,128,0] # R + B = magenta

    fig.savefig('green_jersey')
    
def change_cloth(original_picture):
    directory = os.path.dirname(os.path.abspath(__file__)) 
    filename = os.path.join(directory, 'nike_cloth.jpg')
    img = plt.imread(filename)

    fig, ax = plt.subplots(1, 1)
    ax.imshow(img, interpolation='none')
    
    height = len(img)
    width = len(img[0])
    for row in range(1088):
        for column in range(width):
            if sum(img[row][column]) > 0 and sum(img[row][column]) < 400: 
                img[row][column]=[255,140,0] 

    fig.savefig('orange_cloth')
    
    nike_logo = os.path.join(directory, 'Project_images/nike_logo.jpg')
    nike_img = PIL.Image.open(nike_logo)
    nike_small = nike_img.resize((100, 100)) #eye width and height measured in plt
    fig2, axes2 = plt.subplots(1, 2)
    axes2[0].imshow(nike_img)
    axes2[1].imshow(nike_small)
    fig2.savefig('small_logo')

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list


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
if __name__ == '__main__':
    in_img = 'orange_cloth.png'
 
    add_border(in_img,
               output_image='border_orangecloth.png',
               border=25,
               color='black')

def resize_img(original_image):
    result = original_image
    result = result.resize(250, 250)
    return result
    
def resize_all_image(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = resize_img(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    

resize_all_image()
    
#color changing functions
change_shoe('redshoe.jpg')   
change_jersey('basketball_jersey.jpg')
change_cloth('nike_cloth')