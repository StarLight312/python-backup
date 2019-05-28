from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np
import PIL
'''Procedure'''
#1-3 n/a

'''Part I: Using Arrays of Pixels'''

#4 Arrays and lists are similar because they both involve selecting the position
#  or a certain value that you want to modify. Arrays however, only take in 
#  account of the positioning of the image while lists look at strings and
#  integers

#5
      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
###
# Make a rectangle of pixels yellow
###

Creates a yellow rectangle at the set position
height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow


# Saves the figure
fig.savefig('women2')
'''
print(type(img))
print(img)
print(len(img))
print(len(img[0]))
print(img[5][9][1])
print(img[4][10][1])
print(img[49][24][1])
# There are 960 rows of pixels, 584 columns, the green intensity is 94, the 
# red intensity is 87 and is 95 at the 50th row and 25th pixel.

#6
# Make a rectangle of pixels yellow
###
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')

height = len(img)
width = len(img[0])
for row in range(400, 465):
    for column in range(130, 170):
        img[row][column] = [0, 128, 0] # red + green = yellow
fig.savefig('green_earing')
'''
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')

height = len(img)
width = len(img[0])
for row in range(400, 465):
    for column in range(130, 170):
        img[row][column] = [0, 128, 0] # red + green = yellow
fig.savefig('green_earing')'''
#7
'''
Creates magenta sky
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')

height = len(img)
width = len(img[0])
for row in range(155):
    for column in range(width):
         if sum(img[row][column])>500: # brightness R+G+B goes up to 3*255=765
            img[row][column]=[255,0,255] # R + B = magenta
'''


#7a. These lines tell the program to check the area in that parameter that it is
#    set to.
#7b.-7c. 

directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')

height = len(img)
width = len(img[0])
for row in range(155):
    for column in range(width):
         if sum(img[row][column])>500: # brightness R+G+B goes up to 3*255=765
            img[row][column]=[255,0,255] # R + B = magenta

height = len(img)
width = len(img[0])
for row in range(400, 465):
    for column in range(130, 170):
        img[row][column] = [0, 128, 0]
        
fig.savefig('women_sky_earing')


#8.

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns'''

    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [255, 0, 255, 255] # magenta, alpha=255
    return image
'''    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 2)
    ax.imshow(image)
    fig.savefig('mask')  ''' 
#9    
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(make_mask(100, 100, 20), interpolation='none')
height = len(img)
width = len(img[0])
for row in range(300):
    for column in range(width):
         if sum(img[row][column])>500: # brightness R+G+B goes up to 3*255=765
            img[row][column]=[255,0,255] # R + B = magenta

height = len(img)
width = len(img[0])
for row in range(400, 465):
    for column in range(130, 170):
        img[row][column] = [0, 128, 0]

        
fig.savefig('women_and_mask')