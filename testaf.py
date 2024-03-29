def arithmetic_arranger(problems):
    
    if len(problems) > 5:
      return "Error: Too many problems"
        
    top = []
    bottom = []
    operator = []
    list_of_lists = []
    
    for problem in problems:
        m = problem.split(" ")
        top.append(m[0])
        bottom.append(m[2])
        operator.append(m[1])
        list_of_lists = top + bottom
    
        
    if "*" in operator or "/" in operator:
        print (operator)
        print ("Error: Operator must be '+' or '-'.")
      
    for i in list_of_lists:
        int(i)
        if i != int:
            print ("Error: Numbers must only contain digits.")
            print (i)
            print (type(i))
            break 
           
    for i in range(len(list_of_lists)):
        if len(list_of_lists[i]) > 4:
            print (list_of_lists[i])
            print ("Error: Numbers cannot be more than four digits.")
    
    top_row = '' 
    dashes = ''
    solutions = '' 
    values = list(map(lambda x: eval(x), problems))
    
    
arithmetic_arranger(["420 + 89", "2 + 1", "23 + 45", "69 + 3", "4056 + 4"])
    