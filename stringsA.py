fruit = 'banana' 
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


word = 'banana'    
count = 0
for letter in word:
    if letter == 'a':
        count = count +1
print('\n', count)