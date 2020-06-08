import json


class Trie:
    """
    字典树
    """

    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


trie = Trie()
trie.insert('word')
trie.insert('words')
trie.insert('you')
trie.insert('yours')
trie.insert('yourdad')
# print(trie.root)
format_res = json.dumps(trie.root, sort_keys=True, indent=4, separators=(',', ':'))

print(format_res)
