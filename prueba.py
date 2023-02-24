def arithmetic_arranger(problems):
    problems = " "
    if len(problems) > 5:
        print ("Error: Too many problems.")
    
    arranged_problems = ""
    pieces = []
    answers = ""
    
    first = []
    second = []
    operator = []
    
    for problem in problems:
        parts = problem.split(" ")
        print(parts)
        #first.append(parts[0])
        #second.append(parts[2])
        #operator.append(parts[1])
        if parts[1] not in ["+", "-"]:
            print(parts[1])
            print ("Error: Operator must be '+' or '-'.")
        if not parts[0].isdigit() or not parts[2].isdigit():
            print ("Error: Numbers must only contain digits.")
        for i in range(len(parts[0])):
          if len(parts[0]) > 4 or len(parts[2]) > 4:
            print ("Error: Numbers cannot be more than four digits.")
        
        print (parts)   
    #first = parts[0].rjust(4)
    #second = parts[2].rjust(4)
    #operator = parts[1].rjust(3)
          
    #max_length = max(len(first), len (second))
          
    #formatted_operand1 = first.rjust(max_length)
    #formatted_operand2 = second.rjust(max_length)
          
    #output = formatted_operand1 + "    \n" + operator + " " + formatted_operand2 + "    \n" + "-" * (max_length + 2)
    #answers += output
    #print(pieces)
      
arithmetic_arranger(["32 + 698", "32 + 698", "3801 - 2", "45 + 43", "123 + 49"])