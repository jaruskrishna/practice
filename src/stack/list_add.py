def add_list():
    list1 = ['hel', 'Mor', 'Go']
    list2 = ['lo', 'ning', 'od']

    list_new = []
    print(len(list1))

    for i in range(len(list1)):
        list_new = list1[i] + list2[i]
        print(list_new)

if __name__ == '__main__':
    print("Adding two List")
    add_list()
