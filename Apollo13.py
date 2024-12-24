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

inputs = """2
356.69 163.42 346.67
302.26 345.92 190.39
"""
inputs = inputs.split("\n")

#Rounding Half Up function
#Super scuffed, and probably not that good, but it gets the job done 
def round_half_up(value:float,decimals:int, trailing_zeros:bool = True, leading_zeros = False, leading_places = 0) -> str:
    

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
    
    if leading_zeros:
        new_value = str(new_value).split(".")[0].rjust(leading_places,"0") + "." + str(new_value).split(".")[1]

    return new_value

def automatic_inputs(value = None) -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value

def subtract(angle:float) -> float:
    angle -= 180
    if angle <= 0:
        return 360 - abs(angle)
    else:
        return angle


cases = int(automatic_inputs())

for case in range(cases):
    x,y,z = automatic_inputs().split(" ")
    round_half_up(subtract(float(x)),2,leading_zeros=True, leading_places=3)

    print(f"{round_half_up(subtract(float(x)),2,leading_zeros=True, leading_places=3)} {round_half_up(subtract(float(y)),2,leading_zeros=True, leading_places=3)} {round_half_up(subtract(float(z)),2,leading_zeros=True, leading_places=3)}")