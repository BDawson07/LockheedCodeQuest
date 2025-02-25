"""
Date: 2-25-2025
Name: Website-layout
Authors: Dawson Barthelemy
CodeQuestLink: https://lmcodequestacademy.com/problem/website-layout
"""

#Neccicary libraries for all solutions
import sys
import math
import string

inputs = """2
3
0 20
50 100
70 40
5
10 20
20 30
30 40
40 50
50 60

"""


inputs = inputs.split("\n")

def automatic_inputs(value = None) -> str:
    return_value = inputs[0]
    inputs.remove(inputs[0])  #Fetches the first input and deletes it from being used further
    return return_value

            
class Rows:
    number = 0
    rows = []
    gaps = []


    
    @classmethod
    def reset(cls) -> None:
        """reset the class after each loop"""

        cls.number = 0
        cls.rows = []
        cls.gaps = []

    def __init__(self,start,length) -> None:
        """Define a new row. 
        The elements dont matter, just where it ends"""

        if length == 0:
            return  #no use creating the row
        Rows.number += 1
        self.end = start + length
        Rows.gaps.append([(0, start)])  #first gap created in this list
        Rows.rows.append(self)

    @staticmethod
    def doesFitExactly(start,length) -> float:
        """Used to find where objects will fit exactly.
        Returns a value to see if we need to loop through the code to find non perfect fits"""
        for i in Rows.rows:
            if i.end == start:
                i.end += length
                break
        else:
            
            #if the program breaks, a solution was not found
            return False
        
        #if it breaks, a solution was found
        return True
    @staticmethod
    def doesFitIsh(start,length):
        closest = 100000
        current_find = None
        for i in Rows.rows:
            if start - i.end > 0:
                if start - i.end < closest:
                    current_find = i
                    closest = start - i.end
        
        if current_find != None:
            
            current_find.end = start + length
            return
        else:
            Rows(start,length)
        
 
cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
  
    Rows.reset()
    ###Write the logic for each Sample###
    rows = []
    objects = []

    #how many objects
    count = int(sys.stdin.readline().rstrip())
    for i in range(count):
        objects.append(sys.stdin.readline().rstrip().split(" "))

    #int type conversion
    for i in range(len(objects)):
        objects[i] = [int(objects[i][0]), int(objects[i][1])]
            
    
    #sort the objects by their offset then by their length (least to greatest
    objects.sort()
    
    for i in objects:
        #finds exacts fits
        if not Rows.doesFitExactly(i[0],i[1]):
            
            Rows.doesFitIsh(i[0],i[1])


    print(Rows.number)



    
