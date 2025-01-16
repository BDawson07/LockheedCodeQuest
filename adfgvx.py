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
qct1o8
w0bdzk
4hpm3j
gs67ev
l92fxn
yau5ir
MARTIN
DDAGAVVXGFAAVAGFGDFVVFDDFV
1c62et
iljvm7
d8rgko
suabph
9y354z
fnxq0w
CODE
AFFDVGVDAFXXFFFGGGVFGVDXDGAAXGDAXD
3kcdqg
5iub1f
92me6a
h0l7ry
xto84s
znjwvp
QUEST
GVADDXDDDVAVFVXGFFGADAFFVXGVDVDVVGXDDGAVFGGFXVXG

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
    key = ['aa', 'ad', 'af', 'ag', 'av', 'ax', 
           'da', 'dd', 'df', 'dg', 'dv', 'dx', 
           'fa', 'fd', 'ff', 'fg', 'fv', 'fx', 
           'ga', 'gd', 'gf', 'gg', 'gv', 'gx', 
           'va', 'vd', 'vf', 'vg', 'vv', 'vx', 
           'xa', 'xd', 'xf', 'xg', 'xv', 'xx'
           ]
    FINALKEY = {}
    
    keyrows = []
    for i in range(6): 
        keyrows.append(list(sys.stdin.readline().rstrip().lower()))
        
    for i in range(0,6):
        for c in range(0,6):
            FINALKEY[key[0]] = keyrows[i][c]
            key.remove(key[0])
    ##FINALKEY WORKS###
    



    cipherKey = list(sys.stdin.readline().rstrip().lower())
    ord_cipherKey = cipherKey[:]
    ord_cipherKey.sort()

    cipher = list(sys.stdin.readline().rstrip().lower())
    
    SECTIONS = [[i,[]] for i in cipherKey]
    for i in range(len(SECTIONS)):
        SECTIONS[i].append(ord_cipherKey[i])

    while len(cipher) > len(cipherKey):
        for i in SECTIONS:
            i[1].append(cipher[0])
            cipher.remove(cipher[0])

    
    #FIRST THEY ARE SORTED ALPHABETICALY
    #WE THEN NEED TO GET RID OF CHARS THAT DONT HAVE A VALUE
    
    c_cipherKey = list(cipherKey)[:]
    while len(c_cipherKey) != len(cipher):
        c_cipherKey.remove(c_cipherKey[-1])
    c_cipherKey.sort()
    if len(cipher) != 0:
        for i in SECTIONS:
            if i[2] in c_cipherKey:
                i[1].append(cipher[0])
                cipher.remove(cipher[0])

    

    c_cipherKey = list(cipherKey)
    c_cipherKey.sort()
    for i in SECTIONS:
        i[0] = c_cipherKey[0]
        c_cipherKey.remove(c_cipherKey[0])



    NEW_SECTIONS = []
    
    while len(SECTIONS) > 0:
        for i in cipherKey:
            for c in SECTIONS:
                if c[0] ==  i:
                    NEW_SECTIONS.append(c[1])
                    SECTIONS.remove(c)
    

    
        
    
    
    NEW_STRING = ''
    for i in range(max([len(i) for i in NEW_SECTIONS])):
        for i in NEW_SECTIONS:
                if len(i) > 0:
                
                    NEW_STRING += i[0]
                    i.remove(i[0])
                

                

    NEW_NEW_STRING = ""
    for i in range(0,len(NEW_STRING),2):
        NEW_NEW_STRING += FINALKEY[f"{NEW_STRING[i]}{NEW_STRING[i+1]}"]


    print(NEW_NEW_STRING)
        



            


    