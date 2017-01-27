"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""

def ciborsegundo(x):
    vowels = "AaEeIiOoUu"
    cybersecure = ""
    for y in x:
        if y == 'a':
            cybersecure = cybersecure + "&"
        elif y == "A":
            cybersecure = cybersecure + "!"
        elif y == "E":
            cybersecure = cybersecure + "@"
        elif y == "e":
            cybersecure = cybersecure + "$"
        elif y == "I":
            cybersecure = cybersecure + "%"
        elif y == "i":
            cybersecure = cybersecure + "^"
        elif y == "O":
            cybersecure = cybersecure + "*"
        elif y == "o":
            cybersecure = cybersecure + "+"
        elif y == "U":
            cybersecure = cybersecure + "hackersbwar"
        elif y == "u":
            cybersecure = cybersecure + "?"
        else:
            cybersecure = cybersecure + y
    return cybersecure


            
print (ciborsegundo(" i appreciate consanants"))
