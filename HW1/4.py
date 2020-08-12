from typing import Tuple
max_list = []
max_occur = 0
class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
        self.depth = 0
def add(root, word: str):
    global max_occur, max_list
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            new_node.depth = node.depth + 1
            node.children.append(new_node)
            node = new_node
        if node.depth == k:
            if node.counter > max_occur:
                max_occur = node.counter
                max_list = [word]
            elif node.counter == max_occur:
                max_list.append(word)
    node.word_finished = True
#main
f = open("rosalind_ba1b.txt", "r")
s = f.readline()
s = s[0:-1]
k = f.readline()
k = k[0:-1]
k = int(k)
f.close()
i = 0
root = TrieNode('*')
for i in range(len(s) - k + 1):
    word = s[i:i + k]
    add(root, word)
max_list.sort()
g = open('output.txt', 'w')
for L in max_list:
    g.write(L + ' ')
g.close()
#trie structure code in this homework is adapted from https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1