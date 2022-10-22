class Solution:
    def isValid(self, s: str) -> bool:
        print("The given sequence is - ", s)

        para_dict = {'(': ')', '[': ']', '{': '}'}
        stack = []

        if len(s)%2 != 0:
            print("Invalid input.")
            return False
        else:

#           s = [ ( ) ]
            for char in s:
                # Pushing all the open parenthesis in the stack
                if char in para_dict.keys():
                    stack.append(char)
                else:
                    # if you encounter a direct closing bracket without an opening return False
                    if stack == []:
                        return False

                    open_brac = stack.pop() # Pop open parenthesis

                    if char != para_dict[open_brac]:
                        return False

            return stack == []


if __name__ == "__main__":
    pair = input("Enter the sequence of Parentheses - ")
    a = Solution()
    a.isValid(pair)
