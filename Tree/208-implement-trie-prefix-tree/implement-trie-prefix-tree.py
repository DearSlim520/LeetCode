class Trie:
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            c = ord(ch)  - ord('a')
            if node.children[c] is None:
                node.children[c] = Trie.TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            c = ord(ch)  - ord('a')
            if node.children[c] is None:
                return False
            node = node.children[c]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            c = ord(ch)  - ord('a')
            if node.children[c] is None:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)