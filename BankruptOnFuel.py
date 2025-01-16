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
203 3
101 50 300
199 2
100 102
410 5
50 75 100 125 150


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



cases = int(sys.stdin.readline().rstrip())


def count_not_full():
    count = 0
    for i in list_of_tanks:
        if not i["full"]:
            count += 1
    return count

for case in range(cases):
    list_of_tanks = []
    ###Write the logic for each Sample###
    units_of_fuel, tanks = sys.stdin.readline().rstrip().split(" ")

    units_of_fuel = int(units_of_fuel)

    tanks = int(tanks)


    capacities = sys.stdin.readline().rstrip().split(' ')
    contents = [0 for i in range(len(capacities))]
    not_full = tanks
    highest_fill = 0

    while units_of_fuel >= not_full:
        for i in range(tanks):
            if contents[i] != int(capacities[i]):
                contents[i] += 1
                units_of_fuel -= 1
                
                if contents[i] == int(capacities[i]):
                    not_full -= 1
        highest_fill += 1
    
    if units_of_fuel != 0:
        GCD = math.gcd(units_of_fuel,not_full)
        denominator = not_full // GCD
        fill = highest_fill * denominator +  units_of_fuel // GCD
        for i in range(len(contents)):
            if int(contents[i]) != int(capacities[i]):
                contents[i] = f"{fill}/{denominator}"

        
    contents = [str(i) for i in contents]
    print(" ".join(contents))
