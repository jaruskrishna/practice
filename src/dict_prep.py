def one():

    dict1 = {'name' : 'jack' , 'age': 20, 'role' : 'employee'}
    dict2 = {'animal' : 'dog' , 'color' : 'white' , 'height' : 4}

    dict_merge = {**dict1 , **dict2}

    print("The merge is ", dict_merge)


def two():
    sampledict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    print(sampledict['class']['student']['marks']['history'])

#  Write a Python script to check whether
#  a given key already exists in a dictionary
def three():

    dict1 = {'name': 'jack', 'age': 20, 'role': 'employee'}
    dict2 = {'animal': 'dog', 'color': 'white', 'height': 4}

    dict_merge = {**dict1, **dict2}


# Write a Python script to generate and print a
# dictionary that contains a number
# (between 1 and n) in the form (x, x*x)
def three():
    n = int(input("Enter the number\n"))
    d = dict()

    for i in range(1 , n+1):
        d[i] = i * i
    print("The dictionary is \n", d)

# Write a Python program to check a dictionary is empty or not.
def four():
    dict1 = {'name': 'jack', 'age': 20, 'role': 'employee'}

    if bool(dict1):
        print("\n--Empty--\n")
    else:
        print("\n--Not Empty--")

if __name__ == '__main__':

    #one()
    #two()
    #three()
    four()
