'''
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
'''
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    answer_strings = []
    for problem in problems:
        parts = problem.split(" ")
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operand = parts[0]
        second_operand = parts[2]
        operator = parts[1]

        first_operand_spaces = " " * (4 - len(first_operand))
        second_operand_spaces = " " * (4 - len(second_operand))
        operator_spaces = " " * (5 - len(operator))
        problem_spaces = " " * (7 - max(len(first_operand), len(second_operand)))

        first_line = first_operand_spaces + first_operand + problem_spaces
        second_line = operator + operator_spaces + second_operand_spaces + second_operand
        third_line = "-" * len(first_operand + problem_spaces + operator + operator_spaces + second_operand_spaces)
        
        arranged_problems += first_line + "    "
        answer_strings.append(str(eval(problem)))

    arranged_problems = arranged_problems.strip()
    arranged_problems += "\n" + second_line + "\n" + third_line

    if show_answers:
        answers = "    ".join(answer_strings)
        arranged_problems += "\n" + answers
    
    return arranged_problems
