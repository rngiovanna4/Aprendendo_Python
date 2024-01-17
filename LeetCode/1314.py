"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it"""

def numberOfSteps(num: int) -> int:
        if num == 0:
            return num
        if num%2 == 0:
            return 1 + numberOfSteps(num//2)
        else: 
            return 1 + numberOfSteps(num-1)
        
print(numberOfSteps(14)) #The result need to be equal 6
