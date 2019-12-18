import time

import binary_search as Binary
import trie as Trie

# Around 61k words
dictionary_file = open("usa.txt", "r")
dictionary_file2 = open("usa.txt", "r")
# Around 195k words
# dictionary_file = open("english3.txt", "r")
# dictionary_file2 = open("english3.txt", "r")

if __name__ == "__main__":
    root = Trie.TrieNode('*')

    # Approximate search time - 5 - 6 ms
    # Search time depends on the length of the prefix and number of possible endings
    for word in dictionary_file:
        word = word.strip()
        Trie.add(root, word)

    start_time = time.time()
    print(Trie.find_prefix(root, 'trick'))
    end_time = time.time() - start_time
    print(end_time)

    # Approximate search time - 4 - 5 ms on both files
    dictionary_arr = dictionary_file2.read().splitlines()
    dictionary_arr.sort()
    start_time = time.time()
    print(Binary.binary_search(dictionary_arr, 'trick'))
    end_time = time.time() - start_time
    print(end_time)
