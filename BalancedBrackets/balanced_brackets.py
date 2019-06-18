def balanced_brackets(str):
# create a stack and add the opening brackets to it
# store list of opening brackets to be matched in the traversal
# when a closing bracket is being looked at, pop off the last value in the stack and compare
# return True or False if the brackets are balanced

    stack = []
    opening = ["[", "{", "("]
    closing = ["]", "}", ")"]

    for bracket in str:
        if bracket in opening:
            stack.append(bracket)
        if bracket in closing:
            comparer = stack.pop()
            if opening.index(comparer) == closing.index(bracket):
                continue
            else:
                return False
    
    return True

print(balanced_brackets('[]{}()'));   # should return true
print(balanced_brackets('[{[()]}]'));   # should return true
print(balanced_brackets('[({}}]'));   # should return false