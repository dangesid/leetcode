# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.



def last_word(s):
    s = s.split()
    last_word = s[-1]
    return len(last_word)

s = "Hello World"
print(last_word(s))
