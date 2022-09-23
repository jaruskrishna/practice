def rev_string(ll):
    b = ll[::-1]
    print(b)

def rev_conti_string(lb):

    #First split the words.
    ab = lb.split()
    print(ab)

    #Reverse and then join.
    res = ' '.join(reversed(ab))

    print(res)


#Check if two strings are anagram

def anagram(x,y):
    if (sorted(x) == sorted(y)):
        print("The strings", x ,'and',y   ,"are Anagram")
    else:
        print("They arent Anagram")


################################

#How do you find duplicate characters in a given string?

################################
from collections import defaultdict

def print_duplicates(st):

    #count = dict()
    count = defaultdict(int)
    for i in range(len(st)):
        count[st[i]] += 1
        #print(st[i], count[st[i]] )

    for lt in count:
        if (count[lt] > 1):
            print(lt , "is repeated", count[lt])
        else:
            print(lt , "is occurred only", count[lt])


#How do you count a number of vowels and consonants in a given string?

def find_vowels_consonant(ll):

    ll_sp = [x for x in ll]
    print("\nThe given string is -  ", ll)
    print("After the split - \n", ll_sp)

    for i in range(len(ll_sp)):
        if ll_sp[i] in ['a','e','i','o','u']:
            print("The letter", ll_sp[i], "is a vowel")
        else:
            print("The letter", ll_sp[i], "is a consonant.")

#How do you find duplicate characters in a given string? (

from collections import defaultdict

def find_dup_char(f):

    print("The given string is - ", f)

    count = defaultdict(int)
    for i in range(len(f)):
        count[f[i]] += 1
        #print(i, count[i])

    for x in count:
        if count[x] > 1:
            #print("in if loop !!!!")
            print("The char repeated is ", x)
        else:
            print("Not repeated", x)



if __name__ == "__main__":
    #a = input("Enter the string to be reversed--\n")
    #rev_string(a)

    #b = input("Enter the continuous string ---\n")
    #rev_conti_string(b)

    #x = 'silent'
    #y = 'listen'

    #anagram(x,y)

    #st = 'test string'
    #print_duplicates(st)

    #line  = 'rguhaeixyz'
    #find_vowels_consonant(line)

    one = 'asdsee'
    find_dup_char(one)