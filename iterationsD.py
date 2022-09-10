'''
The counter variable counts how many times we execute
a loop. It starts at zero and we add one to it each
time through the loop. 
'''

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

'''
The sum variable starts at zero and we add value
to the sum each time through the loop. 
'''
zork = 0
print('\nBefore', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

'''
Here we combine the counting and sum patterns and
divides when the loop is done.
'''

count = 0 
sum1 = 0
print ('\nBefore', count, sum1)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum1 = sum1 + value
    print (count, sum1, value)
print('After', count, sum1, sum1/count)

'''
This loop uses as if statement in the loop to 
catch/filter the value we are looking for.
'''
print('\nBefore')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

'''
If a value was found, we use a variable that starts
at False and is set to True as soon as we find what
we are looking for. But the value keeps printing 
True for the items in the list, even if they if it's not.
'''
found = False
print('\nBefore', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)


'''
To get the smallest number, we need to initiate
the variable with a bigger number and change the 
comparison operator.
'''
largest_so_far = -1
print('\nBefore', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

'''
Introduces a new type 'None' and keyword 'is'
'''
smallest = None 
print('\nBefore')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
