# Solution to challenge http://www.pythonchallenge.com/pc/return/bull.html 
# sequence 

# ----- 

def next_term(term):
    changedChar = False 
    firstChar = term[0]
    charCount = 1 
    output = ''
    for idx, c in enumerate(term[1:]):
        if c != firstChar or idx == len(term) - 1: 
            output += "{}{}".format(charCount, firstChar)
            charCount = 0 
            firstChar = c
        charCount += 1
    output += "{}{}".format(charCount, firstChar)
    return output

term = '1' 
for i in range(31): 
    if i == 30: print('el {} - Value {}'.format(i, len(term)))
    term = next_term(term)