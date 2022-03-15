def add(num1, num2):
    if(num1 or num2 < 0):
        sum  = num1 + num2
        print("Addition is ")
        print(sum)

    else:
        print("illegal experssion entered")

    print("*****END****")


if __name__ == '__main__':
    print("enter the number : \n")
    print("num1 :")
    num1 = int (input())
    print("num2 :")
    num2 = int(input())
    add(num1 , num2)