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

inputs = [
1,
"3 5",
"computer",
"mouse",
"program",
"konpuder",
"house",
"compoooo",
"anagram",
"oeifeln"
]


#Rounding Half Up function
#Super scuffed, and probably not that good, but it gets the job done 
def round_half_up(value:float,decimals:int, trailing_zeros:bool = True) -> str:
    

    value = float(value)#JIK

    #handles negative values
    negative = 1
    if value <= 0:
        value *= -1
        negative = -1
    
    new_value = value*10**(decimals+1)
    new_value = math.floor(new_value)/10
    
    if int(str(new_value)[-1]) >= 5:
        new_value = math.ceil(new_value)
    else:
        new_value = math.floor(new_value)
    
    new_value /= 10**decimals * negative

    if trailing_zeros:
        new_value = str(new_value).split(".")[0] + "." + str(new_value).split(".")[1].ljust(decimals,"0")   #trailing Zeros 

    return new_value

def automatic_inputs(cool:int) -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    ###Write the logic for each Sample###
    
    dicts, words = sys.stdin.readline().rstrip().split(" ")
    correct_words = []
    for i in range(int(dicts)):
        correct_words.append(sys.stdin.readline().rstrip().lower())

    for i in range(int(words)):
        biggest_hamming = 100000000
        closest_word = ""
        new_word = sys.stdin.readline().rstrip().lower()
        for check_word in correct_words:
            hamming = 0

            if len(check_word) != len(new_word):
                continue
            
            for i in range(len(new_word)):
                if check_word[i] != new_word[i]:
                    
                    hamming += 1
            if hamming < biggest_hamming:
                biggest_hamming = hamming
                closest_word = check_word
                 
        print(closest_word)