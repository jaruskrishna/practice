
def len_of_long_sub_string(line):
    charSet = set()
    l = 0
    res = 0

    print("The string is -", line)

    for r in range(len(line)):
        while line[r] in charSet:
            charSet.remove(line[l])
            l += 1
        charSet.add(line[r])
        res = max(res, r - l +1 )
    return res


if __name__ == '__main__':
    print("Finding the length of longest sub string.")
    line = "abcabcbb"

    res = len_of_long_sub_string(line)
    print("The num is", res)

    #Input: s = "abcabcbb" geeksforgeeks
    #Output: 3