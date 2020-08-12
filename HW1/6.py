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
def states(text, d: int):
    ans = []
    if len(text) < d:
        return ans
    if d == 0:
        ans.append(text)
        return ans
    else:
        if text[0] == 'A':
            for l in states(text[1:], d):
                ans.append(text[0] + l)
            for l in states(text[1:], d-1):
                ans.append('C' + l)
                ans.append('G' + l)
                ans.append('T' + l)
            return ans
        if text[0] == 'C':
            for l in states(text[1:], d):
                ans.append(text[0] + l)
            for l in states(text[1:], d-1):
                ans.append('A' + l)
                ans.append('G' + l)
                ans.append('T' + l)
            return ans
        if text[0] == 'G':
            for l in states(text[1:], d):
                ans.append(text[0] + l)
            for l in states(text[1:], d-1):
                ans.append('C' + l)
                ans.append('A' + l)
                ans.append('T' + l)
            return ans
        if text[0] == 'T':
            for l in states(text[1:], d):
                ans.append(text[0] + l)
            for l in states(text[1:], d-1):
                ans.append('C' + l)
                ans.append('G' + l)
                ans.append('A' + l)
            return ans
def atMostD(text, d:int):
    ans = []
    for i in range(d):
        ans.extend(states(text, i))
    ans.extend(states(text, d))
    return ans
#main
f = open("rosalind_ba1j.txt", "r")
text = f.readline()
text = text[0:-1]
k, d = [int(x) for x in next(f).split()]
f.close()
i = 0
root = TrieNode('*')
for i in range(len(text) - k + 1):
    word = text[i:i + k]
    for l in atMostD(word, d):
        add(root, l)
#reverse complement
str = ""
for ch in text:
    if ch == 'A':
        com = 'T'
    elif ch == 'C':
        com = 'G'
    elif ch == 'G':
        com = 'C'
    elif ch == 'T':
        com = 'A'
    else: com = ''
    str = com + str
for i in range(len(str) - k + 1):
    word = str[i:i + k]
    for l in atMostD(word, d):
        add(root, l)
g = open('output.txt', 'w')
for L in max_list:
    g.write(L + ' ')
g.close()