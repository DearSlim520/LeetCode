class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26

    def __init__(self):
        self.root = WordDictionary.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            cur = ord(ch) - ord('a')
            if not node.children[cur]:
                node.children[cur] = WordDictionary.TrieNode()
            node = node.children[cur]
        node.isEnd = True

    def search(self, word: str) -> bool:
        # have to use backtrack
        def dfs(node, i) -> bool:
            if i == len(word):
                return node.isEnd
            ch = word[i]
            if ch != '.':
                cur = ord(ch) - ord('a')
                if not node.children[cur]:
                    return False
                return dfs(node.children[cur], i + 1)
            else:
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)