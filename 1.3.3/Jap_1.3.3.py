from __future__ import print_function # use Python 3.0 printing 
'''Procedure'''
#1-5 n/a

''''Part 1: Conditionals'''

#6a. It would be false because although the first part is true, it also has an 
#   and statement and the other statement was false.
#6b. It would be true because a + 2 is equal to 5 and a -1 is not equal to 3.
#7 Compund Conditional:x >= 40 and x <= 130 and y <= 120 and y>=100
#8 n/a

'''Part 2: if-else Structures & the print() function'''
#9.
def age_limit_output(age):
    '''Outputs a statement depending on if the age is more than 13 or less 
    then 13'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print('Minimum age is', AGE_LIMIT)

#9a.It outputs this because when it satisfies the function and makes it true, 
#   it will print out a certain string and if it makes it false, then it will 
#   output a different string.

#9b.
def report_grade(percent):
    '''Returns if you achieved mastery if the percent is 80 or higher and if 
    less than 80 it will print that you should seek more practice'''
    if percent >= 80:
        print("A grade of",percent, "indicates mastery. Keep up the good work!")
    else:
        print("A grade of",percent, "does not indicate mastery. Seek extra practice or help.")

'''Part 3: The in operator and an introduction to collections'''    
#10
#11
def letter_in_word(guess, word):
    if guess in word and len(guess)==1:
        return True
    else:
        return False
#12
def hint(color, secret):
    if color in secret:
        print ('The color', color, 'IS in the secret sequence of colors.')
    else:
        print ('The color', color, 'IS NOT in the secret sequence of colors.')

'''Conclusion'''
#1. The blocks that are indented after the if and else statements only work if 
#   the statement is true(or false) and everything underneath that is indented 
#   will be ran if the fucntion if true. When an if statement is true then 
#   everything else will not run.
#2. Ones I learned from this leason is or and also and. The not operator is also 
#   another boolean operator
#3. Ira: The code won't necessarily go slower just because there are 2 commands
#   but she is correct when thinking that the code will output that string no 
#   matter what
#3. Jayla: She makes a good point that it would be easier to just move all to 
#   one line so you won't have to worry about forgetting it when you want to 
#   change the code later
#3. Kendra: This is kind of untrue because one line doesn't really make much a 
#   of a difference to the memory of the program.

'''Assignment Check'''
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)