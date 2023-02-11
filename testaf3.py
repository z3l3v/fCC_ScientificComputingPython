def arithmetic_arranger(problems, show_answer=False):
  if len(problems) > 5:
        return "Error: Too many problems."
    
  arranged_problems = ""
  answers = []
  for problem in problems:
      parts = problem.split(" ")
      if parts[1] not in ["+", "-"]:
          return "Error: Operator must be '+' or '-'."
      if not parts[0].isdigit() or not parts[2].isdigit():
          return "Error: Numbers must only contain digits."
      if len(parts[0]) > 4 or len(parts[2]) > 4:
          return "Error: Numbers cannot be more than four digits."
        
      first = parts[0].rjust(4)
      second = parts[2].rjust(4)
      operator = parts[1].rjust(3)
      line = " " * 7
      arranged_problems += f"{first}    {operator} {second}\n{line}\n"
      if show_answer:
          answer = str(eval(problem))
          answers.append(answer.rjust(4))
          arranged_problems += f"{answers[-1]}\n"
          arranged_problems += "-" * len(answers[-1]) + "\n"
  if show_answer:
      arranged_problems += "\n".join(answers)
  
  return arranged_problems.strip()