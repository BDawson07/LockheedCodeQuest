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
    3,
    160,
    200,
    265
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

def automatic_inputs() -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value


#example sys.stdin.readline().rstrip()
cases = int(automatic_inputs())

for case in range(cases):
    ###Write the logic for each Sample###
    circ_of_earth = 40_075
    altitude = automatic_inputs()
    
    distance_traveled = round_half_up(2*math.pi*(altitude + circ_of_earth/(2*math.pi)),1    )
    print(distance_traveled)