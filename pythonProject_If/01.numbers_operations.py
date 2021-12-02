n1 = int(input())
n2 = int(input())
oper = input()

result = None
out = ""

if n2 == 0 and (oper == '/' or oper == '%'):
    out = f"Cannot divide {n1} by zero"
elif oper == '/':
    result = n1 / n2
    out = f"{n1} {oper} {n2} = {result:.2f}"
elif oper == '%':
    result = n1 % n2
    out = f"{n1} {oper} {n2} = {result}"
else:
    if oper == '+':
        result = n1 + n2
    elif oper == '-':
        result = n1 - n2
    elif oper == '*':
        result = n1 * n2

    number = 'even' if result % 2 == 0 else 'odd'

    out = f"{n1} {oper} {n2} = {result} - {number}"

print(out)
