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
30
1,200.00,
2,,
3,,
4,350.00,
5,,
6,,
7,,
8,100.00,
9,,50.00
10,,
11,,
12,400.00,
13,,
14,,
15,,
16,,
17,,
18,,
19,,
20,,
21,75.00,
22,,
23,,
24,,100.00
25,,
26,,
27,200.00,
28,,
29,,
30,,
31
1,300.00,
2,,
3,,
4,450.00,
5,,
6,,
7,,
8,100.00,
9,,50.00
10,,
11,,
12,800.00,
13,,
14,,
15,,
16,,
17,,
18,,
19,,
20,,
21,75.00,
22,,
23,,
24,,100.00
25,,
26,,
27,200.00,
28,,
29,,
30,,
31,,
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

for case in range(cases):
    float_go_away = 10000
    billing_cycle = int(sys.stdin.readline().rstrip())
    A = 0
    D = billing_cycle
    I = .18
    P = 12
    cost = 0

    #feteches each day report
    for i in range(billing_cycle):
        a,b,c = sys.stdin.readline().rstrip().split(",")
        if b != '':
            cost += float(b) * float_go_away
        if c != '':
            cost -= float(c) * float_go_away
        A += cost
    
    A /= float_go_away

    print(f"${round_half_up((A/D) * (I/P),2)}")
