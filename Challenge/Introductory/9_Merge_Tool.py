# Consider the following:
# A string, , of length  where .
# An integer, , where  is a factor of .
# We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:
# The characters in  are a subsequence of the characters in .
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given  and , print  lines where each line  denotes string .
# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen

# Sample Input ==> AABCAAADA  3 
# Sample Output ==> 
# AB
# CA
# AD

# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
# Syntax : 
# zip(*iterators)
# Parameters : 
# Python iterables or containers ( list, string etc )
# Return Value : 
# Returns a single iterator object, having mapped values from all the
# containers.

def remove_duplicates(data):
    s = set()  # A set is an unordered collection with no duplicate elements
    o =[]
    for i in data:
        if i not in s:
            s.add(i)
            o.append(i)
    return ''.join(o)   # using to join to concatenate string

def string_split(string, length):
    for t in [string[i:i+length] for i in range(0, len(string), length)]:   #using the range function to get the substring and string out
        print(remove_duplicates(t))
    for part in zip(*[iter(string)]*length):
        print(part)

string_split('AABCAAADA', 3)