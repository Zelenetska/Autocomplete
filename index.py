import timeit
import sys

import binary_search as Binary
import trie as Trie

# Around 61k words
dictionary_file = open("usa.txt", "r")
dictionary_file2 = open("usa.txt", "r")
# Around 195k words
# dictionary_file = open("english3.txt", "r")
# dictionary_file2 = open("english3.txt", "r")

root = Trie.TrieNode('*')
for word in dictionary_file:
    word = word.strip()
    Trie.add(root, word)

dictionary_arr = dictionary_file2.read().splitlines()
dictionary_arr.sort()


def trie_test():
    return Trie.find_prefix(root, 'appl')


def binary_test():
    return Binary.binary_search(dictionary_arr, 'appl')


if __name__ == "__main__":
    trie_times = timeit.repeat("trie_test()", setup="from __main__ import trie_test", repeat=5, number=1000000)
    binary_times = timeit.repeat("binary_test()", setup="from __main__ import binary_test", repeat=5, number=1000000)
    print('Trie search time: {}'.format(trie_times))
    print('Binary search time: {}'.format(binary_times))
