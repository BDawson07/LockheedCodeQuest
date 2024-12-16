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
    2,
    "Test1",
    "Test2"
]


#Rounding Half Up function
#Super scuffed, and probably not that good, but it gets the job done 
def round_half_up(value:float, decimal:int) -> str:
    negative = 1
    if value <= 0:
        negative = -1 #if it is negative, it will flip the sign in the end
        value *= -1
    new_value = value * 10**(decimal)
    print(new_value)
    
    # checks the last digit of value
    if int(str(value)[-1]) >= 5:
        new_value = int(math.ceil(new_value))
    else:
        new_value = int(math.floor(new_value))

    
    new_value = new_value / 10.00**(decimal) * negative
    new_value = str(new_value).split(".")[0] + "." + str(new_value).split(".")[1].ljust(decimal,"0")

    #Important: Returns a string
    return new_value 

def automatic_inputs() -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value

cases = automatic_inputs()

for case in range(cases):
    ###Write the logic for each Sample###
    print(automatic_inputs())
