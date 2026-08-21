# Interview question:
# Given a string containing brackets, determine if every opening bracket is closed in the correct order.
#
# Hint:
# Use a stack and check that each closing bracket matches the most recent opening bracket.

def paran(s):
    main = {")": "(", "}": "{", "]": "["}
    stack = []

    for i in s:
        if i in main:
            if stack and stack[-1] == main[i]:
                stack.pop()
            else:
                return False

        else:
            stack.append(i)
        

if __name__ =='__main__':
    print("Valid Parantheses - ")
    input1 = '()'
    input2 = '([)'
    result1 = paran(input1)
    print("This is not a valid - ", input1)
    result2 = paran(input2)
    print("This is not a valid - ", input2)