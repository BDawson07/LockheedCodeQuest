import sys
import math
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

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    converting = int(sys.stdin.readline().rstrip())
    for i in range(converting):
        temp, typeCF = sys.stdin.readline().rstrip().split(" ")
        C = 0
        F = 0
        if typeCF == "C":
            C = float(temp)
            F = ((C * 9 / 5)*10e7 + 32*10e7)/10e7
            print(f"{temp} C = {round_half_up(F,1)} F")
        else:
            F = float(temp)
            C = ((F*10e7 - 32*10e7)/10e7 * 5 / 9) 
            print(f"{temp} F = {round_half_up(C,1)} C")
