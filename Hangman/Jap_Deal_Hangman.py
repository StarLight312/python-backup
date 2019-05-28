import random
import time 
#def hangman_display(guessed, secret):
#    '''This function first checks for all the letters in secret one by one. 
#    It then adds the letter to the empty string: result, if that letter is in 
#    guessed. If the letter is a space it would add a space to the result string.
#    Lastly for everything else, it adds a '-' to the result string. Finally, it 
#    returns the result string.'''
#    result = ""
#    for letters in secret:
#        if letters in guessed:
#            result += letters
#        elif letters == " ":
#            result += letters
#        else:
#            letters = "-"
#           result += letters
    
#       return result 
    

def hangman_game():
    '''The game first picks a random word from the list of themed words we 
    chose to include. It then prints it out so we can easily test the function.
    Next it prints out the introduction to our game and asks for the user to
    guess what the word is. It then prompts the user to keep guessing letters
    untill they get the word. It then checks if the letter is in the random 
    word and replaces the "-" with the letter if it is in the word. If it is not
    in the random word, it will say you got it wrong and subtract your life 
    counter by 1(you have 7 in total). If you end up losing all your life 
    counters, you lose and it will display an option to restart. If you end up 
    guessing the full answer, it will congratulate you and also ask if you 
    would like to play again. Also, we added a statement that checks to make
    sure that the user only put in one letter, otherwise it will remind the user
    to input just one letter at a time.'''
    life_counter = 7
    answer = ""
    themed_words = ["dragon", "hydra", "griffin", "chimera", "fairy", "unicorn",
    "orc", "wizard", "elf", "goblin", "dwarf", "hobbit"]
    random_word = random.choice(themed_words)
    print (random_word)
    print "Welcome to our Hangman Game: The Mythical Outdoors!"
    time.sleep(1.5)
    print "Our theme is Mythical Creatures! Try and guess our word: "
    time.sleep(1.5)
    for letter in random_word:
        answer += "-"
    print (answer)
    counter = 0
    
    while life_counter > 0:
        if answer == random_word:
            print "Congrats, you guessed our word!"
            print "Would you like to play again?"
            print "Click y to restart and n to stop"
            life_counter = 0
        else: 
            guessed_letter = raw_input()
            guessed_letter = guessed_letter.lower()
            if len(guessed_letter) == 1:
                letter_found = 0
                for letters in random_word:
                    current_answer = ""
                    if letters == guessed_letter:
                        index = 0 
                        while index < len(answer):
                            if (guessed_letter == random_word[index]):
                                current_answer += guessed_letter
                                letter_found = 1
                            
                            else:
                                current_answer += answer[index]
                            index += 1
                        
                        answer = current_answer 
                                
                if (letter_found == 0):
                    print "That letter is not in the word."
                    life_counter -= 1
                    print "Guesses Left: %s" % life_counter
            else:
                print "-You need to print in a single letter-"    
            print (answer)
        
            if life_counter == 0:                    
                print "You lose!"
                print "The word was %s" % random_word
                print "Would you like to play again?"
                print "Click y to restart and n to stop"
    start_over()       
def start_over():
    '''Asks user for an input of y or n.'''
    restart_choice = raw_input()
    if restart_choice == "y":
        hangman_game()
    elif restart_choice == "n":
        print "Game Over"
    else:
        print "That's not an option"
        start_over()
        
        
hangman_game()