fh = open("mboxshort.txt", "r")

for lx in fh:
    ly = lx.rstrip()
    print (ly.upper())