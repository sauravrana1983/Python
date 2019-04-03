# You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
# For a better understanding of the problem, check the explanation.
# Input Format
# A single line of input consisting of the string .
# Output Format
# A single line of output consisting of the modified string.

# Sample Input ==> 1222311
# Sample Output ==> (1, 1) (3, 2) (1, 3) (2, 1)

# https://docs.python.org/2/library/itertools.html  ==> Read more about the tools

from itertools import groupby

data = input('Enter the string: ')
def compress_string(value):
    # for i,j in groupby(value):
    #     print(int(i))
    #     print(list(j))
    print(*[(len(list(c)), int(k)) for k, c in groupby(value)])

compress_string(data)