"""
Date: 12/16/2024
Name: CalculatOR
Authors: @BDawson07
CodeQuestLink: https://lmcodequestacademy.com/api/static/problems/calculator
"""

#Neccicary libraries for all solutions
import sys
import math
import string

inputs = [
"4",
"1 + 2",
"2 - 3",
"3 * 4",
"4 / 5"
]


#Rounding Half Up function
#Super scuffed, and probably not that good, but it gets the job done 
def round_half_up(value:float,decimals:int) -> str:

    

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

    new_value = str(new_value).split(".")[0] + "." + str(new_value).split(".")[1].ljust(decimals,"0") 

    return new_value

def automatic_inputs() -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value

cases = int(sys.stdin.readline().rstrip())


for case in range(cases):
    ###Write the logic for each Sample###
    equation = sys.stdin.readline().rstrip()
    flipped = [i for i in equation.split(" ")[::-1]]
    v1, v2 = eval("".join(equation)), eval("".join(flipped))
    print(f"{round_half_up(v1,1)} {round_half_up(v2,1)}")