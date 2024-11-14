s = "([])"
stack = []


for char in s:
    if char in '([{':
        stack.append(char)
    elif not stack:
        print(False)
    elif char == ')':
        if stack.pop() != '(':
            print(False)
    elif char == ']':
        if stack.pop() != '[':
            print(False)
    elif char == '}':
        if stack.pop() != '{':
            print(False)
if stack:
    print(False)
print(True)