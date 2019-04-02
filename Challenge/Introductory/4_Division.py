# Task 
# Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .
# You don't need to perform any rounding or formatting operations.
# Input Format
# The first line contains the first integer a . The second line contains the second integer b .

def division(a,b):
    if(b>0):
        print(a//b) # Integer division
        print(a/b)  #float division
    else:
        print('Divisor cannot be 0')

division(4,3)
division(4,0)