# You must determine whether a given expression has valid brackets. This means all the parentheses (), square brackets
# [] and curly brackets {} must be correctly paired & nested.
#
# The expression does not contain whitespace characters.
# Input
# A single line: expression.
# Output
# A single line: true if each kind of bracket (), [] and {} in expression are paired correctly, false otherwise.
# Constraints
# expression contains less than 2048 characters.
# Example
# Input
# {([]){}()}
# Output
# true
import re
expression = input()
expression = re.sub("[^][}{)(]+", "", expression)
if len(expression)%2==0:
    pairs = {'{':'}', '[':']', '(':')'}
    stack = []
    for e in expression:
        print(e)
        if e in pairs.keys():
            stack.append(e)
        elif stack and e in pairs[stack[-1]]:
            stack.pop()
        elif stack:
            break
        print(stack)

    if len(stack)==0:
        print('true')
    else:
        print('false')
else:
    print('false')