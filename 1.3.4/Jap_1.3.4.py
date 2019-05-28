from __future__ import print_function # must be first in file 
import random

'''Procedure'''


'''Part 1: Nested if structures and testing'''
#1
def food_id(food):
    ''' Returns categorization of food
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a. It ouputs, 'NOT Citrus, Fruit' which is a result of line 17(line 22 for my
#    code)

#1b. I. It will activate upon the input of the if statement on line 19
#    II. It will execute its command when line 19 is false
#    III. The input from line 25 will return the statemnt on line 26

#1c. It will never result as starchy because banana is already considered a 
#    citrus and will not do the else command because the if function had 
#    already been executed.

#2
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()'
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id'
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
#3.
def f(n):
    '''This function will test if the number is an integer, an even number, a
    multiple of 6, an odd number or if it is not an even number'''
    if int(n) == n:
        if n % 2 == 0 and n % 3 == 0:
            print ("The number is a multiple of 6")
            return "The number is a multiple of 6"
        elif n % 2 == 0 and n % 3 != 0:
            print ("The number is an even number")
            return "The number is an even number"
        else:
            print ("The number is an odd number")
            return "The number is an odd number"
    else: 
        print ("The number is not an even number")
        return "The number is not an even number"
        
#4. We would use the for loop or something to access the dictionary or list we 
#   want to view.

#5.

def f_test():
    '''This will test if the function is working the way it is supposed to
    and the statements print out All good if it works and there's a bug if
    it doesn't'''
    works = True
    if f(12) != "The number is a multiple of 6":
        works = 'Multiple of 6 bug in f(n)'
    if f(2) != 'The number is an even number':
        works = 'Even number bug in f(n)'
    if f(1) != 'The number is an odd number':
        works = 'Odd number bug in f(n)'
    if f(1.5) != "The number is not an even number":
        works = 'Not even number bug in f(n)'
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
#6. Missing?

#7. When + is used as concatation, then it will output the answer as a string
#   and only add the 6 to the end of the 5.5. The Numeric addition adds the 
#   number/value set to the variable together to get the sum of the numbers.

#8
def guess_once():
    '''It will print a random number and if you guess the right number, 
    it will say you got it right'''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '!', sep='')
    elif guess > secret:
        print('Too high, my number was ', secret, '!', sep='')
    else:
        print('Right on! I was number ', guess, end='!\n')
#8a. Just like how the sep= command seperates the strings and spaces it out to 
#    the given function, the end= makes so that at the end of the string, it
#    it will have a ! to end the string. 

#8b.

#9. 
def quiz_decimal(low, high):
    '''Tests the function if the number inputted is higher or lower
    than the numbers used. If it was higher than the highest value, then it 
    will say that the number is greater than the value, and lower if it was
    lower than the value. '''
    print ("Type a number between ", low, "and ", high, ":")
    number = float(raw_input())
    if number > high:
        print ("No, ", number, "is greater than ", high)
    elif number < low: 
        print ("No, ", number, "is less than ", low)
    elif number == low:
        print ("No, ", number, "is equal to ", low)
    elif number == high:
        print ("No, ", number, "is equal to ", high)
    else:
        print ("Good!", low, "< ", number, "< ", high)
        
#Conclusion

#1. If functions can be used in the glass box testing to detirmine if the 
#   statement is true or not.

#2. Depending on if the function is true or not, the code could just execute
#   one of the blocks.

#3. Programers use test suites first to detirmine if the code results in the 
#   way they want it to. Additionally, this will also verify if there are any
#   bugs in the program so the coder can know what and where the bug is before
#   testing it out.

#4 Yes you can create a function for each output

#Challenge:
#1. 
def f_challenge(n):
    '''This function checks wheter or not the number that is tested is
    an integer, a multiple of 6, an even number, or an odd number'''
    if int(n) != n:
        print (n, "is not an integer")
    elif n % 2 == 0 and n % 3 == 0:
        print (n, "is a multiple of 6")
    elif n % 2 == 0 and n % 3 != 0:
        print (n, "is an even number")
    else:
        print (n, "is an odd number")
        

    
'''Assignment Check'''
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)

#I recieved the result I coded for and it printed out the code that it was 
# suppose to print.