# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    outline = ''
    with open(filename, 'r') as f:
      outline = f.read().lower().split()
      
    return outline


def count_words():
    text = read_file_content("./story.txt")
    
    words = dict()
    for word in text:
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] = words[word] + 1
            
    print(words)
    
count_words()