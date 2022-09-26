def print_formatted(number):
    # your code goes here
    for i in range(1,n+1):
        i = i
        a = oct(n).rjust(7)
        b = hex(n).upper().rjust(8)
        c = bin(n).rjust(22)

        print(i , a , b , c)

    #print(num)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)