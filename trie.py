class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.
        self.word_finished = False


def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the current `node`
        for child in node.children:
            if child.char == char:
                # Point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Word was added. Mark the last node as the end of a word.
    node.word_finished = True


def dfs(node, res_word: str, pos_words: list):
    # Return first 5 matching words
    if len(pos_words) >= 5:
        return
    # If such word exists, add it to the result array
    if node.word_finished:
        pos_words.append(res_word)

    # Loop through node's children and recursively call dfs() for each of them
    for child in node.children:
        dfs(child, res_word + child.char, pos_words)


def find_prefix(root, prefix: str):
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then find all possible words with this prefix
    """
    node = root
    possible_words = []
    result_word = prefix
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return 'Nothing found for your search'
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return 'Nothing found for your search'

    # We found the matching prefix
    # Make the depth first search for the child nodes to find all possible words
    dfs(node, result_word, possible_words)

    return possible_words
