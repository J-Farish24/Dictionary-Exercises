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



#Open message and create encrypted message file
infile = open(MESSAGE, 'r')
outfile = open(ENCRYPTED, 'w')
#Store message file's contents in an object
unencrypted_message = infile.read()
#Go through each letter of the message and write the corresponding code to the encrypted message file
for character in unencrypted_message:
    if character in codes:
        outfile.write(codes[character])
#Else for spaces, periods, and other symbols to be written 
    else:
        outfile.write(character)
#Close files
infile.close()
outfile.close()