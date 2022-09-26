if __name__ == '__main__':
    s = input()

    word =  list(s)
    print(word)

    # The any() function used if any one element is true it returns true. Passes through out the string.

    print(any(i.isalnum() for i in word))
    print(any(i.isalpha() for i in word))
    print(any(i.isdigit() for i in word))
    print(any(i.islower() for i in word))
    print(any(i.isupper() for i in word))
