
def operations(n):
    # Declaring an empty list.
    stack = n

    # Converting ito a list.
    stack_list = []
    stack_list = list(stack)

    print('Stack elements - {} ' .format(stack_list))

    # Popping out elements.
    stack_list.pop()
    stack_list.pop()

    print('Stack elements after pop - {} '.format(stack_list))

if __name__ == '__main__':
    print("Stack Program")
    n = str(input("Enter the elements as a list - "))
    operations(n)
