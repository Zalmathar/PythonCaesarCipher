# Remember you can only use the websites listed below: Good Luck!
# Allowed Websites:
# https://docs.python.org/3/
# https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
# https://en.wikipedia.org/wiki/Caesar_cipher

import curses

key  = input('Key: ') # Get key for ceaser cypher
while True:
    try:
        check = int(key)
        print("Key is valid.")
        break
    except ValueError:
        print("Key is not a number! Please try again.")
        key = input('Key: ')
key = int(key)
text = input('Text to be encrypted: ')
cypher = ''
for x in text:
    if x.isupper():
        cypher =+ chr((((ord(x) + key) - 97) % 26) + 97)
    elif x.islower():
        cypher =+ chr((((ord(x) + key) - 65) % 26) + 65)
    else:
        cypher =+ x
print("Cyphered text: " + cypher)
exit()
