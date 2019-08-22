# Remember you can only use the websites listed below: Good Luck!
# Allowed Websites:
# https://docs.python.org/3/
# https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
# https://en.wikipedia.org/wiki/Caesar_cipher

import curses


keycheck = 0
while keycheck < 1:
    key  = input('Key: ') # Get key for ceaser cypher
    try:
        val = int(key)
        print('key is valid integer')
        keycheck = 1
    except ValueError:
        print('key is not a number please try again')

charcheck = 0
while charcheck < 1:
    charInput = input('Text to be Chiphered: ')
    try:
        val = int(charInput)
        print('Input invalid please try again')
    except ValueError:
        print('Character input accepted. Chiphering text!')
        charcheck = 1
ciphered = []        
for x in charInput:
    intToascii = ''
    asciiToInt = ord(x)
    asciiToInt =+ val
    print(ord(x))
    intToascii = chr(asciiToInt)
    ciphered.append(intToascii)
print(*ciphered, sep = '')