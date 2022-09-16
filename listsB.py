total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total += value
    count += 1

average = total / count
print('Average: ', average)

numlist = list()
while True:
    inp1 = input('Enter a number: ')
    if inp1 == 'done' : break
    value = float(inp1)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average: ', average)