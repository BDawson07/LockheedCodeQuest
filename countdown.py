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
import datetime

inputs = """4
11.30.2024 17:46:09|12.25.2024 07:02:28
01.10.2026 14:15:13|01.01.2027 15:25:20
03.12.2025 23:59:46|01.01.2026 11:31:38
05.05.2024 05:09:43|07.04.2024 04:10:50
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
    ###Write the logic for each Sample###

    #sample input  MONTH.DAY.YEAR HH:MM:S|MONTH.DAY.YEAR HH:MM:S
    date1,date2 = sys.stdin.readline().rstrip().split("|")


    #DATE1
    date, time = date1.split(" ")

    MM,DD,YY = date.split(".")   
    HH,M,S = time.split(":")
    
    date1 = datetime.datetime(int(YY) ,int(MM) ,int(DD) ,int(HH) ,int(M) ,int(S) )

    #DATE1
    date, time = date2.split(" ")

    MM,DD,YY = date.split(".")
      
    HH,M,S = time.split(":")

    date2 = datetime.datetime(int(YY) ,int(MM) ,int(DD) ,int(HH) ,int(M) ,int(S) )

    date = date2 - date1
    days = date.days
    
    HH,MM,SS = str((date)).split(" ")[2].split(":")
    
    days_str  = "Days"
    hh_str  = "Hours"
    mm_str  = "Minutes"
    ss_str  = "Seconds"

    if int(days) == 1:
        days_str = "Day"
    if int(HH) == 1:
        ss_str = "Hour"
    if int(MM) == 1:
        mm_str = "Minute"
    if int(SS) == 1:
        ss_str = "Second"

    print(f"{days} {days_str} {HH} {hh_str} {MM} {mm_str} {SS} {ss_str}")

