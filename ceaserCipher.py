"""
Date: MM-DD-YY
Name: 
Authors:
CodeQuestLink:
"""

#Neccicary libraries for all solutions
import sys
import math
import string

inputs = """3
1
buubdl bu ebxo
3
ghvwurb wkh fdvwoh
6
yzkgr znk ynov
"""


inputs = inputs.split("\n")

#Rounding Half Up function
#Super scuffed, and probably not that good, but it gets the job done 
#also handles leading and trailing zeros
def round_half_up(value:float,decimals:int, trailing_zeros = True, l_zeros = False, l_places = 0) -> str:

    
    #negative handling
    value = float(value)#JIK
    negative = 1
    if value <= 0:
        value *= -1
        negative = -1
    
    new_value = value*10**(decimals+1)
    new_value = math.floor(new_value)/10
    

    #rounding
    if int(str(new_value)[-1]) >= 5:
        new_value = math.ceil(new_value)
    else:
        new_value = math.floor(new_value)
    new_value /= 10**decimals * negative


    #formating
    if trailing_zeros:
        new_value = str(new_value).split(".")[0] + "." + str(new_value).split(".")[1].ljust(decimals,"0")   #trailing Zeros 
    
    if l_zeros:
        new_value = str(new_value).split(".")[0].rjust(l_places,"0") + "." + str(new_value).split(".")[1]

    return new_value




def automatic_inputs(value = None) -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value

def alteration(number, altering, max):
    number += altering
    while number <= 0:
        number += max
        
    while number > max:
        number -= max

    return number

base = ord("a") - 1


cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    ###Write the logic for each Sample###
    shift = int(sys.stdin.readline().rstrip())

    sentence = sys.stdin.readline().rstrip().split()
    new_sentence = []
    for word in sentence:
        new_word = ""
        for char in word:
            new_word += chr(base + alteration((ord(char)-base),shift*-1,26))
        new_sentence.append(new_word)
    
    print(" ".join(new_sentence))
            
