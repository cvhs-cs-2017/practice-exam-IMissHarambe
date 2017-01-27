def ciborsegundo(x):
    vowels = "AaEeIiOoUu"
    cybersecure = ""
    for y in x:
        if y == 'a':
            cybersecure = cybersecure + "Now"
        elif y == "A":
            cybersecure = cybersecure + "Look"
        elif y == "E":
            cybersecure = cybersecure + "At"
        elif y == "e":
            cybersecure = cybersecure + "This"
        elif y == "I":
            cybersecure = cybersecure + "Net"
        elif y == "i":
            cybersecure = cybersecure + "That"
        elif y == "O":
            cybersecure = cybersecure + "I"
        elif y == "o":
            cybersecure = cybersecure + "Just"
        elif y == "U":
            cybersecure = cybersecure + "Found"
        elif y == "u":
            cybersecure = cybersecure + "Whenisaygobereadytothrow"
        else:
            cybersecure = cybersecure + y
    return cybersecure



print (ciborsegundo("The lazy student never gets paid!"))
