FILE = 'info_security.txt'
codes = {'A': '!', 'a': '1', 'B': '@', 'b': '2', 'C': '#', 'c': '3', 'D': '$', 'd': '4', 'E': '%', 'e': '5', 'F': '^', 'f': '6',
 'G': '&', 'g': '7', 'H': '*', 'h': '8', 'I': '(', 'i': '9', 'J': ')', 'j': '0', 'K': '_', 'k': '-', 'L': '+', 'l': '=', 'M': '~', 'm': '`',
 'N': '{', 'n': '[', 'O': '}', 'o': ']', 'P': '|', 'p': '\\', 'Q': ':', 'q': ';', 'R': '"', 'r': "'", 'S': '<', 's': ',', 'T': '>', 't': 'L',
 'U': '?', 'u': '/', 'V': 'A', 'v': 'a', 'W': 'B', 'w': 'b', 'X': 'C', 'x': 'c', 'Y': 'D', 'y': 'd', 'Z': 'E', 'z': 'e' }




infile = open(FILE, 'r')
unencrypted_message = infile.read()
for character in unencrypted_message:
    if character in codes:
        print(codes[character], end = '')
    else:
        print(character, end = '')