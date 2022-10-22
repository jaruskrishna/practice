def isPalindrome_str(n):
    print("The given string is - ", n)

    #reverse the string

    rev_n = ''.join(reversed(n))

    print("The reversed string is - ", rev_n)

    if (n == rev_n):
        print("The given string ", n , " is a palindrome.")
    else:
        print("Invalid string given.\n\n")

if __name__ == "__main__":
    print("\nHello to PALINDROME")
    word = input("Enter the value --- \n")
    isPalindrome_str(word)
    print("------Exit------")