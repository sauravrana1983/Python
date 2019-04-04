
from itertools import combinations

def Iterables():
    length_of_str = int(input())            # 'Please enter the length of the string '
    actual_str= input().split(' ')          # 'Please enter space seperated character of string '
    length_of_substring = int(input())      # 'Please enter length of substring '

    C = list(combinations(actual_str, length_of_substring))
    F = list(filter(lambda c: 'a' in c, C))
    # for t in zip(*F):
    #     print(t)
    print("{0:.3}".format(len(list(F))/len(C)))

Iterables()
