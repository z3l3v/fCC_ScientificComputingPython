def arithmetic_arranger(problems, show=False):
          
  y = 0
  top_row, bottom_row, line, results = '', '', '', ''

  if len(problems) > 5:
    return "Error: Too many problems."
  
  while len(problems) > y:
    
      m = problems[y].split()
      top = m[0]
      bottom = m[2]
      operator = m[1]
        
      if len(top) < 5 and len(bottom) < 5:
          if top.isnumeric() and bottom.isnumeric():
            if operator == "+":
              result = str(int(top) + int(bottom))
            elif operator == '-':
              result = str(int(top) - int(bottom))
            else: 
              return "Error: Operator must be '+' or '-'."
          else:
              return "Error: Numbers must only contain digits."
      else: 
        return "Error: Numbers cannot be more than four digits."
        
      length = max(len(top), len(bottom)) + 2
      spaces = ' ' * 4      
        
      top_row += ' ' * (length - len(top)) + top + spaces
      bottom_row += operator + ' ' * (length - len(bottom) - 1) + bottom + spaces
      line += length * '-' + spaces
      results = ' ' * (length - len(result)) + result + spaces
      y += 1 
      
  if show:
        arranged = top_row.rstrip() + '\n' + bottom_row.rstrip() + '\n' + line.rstrip() + '\n' + results.rstrip()
  else:
        arranged = top_row.rstrip() + '\n' + bottom_row.rstrip() + '\n' + line.rstrip()

  return arranged