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

inputs = """1
6
www.google.com 128
www.dropbox.com 1424
www.cnn.com 142
codequest.global.lmco.com 212
www.australia.gov.au 4120
filetransfer.us.lmco.com 2186


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
    requests = int(automatic_inputs())
    
    further_review = []
    for i in range(requests):
        request,size = automatic_inputs().split(" ")
        if len(request.split(".")) >= 2:
            if request.split(".")[-2] == "lmco" and request.split(".")[-1] == "com":
                continue
            else:
                if int(size) > 1000:
                    further_review.append(" ".join([request,size]))
                    

    for i in further_review:
        print(i)