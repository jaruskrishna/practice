

#Sort the dictionary by key
from  collections import OrderedDict
def ordered_using_key(ll):

    print("\nBefore the Ordered -\n")
    res_ll = sorted(ll.items())
    print(res_ll)

    print("After Ordered - ")
    res_ol = OrderedDict(sorted(ll.items()))
    print(res_ol)

def retrieve(cc):

    print(cc.get('Japan'))

#Python program to find the sum of all items in a dictionary

def sum_dict(dd):

    res = 0
    for i in dd.values():
        res = res + i
    print("\nThe sum is - ", res)


#Convert Key-Value list Dictionary to List of Lists

def convert_dict_list(td):

    print("\nThe dictionary before merge - ")
    print(td)

    res = [[key] + val for key, val in td.items()]

    print("\nAfter the merge -")
    print(res)

    res1 = res[0] + res[1] + res[2]
    print("\nMerge the inner lists to one list -\n",  res1)


#Convert List to List of dictionaries

def list_t0_dict(self, ):
    pass



if __name__ == '__main__':
    print("Hello")

    dict1 = {
        'ravi': 10, 'rajnish': 9,
        'sanjeev': 5, 'yash': 2,
        'suraj': 32, 'inkul': 31,
        'aron' : 40, 'brandom': 42
            }
    #ordered_using_key(dict1)

    country_code = {'India': '0091',
                    'Australia': '0025',
                    'Nepal': '00977'}

    #retrieve(country_code)

    #sum_dict(dict1)

    test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

    convert_dict_list(test_dict)