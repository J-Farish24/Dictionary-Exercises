#File Constants
MESSAGE = 'info_security.txt'
ENCRYPTED = 'info_security_encrypted.txt'

#Code Dictionary
codes = {'A': 'Z', 'a': 'z', 'B': 'Y', 'b': 'y', 'C': 'X', 'c': 'x', 'D': 'W', 'd': 'w', 'E': 'V', 'e': 'v', 
'F': 'U', 'f': 'u','G': 'T', 'g': 't', 'H': 'S', 'h': 's', 'I': 'R', 'i': 'r', 'J': 'Q', 'j': 'q', 
'K': 'P', 'k': 'p', 'L': 'O', 'l': 'o', 'M': 'N', 'm': 'n','N': 'M', 'n': 'm', 'O': 'L', 'o': 'l', 
'P': 'K', 'p': 'k', 'Q': 'J', 'q': 'j', 'R': 'I', 'r': 'i', 'S': 'H', 's': 'h', 'T': 'G', 't': 'g',
'U': 'F', 'u': 'f', 'V': 'E', 'v': 'e', 'W': 'D', 'w': 'd', 'X': 'C', 'x': 'c', 'Y': 'B', 'y': 'b', 
'Z': 'A', 'z': 'a' }




infile = open(MESSAGE, 'r')
outfile = open(ENCRYPTED, 'w')
unencrypted_message = infile.read()
message = ''
for character in unencrypted_message:
    if character in codes:
        print(codes[character], end = '')
        outfile.write(codes[character])
        message += codes[character]
    else:
        print(character, end = '')
        outfile.write(character)
        message+= character
infile.close()
outfile.close()



print('\n\n\n')
values = codes.values()
decoder = {}
for value in values:
    for key in codes:
        if codes[key] == value:
            decoder[value] = key
for character in message:
    if character in decoder:
        print(decoder[character], end = '')
    else:
        print(character, end = '')