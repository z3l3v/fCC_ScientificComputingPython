'''
^ Matches the beggining of a line
$ Matches the end of the line
. Matches any character
\s Matches whitespace
\S Matches any non-whitespace character
* Repeats a character zero or more times
*? Repeats a character zero or more times (non-greedy)
+ Repeats a character one ore more times
+? Repeats a character one or more times (non-greedy)
[aeiou] Matches a single character in the listed set
[^XYZ] Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
( Indicates where string extraction is to startswith) Indicates where string extraction is to end
'''

'''
We must import re
We can use re.search() to see if a string matches a regular
expression, similar to using the find() method for strings.
We cna use re.findall() to extract portions of a string that matches our 
regular expression, similar to combining find() and var[5:10]
'''

hand = open('mboxshort.txt')
for line in hand:
    line = line.rstrip()
    #if line.find('From:') >=0:
    if line.startswith('From:'):
        print(line)
        
import re 

print("\n Now with regular expressions")
hand = open('mboxshort.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('From:', line):
    if re.search('^From: ', line) :
        print(line)