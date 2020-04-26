def valid_parentheses(s_p):
    pd = { ']':'[', ')':'(', '}':'{'}
    stack = []
    for s in s_p:
        if s in pd:
            top_elem = stack.pop()
            if pd[s] != top_elem:
                return False
        else:
            stack.append(s)
    return not stack

print(valid_parentheses("()[]{}"))


def quotab(0)


