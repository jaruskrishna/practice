# Interview question:
# Decode an encoded string such as "3[a]2[bc]" into "aaabcbc".
#
# Hint:
# Use a stack to remember the previous string and repeat count when you see "[".

def decode (s):
    stack = []
    curr_string = ""
    curr_num = 0


    for char in s:
        print ("-----------STEP ", char)
        
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
            print("The Current NUmber now ", curr_num)

        elif char == '[' :
            stack.append((curr_string, curr_num))
            curr_string = ""
            curr_num = 0

        elif char == ']' :
            last_str, num = stack.pop()

            curr_string = last_str + (curr_string * num)

        else:
            curr_string += char

    return curr_string

if __name__ == '__main__':
    a = input("enter the String for decode -  ")
    print(decode(a))
              
              



