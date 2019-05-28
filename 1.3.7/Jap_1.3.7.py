from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random


'''Procedure'''
#1-3 n/a

'''Part I: for loops, range() and help()'''

#4
def days():
    ''' It will evaluate the letters in the string of MTWRFSS and print out the 
    each letter and day at the end one by one. It will then print out the
    range of 5,8 and the the string based off list'''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
#5


def picks():
    '''Picks a random number from the list 5 times and adds it to the variable.
    Then it will save it as a histogram and create a file called picks'''
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')

#6a

def roll_hundred_pair():
    '''It rolls 2 dices 100 times and puts the sum into a histogram. It then 
    creates a new file called roll_hundred_pair that displays the histogram'''
    individual_rolls = []
    dice_1 = [1, 2, 3, 4, 5, 6]
    dice_2 = [1, 2, 3, 4, 5, 6]
    for number in range(1,101):
        individual_rolls += [random.choice(dice_1) + random.choice(dice_2)]
    
    plt.hist(individual_rolls)
    plt.savefig('1.3.7/roll_hundred_pair')
    

#6b 
def dice(n):
    '''Adds the sum of the 2 dice rolls the amount of times you specify it to
    do so. It will then return the result.'''
    total = 0
    for roll in range(n):
        dice_1 = random.choice([1, 2, 3, 4, 5, 6])
        dice_2 = random.choice([1, 2, 3, 4, 5, 6])
        total += dice_1 + dice_2
    return "Roll was %s" % total
    
#Part II: While loops

#7 Line 2 is necessary because the while loop will not run if guess is already
#  true. If guess was a, then it would not run the while loop since the guess is 
#  already in the answer.

def validate():
    '''It checks if your guess is in the answer or not and if it is then it
    will print Thank you.'''
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    
#8 

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''This function picks randomly from the 4 players and asks the user to
    guess the winner. If it isn't the randomly picked answer, then it will keep
    prompting them to keep guessing. The arguements are strings.
    '''
    winner = random.choice(players) 

    ####
    # This section prints out a statement and the availble options of people 
    # you can choose from. It prints out a comma and space in between players 
    # name
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: #This line prints out a comma after each
    #of the players name and a space afterwards
        print(p+', ',)
    print(players[len(players)-1]) # This line prints out the name of each
    #player

    ####
    # This code asks for an input and if it isnt the winner then it will keep
    # asking them to guess.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses   
#9.   
def goguess():
    '''This function is a number guessing game in which it picks a number
    randomly from 1 to 20. The user then has to guess what they number is and 
    if it is greater than or less then it will state it. If it is right, then
    it will print out a statement and say how many guesses it took'''
    print ("I have a number between 1 and 20 inclusive.")
    options = range(1,21)
    number = random.choice(options)
    guesses = 1
    guess = int(raw_input("Guess: "))
    while guess != number:
        if guess > number:
            print ("%s is too high" % guess)
            guess = int(raw_input("Guess: "))
        elif guess < number:
            print ("%s is too low" % guess) 
            guess = int(raw_input("Guess: "))
        guesses += 1
        
    print("Right! My number is %s! You guessed in %d guesses!"%(guess, guesses)) 
    
#10 It will vary on your luck as it could take just one attempt to get it right
#   or it could all 6000 tries to get the number correct.

'''Part III: Practice'''

#11a. 

def matches(ticket, winners):
    '''Checks if each number in ticket and if it is in winners. It then returns
    however many matching numbers there are.'''
    matches = 0
    for i in ticket:
        if i in winners:
            matches += 1
    return matches
    
def report(guess, secret):
    '''It first checks for all the colors in guess if it is the same color and 
    the same position as the color in secret. If it is it will add one to a 
    variable. Then it checks for the colors that are the same but not in the 
    correct position and also adds that to the result.'''
    result = []
    correct = 0
    j = 0
    while j < len(guess):
        i = 0
        while i < len(secret):
            if (guess[j] == secret[i]):
                if (i == j):
                    correct += 1
                    break
            i += 1
        j += 1
    
    number = 0
    j = 0
    while j < len(guess):
        i = 0
        while i < len(secret):
            if guess[j] == secret[i]:
                number += 1
                secret.remove(secret[i])
                break
            i += 1
        j += 1

    result.append(correct)
    result.append(number-correct)
    return result        
            
'''Conclusion'''
#1. If the programmer repetedly does the same code over and over again instead
#   of using a loop, there will be more prone to errors, less viable in certain
#   situations and would not look that clean overall

#2. They both involve using both sets of data and iterating through the data 
#   values in order to get the results.

#3. A while loop will only run if the given condition is true. A for loop will
#   keep on running depending on what you set it to.

#4. Me and my partner worked well together. We helped each other when we had 
#   questions and explained what the code meant when we were stuck. Additionally
#   we worked together to be able to brainstorm ways to complete the problem.

'''Assignment Check'''
#1.3.7 Function test
days()
picks()
roll_hundred_pair()
dice(5)
validate()
guess_winner()
goguess()
t = [11, 12, 13, 14, 15]
w = [3, 8, 12, 13, 17]
print (matches(t, w))
g = ['red','red','red','green','yellow']
s = ['red','red','yellow','yellow','black']
print (report(g, s))


#1. Yes I have completed the function check and it is working when ran
                
    

            