# Ways to remove duplicates from list

def rem_dup(l):
    print("\nThe original list" , l)
    res = [*set(l)]

    print("\nAfer removinf duplicates", res)


def rem_dup_use_for(l):
    print("\nThe original list", (l))

    res = []
    [res.append(x) for x in l if x not in res]

    print("\nAfter removing the duplicates -", res)


if __name__ ==  '__main__':
    list1 = [100,21,22,1,1,3,5,4,21,100,22,334,4,6]
    dict = {1 : 'one', 2 : 'two', 3:'three'}
    set1 = {11,2,3,5,6,4,4}
    #rem_dup(list1)
    rem_dup_use_for(list1)