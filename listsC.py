fhand = open('mboxshort.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print("Index 1, second item, e-mail: ", words[1])
    email = words[1]
    pieces = email.split('@')
    print ("Email username, mail server domain: ", pieces[0], pieces[1]) 

# ["From", "stephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"]
#     0                  1                 2      3     4        5         6            