# Read an integer .
# Without using any string methods, try to print the following:
# Note that "" represents the values in between.
# Input Format
# The first line contains an integer .

def printAll(value):
    print(*range(1,value + 1), sep='')

printAll(10)