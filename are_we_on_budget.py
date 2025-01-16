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
6
123.45 678.90 1234.56 789.01 2345.67 8901.23
321.54 876.09 1432.65 987.10 2543.76 8109.32
6
250.00 349.99 150.45 782.15 650.00 99.99
225.16 299.99 160.14 798.16 650.00 75.00
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



cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    num_numbers = int(sys.stdin.readline().rstrip())
    projected_costs = sys.stdin.readline().rstrip().split(" ")
    actual_costs = sys.stdin.readline().rstrip().split(" ")

    check_numbers_for_floats([float(i) for i in projected_costs] + [float(i) for i in actual_costs])   

    variance = 0
    for i in range(len(projected_costs)):
        variance += (float(actual_costs[i]) * float_go_away - float(projected_costs[i]) * float_go_away) 

    print(round_half_up(variance / (num_numbers * float_go_away), 2))
