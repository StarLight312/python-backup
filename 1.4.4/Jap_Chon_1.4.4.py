
'''Procedure'''
#1-12 n/a

#13
# mathplotlib.pylot(plt) - This library is primarily used for the plotting and 
# creating the plot graph for the photo.
# numpy(np) - used for designing and creating the array of the plot graph. It 
# can be used to manipulate the color and background of an image.
# PIL - used to manipulate the photo's shape or what it looks like.

#14 n/a

#15a.
# Line 19 calls the function subplots from the plt library. The function is
#being called with 2 arguments: 1 and 2. The function returns 2
#objects, which are being assigned to fig and ax.

#15b. 
# Line 23 calls imshow() on ax[1]
# Line 24 calls set_xticks() on ax[1] 
# Line 25 calls set_xlim() on ax[1]
# Line 26 calls set_ylim() on ax[1]
# Line 27 calls savefig() on fig

#15c.
# (966, 1162)

#16
#Upper left(700, 940) ; Upper right(790, 940); Lower left(700, 1010)
#Width: 90px Height: 70 px;

#17a.
#It passes 2 arguements and is being assigned to the variable earth_file

#17b.
#It is being assigned to the earth_img variable

#17c. There are 2 paranthesis because one if for storing the arguements and the
# other is to store the height and width you want the new image to be resized to

#17d. The (89, 87) serves as the width and height that is being assigned to the 
#variable

#17e.Line 33 calls the function subplots from the plt library with 2 
#argument(s): 1 and 2. The function returns 2 object(s), which are 
#being assigned to fig2 and axes2.
#Line 34 calls the method imshow on the object ax with 1 argument: earth_img. 
#Line 35 calls the method imshow on the object ax with 1 argument: earth_small.
#Line 36 calls the method savefig on the object fig2 with 1 argument: 
#resize_earth.
    
#17f. 
#i. An additional arguement that can be used for resize is filter.
#ii. The default value of filter is nearest
#iii. Antiallias is recommeneded for getting a high quality downsampling filter

#17g The width and height is being represented by the size attribute. 

#17h.It outputs these values to represent the height and width of the image 
# that it is set to.

#17i. We can tell that they have a different number of pixels because of the 
#different values of their axis and the scale they are set to.

#18 I think that the resize() method uses teh information given about the
#   original image and modifes the coordinates based on the coordinates given by
#   the user. 

#19a. student_img: 682,575 bytes earth_small: 30,972 bytes

#19b. n/a

#19c. The student_img has 211,546 bytes and the earth_small has 18,774 bytes.

#19d. The values differ by a good amount due to the empty white space that the 
#     downloaded images did not include

#19e. If a color used for the first arguement, then it will fill that region 
# with the color specified. 

#19f. If they are in two different modes then they will display two different
# types of pictures depending on the mode that it is set to.

#19g The first arguement tells the image it wants to paste, the (1162, 966) are 
# coordinates that the image will be pasted, and the mask specifies the image
# that is being pasted once again.

#20 n/a(in earthEyes.py)


'''Conlcusion'''

#1 The methods we used in this lesson were resize and paste which modified the 
# overall size of the image and enabled us to paste the image to designated 
# coordinates.

#2 The abstraction we used in this activity was first having to resize the earth
# size and then getting it another earth to the deisnated location of the other
# eye. The paste and resize methods we got from the PIL library proved to be 
# helpful in comepleting this task.
