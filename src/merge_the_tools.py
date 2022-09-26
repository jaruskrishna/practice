def merge_the_tools(string, k):
    # your code goes here
    #length = len(string)
    # Divide the length by k 
    num = int(len(string) / k)
    #print(num)
    out = [(string[i:i+num]) for i in range(0, len(string), num)]
    #print(out)
    
    for i in range(len(out)):
        print(out[i])
        a = removeDupWithoutOrder(out(i))
        my_list[].append()

    print(my_list)

    
def removeDupWithoutOrder(str):
    return "".join(set(str))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
