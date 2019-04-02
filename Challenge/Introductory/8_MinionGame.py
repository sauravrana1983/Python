# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

def minion_game(value):
    vowel = 'AEIOU'
    string_length = len(value)
    # Possible Number of substrings
    possible_substring = (string_length*(string_length+1))//2
    print(possible_substring)

    kevin_score = sum(string_length-i for i in range(string_length) if value[i].upper() in vowel)
    stuart_score = sum(string_length-i for i in range(string_length) if value[i].upper() not in vowel)
    
    if(kevin_score > stuart_score):
        print('Kevin ' + str(kevin_score))
    elif (stuart_score > kevin_score):
        print('Stuart ' + str(stuart_score))
    else:
        print('Draw')

minion_game('banana')