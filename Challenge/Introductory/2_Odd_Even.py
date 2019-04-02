# The problem statement
# Task 
# Given an integer, , perform the following conditional actions:
#   If  is odd, print Weird
#   If  is even and in the inclusive range of  to , print Not Weird
#   If  is even and in the inclusive range of  to , print Weird
#   If  is even and greater than , print Not Weird
#   Input Format
#   A single line containing a positive integer, .
# Constraints
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

def check_input(value):
    output = value%2
    print('Checking for input : ' + str(value))
    if(output>0):
        print('Weird')
    elif((2<=value<=5 and output==0)  or (value>20 and output==0 )):  # Even Inclusive check 2<=value<=5
        print('Not Weird')
    elif(6<=value<=20 and output==0):
        print('Weird')
    else:
        print('even')


#Running Boundary Condition Checks
check_input(3)
check_input(20)
check_input(21)
check_input(2)
check_input(5)


#alternate function
def check_odd_even(value):
    check = {True: "Not Weird", False: "Weird"}  # Declared a dictionary object
    print(check[value%2==0 and (value in range(2,6) or value >20)])

#Running Boundary Conditions
check_odd_even(3)
check_odd_even(20)
check_odd_even(29)
check_odd_even(24)