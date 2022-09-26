import re

def minion_game(string):
    # your code goes here

    # Stuart  Consonanta
    # Kevin Vowels

    # For kevin

    my_string = list(string)
    kevin, stuart = 0,0

    for i in range(len(my_string)):
        if my_string[i] in 'aeiou':
            kevin += len(my_string) - i
        else:
            stuart += len(my_string) - i
   
    if stuart > kevin:
        print ("Stuart {}" .format(stuart))
    else:
        print ("Kevin {}" .format(kevin))    

if __name__ == '__main__':
    s = input()
    minion_game(s)