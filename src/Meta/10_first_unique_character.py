# Interview question:
# GFind the Index of the First Occurrence in a String
#
# Hint:
# Count characters, then scan the string again to find the first count of 1.

def funiq(parent, child):

    i = j  = 0
    while i < len(parent) and j < len(child):
        start = i
        while i < len(parent) and j < len(child) and parent[i] == child[j]:
            i += 1
            j += 1

        if j == len(child):
            return 1
        j = 0 
        i = start + 1    
    return False
    #return parent.find(needle)


if __name__ == '__main__':
    print("Given a parent String and find the child string.")
    parent = 'surajkrishna'
    child = 'kri'
    result = funiq(parent, child)
    if result:
        print("Found")
    else:
        print("Not Found")



        # i 
        # surajkrishna
        # j
        # kri
        #
        #