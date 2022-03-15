#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    
    # Check of uppercase and lower case and convert them to vice-versa.
    sentence_case = sentence.swapcase()
   
    # Split into a list.
    words = sentence_case.split()
    print(words)

    # Reverse and the joining the list into a string.
    reverse = ' '.join(reversed(words))
    print(reverse)
    
    # Return a string.
    return reverse
    
if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sentence = input()
    result = reverse_words_order_and_swap_cases(sentence)
    # fptr.write(result + '\n')
    # fptr.close()
