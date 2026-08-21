# Interview question:
# Given a list of strings, group together the words that are anagrams of each other.
#
# Hint:
# Use the sorted word or a 26-character frequency tuple as the dictionary key.

from collections import defaultdict

def grana(words):
    anagram = defaultdict(list)
    print("The anagram - ", anagram)

    for word in words:
        sorted_word = "".join(sorted(word))
        #print("Each word - " sorted_word)

        anagram[sorted_word].append(word)

    return list(anagram.values())

if __name__ =='__main__':
    print("Hello Group Anagram")
    input_words = ['eat','ate','cat','tac','mat','mac']
    result = grana(input_words)
    print("Here is your Input - ", input_words)
    print("The Anagramed result - ", result)
