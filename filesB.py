fhand = open('mboxshort.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count: ', count)

#startswith()
fhand = open('mboxshort.txt')
for line in fhand:
    if line.startswith('From: '):
        print(line)

#rstrip()
fhand = open('mboxshort.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        
fhand = open('mboxshort.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#With input()     
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print ('There were', count, 'subject lines in', fname)

#try and except
fname = input('Enter the file name: ')
try: 
    fhand = open(fname)
except: 
    print('File cannot be opened: ', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count += 1
print ('There were', count, 'subject lines in', fname)