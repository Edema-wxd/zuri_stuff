# Check if a word is an anagrams 
# Example:
# 

def find_anagrams(word_a, word_b):
    # check length
    # check if they have the same number of letters
    a = dict()
    b = dict()
    
    if len(word_a) == len(word_b):
        for letter in word_a:
            if letter not in a.keys():
                a[letter] = 1
            else:
                a[letter] = a[letter] + 1
                
        for letter in word_b:
            if letter not in b.keys():
                b[letter] = 1
            else:
                b[letter] = b[letter] + 1
        if a == b:
            return print(True)
        else:
            return print(False)
    
    else:
        return print(False)

find_anagrams("carrace","racecar")