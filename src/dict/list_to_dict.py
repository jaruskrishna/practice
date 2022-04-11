def convert():
    key = ['Ten', 'Twenty', 'Thirty', 'Forty', 'fifty']
    value = [10, 20, 30, 40, 50]

    new_dict = dict(zip(key, value))

    print(new_dict)

    return new_dict

def update_dict():
    new_dict.update({'sixty': 60})
    print(new_dict)


if __name__ == '__main__':
    new_dict = dict()
    new_dict = convert()
    update_dict()
