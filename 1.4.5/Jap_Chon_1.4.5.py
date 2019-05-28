from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
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

def round_corners_of_all_images(directory=None):
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
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    

round_corners_of_all_images()

'''Procedure'''
#1-4 n/a

#5 The 3 function names are round_corners_one_image, get_images, and 
#  round_corners_of_all_images.

#6 It created a new folder called modified. 

#7a. Arguement 1: original_image; Arguement 2: percent_of_side; 
#    Return Value: result

#7b. The color is purple-ish

#7c. rounded_mask is the object created in line 26 and drawing_layer for line 27

#7d.We would want the alpha value to be 0 for the background to be transparant. 

#7e. Lines 33-38 creates the two purple rectangles while lines 41-48 creates the 
# 4 blue circles on the edge.

#7f. The rgb color on line 54 is black.

#7g. The color values of the corners are white.

#8a. The get_images() function can have either 0 or 1 arguements.

#8b. The function returns 2 objects: which are both lists.

#8c. os.getcwd(), os.listdir(directory), os.path.join(directory, entry)

#8d. os.listdir(directory): Return a list containing the names of the entries in
#the directory given by path. The list is in arbitrary order, and does not 
#include the special entries '.' and '..' even if they are present in the
#directory.

#8e. This function uses a try-except structure just in case if any of the images
# do not open for some reason and make sure it executes the code for all the 
# images that need to be manipulated. Some disadcantages include not knowing 
# what error you may have done because it the structure skips over the mistake 
# if it is listed in the except section already.

#8f. These lines check if the error is an IOE error and if it is than it will 
# pass and continue the function for the other images.

#9a. This is to create a directory for all the images while also checking to see 
# if they already have a directory or not. If they do then the program skips 
# over it and moves on to the next one.

#9b. It checks for all the images in that range/length of the list. The number 
# represents how many images there are.

#9c. The n represents the position of the images it will be checking one by one 
# and execute the code based on the image it is on.

'''Conclusion'''

#1. This is accomplished by using the mask to make a certain shape and to get a
# transparent background that makes it able to see through

#2. This made it easier because we could call the function we want the image to
# to use for the manipulation. Adiitionally, it made the work neater and we were
# able to seperate it into different sections based on what the code does.

#3. I think that Alice is somewhat right that pictures are always manipulated
# because the photo taken are always going under some type of manipulation
# wheter it be the resizing of the photo when it is taken or other types of 
# change. I dont exactly agree with Barb because her claim is kind of general 
# and I dont agree with how she believs that some manipulations are fake since
# a manipulated photo is still real and just a modified version of the real one.

#4 If the picture is your own then I believe that you can use or manipulate or 
# sell it anyway you want to. However if the picture is orginally someone else's
# even after you manipulate it, I think the credit should still belong to the 
# person who took the original photo. Even if you manipulate it completly,
# credit should still be given to the creator,

#5.Overall our team worked well togther and provided assistance when we needed
# it. Also, we communicated on our ideas and made sure each one of us got the 
# lesson. One thing we can improve on is seeking help from other groups 
# instead of just relying on each other.