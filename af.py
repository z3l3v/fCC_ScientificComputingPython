def arithmetic_arranger(problems):
    
    if len(problems) > 5:
      print ("Error: Too many problems")
        
    top = []
    bottom = []
    operator = []
    list_of_lists = []
    
    for problem in problems:
        m = problem.split(" ")
        top.append(m[0])
        bottom.append(m[2])
        operator.append(m[1])
        list_of_lists.append(m)
        
    #print (list_of_lists)
        
    if "*" in operator or "/" in operator:
        print ("Error: Operator must be '+' or '-'.")
     
    for i in list_of_lists:
        if int(i[0]) == False or int(i[2]) == False:
            print ("Error: Numbers must only contain digits.")
            break
            
    for i in list_of_lists: 
        if len(i[0]) > 4 or len(i[2]) > 4:
            print ("Error: Numbers cannot be more than four digits.")
    
    top_row = '' 
    dashes = ''
    solutions = '' 
    values = list(map(lambda x: eval(x), problems))
    
    for i in range(0, len(list_of_lists), 2):
        length = max(len(list_of_lists[0]), len(list_of_lists[2])) + 2
        top_row += top[i].rjust(length)
        dashes += '-' * length
        solutions += str(values[i // 2]).rjust(length)
        if i != len(top) - 2:
            top_row = ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4
    print (top_row)
                    
    '''
    #length = max(len(top[0]), len (bottom[2])) + 2
    #width = length +2 
    
    line1 = f"{list_of_lists[0] :> {width}"
    line2 = f"{f'{lists_of_lists[1]} {lists_of_lists[2]}':>{width}}"
    dashes = '_' * width
    answers = str(int(lists_of_lists[0]} + int(list_of_lists[2]})
    a = f"{ans :>{width}}"
    
    for i in range(top):
    '''
        
    
    
        
        
    
arithmetic_arranger(["4212 + 89", "2 + 1", "23 + 45"])