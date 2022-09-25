def merge():

    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

    merge_dict = dict1.update(dict2)

    print(merge_dict)

if __name__ == '__main__':
    merge()
