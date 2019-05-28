import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
'''Procedure'''
#1-3 n/a

'''Part I: Working with a Filesystem'''

#4. The absolute filename of nice.jpg is desktop

#5. The relative file name is users/studentlogin/nice.jpg

#6.  C:\\Windows\\Cursors\\cursor1.png is an absolute filename. No, it is not 
#    necessary to be in a particular directory for this file. The difference 
#    between the different commands is the type of input and format you would 
#    need to set it up with.




'''Part II: Rendering an Image on a Screen'''


#7 Test Code:
'''Read the image data'''
directory = os.path.dirname(os.path.abspath(__file__)) 

filename = os.path.join(directory, 'crazy_mice.jpg')

img = plt.imread(filename)


fig, ax = plt.subplots(1, 2)

ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[1].plot(115, 40, 'ro')
ax[1].plot(140, 40, 'ro')
ax[1].plot(40, 45, 'ro')

fig.savefig('crazy_mice')

'''
JDoe_JSmith_1_4_2: Read and show an image.

This code plots one subplot

Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_plot')'''



#7a The nose is around (275, 400)

#7b The cat's nose is around (60, 40)

'''Part III: Objects and Methods'''
#8a. fig is an instance of the the Figure class and ax is an instance of the 
#    AxesSubPlot class

#8b. Similarly, in line 25, the method savefig is being called on the object
#    fig. That method is being given 1 arguments. That method is a method of 
#    the class Figure

#8c. The comment states that it will show the image/figure on the screen

'''Part IV: Arrays of Objects'''

#9a. The method imshow is being called on the object ax.

#9b. 
'''
This creates 2 subplots
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('two_woman')
'''

'''
This creates 5 subplots
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats')
'''

'''Part V: Keyword = Value Pairs'''

#10 The interpolations are related in the way it tells us where to focus on the
#   image. Additionally, the code creates a similar picture coompared to the
#   picture given but not exact because the data points may not be exact.
'''
Focuses on a certain part of the picture
Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')
'''

#11a.

'''Read the image data
Makes the image upside down
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

fig, ax = plt.subplots(1, 1)
# Show the image data in the first subplot
ax.imshow(img, interpolation='none') # Override the default
ax.imshow(img)
ax.set_xlim(100, 500)
ax.set_ylim(100, 500)
ax.set_xlabel('Width')
ax.set_ylabel('Height')
# Show the figure on the screen
# fig.show()
fig.savefig('experiment.png')'''


#11b. 
'''
Creates 3 close up pictures of the image

directory = os.path.dirname(os.path.abspath(__file__)) 

filename = os.path.join(directory, 'cat1-a.gif')

img = plt.imread(filename)


fig, ax = plt.subplots(1, 3)

ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(45, 55)
ax[0].set_ylim(110, 100)
ax[1].set_xlim(55, 65)
ax[1].set_ylim(100, 90)
ax[2].set_xlim(65, 75)
ax[2].set_ylim(90, 80)

fig.savefig('three_closeup.png')'''

#12 An example of another method would be the change_geomatry method which has
#   numrows, numcols, and num as it's arguements. It's default value is whatever
#   is inserted in the arguements

#13
#Plots red dots on the given location
'''directory = os.path.dirname(os.path.abspath(__file__)) 

filename = os.path.join(directory, 'crazy_mice.jpg')

img = plt.imread(filename)


fig, ax = plt.subplots(1, 2)

ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[1].plot(115, 40, 'ro')
ax[1].plot(140, 40, 'ro')
ax[1].plot(40, 45, 'ro')

fig.savefig('crazy_mice')'''

