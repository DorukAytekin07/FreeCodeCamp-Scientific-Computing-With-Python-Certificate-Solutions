def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = ["", "", ""]

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format"

        num1, operator, num2 = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'"

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits"

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"

        width = max(len(num1), len(num2)) + 2
        line1 = num1.rjust(width)
        line2 = operator + num2.rjust(width - 1)
        line3 = '-' * width

        arranged_problems[0] += line1 + '    '
        arranged_problems[1] += line2 + '    '
        arranged_problems[2] += line3 + '    '

    arranged_problems = '\n'.join(arranged_problems)

    if show_answers:
        for problem in problems:
            parts = problem.split()
            num1, operator, num2 = parts
            result = str(eval(problem))
            width = max(len(num1), len(num2), len(result)) + 2
            line4 = result.rjust(width)
            arranged_problems += '\n' + line4 + '    '

    return arranged_problems.rstrip()

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))
print(arithmetic_arranger(problems, True))
