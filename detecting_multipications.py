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
.3 .61 .4 .15 .81 .47 .98
.2 .64 .7 .36 .63 .71 .09
.45 .53 .59 .13 .21 .78 .34 .78 .91
.87 .71 .32 .33 .58 .61 .79 .86 .62
.5 .71 .42 .36 .49 .82 .6 .21
.67 .41 .76 .83 .85 .12 .51 .92
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

#simplifies floating point math by simply getting rid of the floating points. Call this with a list of all values that will
#have floats and code things like addition or subtraction with the float_go_away value in mind
def check_numbers_for_floats(values:list) -> None:
    global float_go_away
    float_go_away = 1

    greatest_len = 0
    for i in values:
        if len(str(float(i)).split(".")[1]) > greatest_len:
            greatest_len = len(str(i).split(".")[1])   #finds the most complicated float value
    
    #At this point does it matter?
    if greatest_len >= 30:
        greatest_len = 30
    float_go_away = 10**(greatest_len)
    

    

def automatic_inputs(value = None) -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value



cases = int(automatic_inputs())

for case in range(cases):
    ###Write the logic for each Sample###
    antennas = automatic_inputs().split(" ")
    hamronics = automatic_inputs().split(" ")

    indexes = []
    for i in range(len(antennas)):
        if .6 < float(antennas[i]) <= .85:
            if .6 < float(hamronics[i]) <= .85:
                indexes.append(str(i))
    if len(indexes) == 0:
        
        print("No multipaction events detected.")
    elif len(indexes) == 1:
        print(f"A multipaction event was detected at time index {indexes[0]}.")
        print("")
    else:
        print(f"{len(indexes)} multipaction events were detected at time indices: {' '.join(indexes)}.") 
