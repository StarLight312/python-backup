import random 
'''Procedure'''

#1-3 n/a

'''Part I: Tuples, Syntax'''

#4 (3, 7, 13)

#5 To submit work, we mainly use google classroom room to digitally hand in 
#  what we worked on. Additionally, our teacher would want us to use lower case
#  letters and use the underscore to sperate words.

#6a I predict that it will result in the string b because b is indexed as 1.

#6b I think that it result in a and b because when it is formatted this way, it 
#   returns the starting value and everything after it up to the second number
#   This makes it so that it will not print out 3 and just the and b string.

#7a It printed out true because b was still thinks that a is equal to 10 as it 
#   has not been restarted.

#7b It prints out 15 because after restating the b = (9, a, 11) it gave a its
#   updated value of 15 in which it was set to earlier.

'''Part II: Lists'''
 #8 I think it will result in b and 3 because the 1: outputs the value at the 1
 #  index all the way to the end.
 
 #9 It resulted in false because after changing it to '3', it changes it to a 
 #  string. Because it is a string, it outputed false when it was checked if it 
 #  was equal to 3
 
 #10a I think the output will add the two new values at the end of the list 
 #    because value was set to value added with 2 new values added to the list.
 
 #10b I predict that it will add the 6 and 7 value into the list as it got
 #    appended into the list

#11 This does not work because it does not specify what it wants to add 5 to
#   and additionally, it won't add 5 to the list because it is not appended the
#   right way.

#12 It will result in 18 because it is multiplied by 3 and set directly back to 
#   the a variable.

#13 n/a

#14
def roll_two_dice():
    '''Randomly rolls 2 sets of dices with numbers in a list and adds them
    together to get the sum after the 2 dices have been rolled.'''
    final = 0
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    final = random.choice(dice1) + random.choice(dice2)
    return final


#Assignment Check
#1.3.6 Function Test
print(roll_two_dice())

#1 I got a random sum of numbers after running the code so I believe that I 
#  have completed the assignment successfully.
 