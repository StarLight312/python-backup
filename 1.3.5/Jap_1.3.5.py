'''Procedure'''

#1-4. n/a

#5. The integer, float, and sometimes string types can represent 6 million

#6. The first example resulted in a string because both variables were strings. 
#   The second example however, had a string and an interger so it resulted in 
#   an error.

#7. When the integer has a negative number as the index then it will result in 
#   the placement of the letter starting from the end. Additionally, if the
#   number is greater than the amount of iterables in a string, then it will 
#   result in an error. The iterables also count the spaces in and if it results
#   on a space, it will output " "

#8. Slicing: In order for slogan to return the string "best" I used slogan[17:]

#9. n/a

#10a. It results in 7 because it takes the length of the string that is set to 
#     activity. Theater has a length of 7 so it resulted in 7.

#10b. It first uses the string from the activity variable and outputs theate
#     because the len of activity is 7 and -1 is 6. This makes it so that it 
#     would only output from the start to the 5th iterate.

#11. It outputs true because the first string, 'test goo' is in the next string

#12.
def how_eligible(essay):
    '''This function detirmines how many of the given characters are in the 
    sentence and returns a score depending on how many there are'''
    if '?' and '!' and '"' in essay:
        return 4
    elif '?' and '!' in essay:
        return 3
    elif '?' and '!' in essay:
        return 2
    elif ',' in essay:
        return 1
    else:
        return 0



#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

#I did end up getting the correct returned values however I was unable to insert
#the comma because it ended up returning a 4 everytime I tested it.
