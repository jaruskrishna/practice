def listprint():

    list1 = ['apple', 'banana','mango']
    list2 = [1,2,3,4]

    print("List - 1\n",list1)
    print("\nList - 2\n",list2)

    list3 = zip(list1,list2)

    print("\nList - 3\n",list(list3))

#    for list,list2 in list3:
#        print("Fruit is {} and count is {} \n", list1, list2 )

if __name__ == '__main__':
    print("--Start--\n")
    listprint()