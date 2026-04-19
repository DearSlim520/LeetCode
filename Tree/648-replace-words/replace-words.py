class Solution:
    class TrieNode:
        def __init__(self):
            self.val = None
            self.children = [None] * 26

    def __init__(self):
        self.root = self.TrieNode()
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        def insert(node: TrieNode, word: str, index: int):
            for ch in word:
                c = ord(ch) - ord('a')
                if node.children[c] is None:
                    node.children[c] = self.TrieNode()
                node = node.children[c]
            node.val = index

        def containsPrefix(node: TrieNode, word: str, dictionary: List[str]):
            for ch in word:
                c = ord(ch) - ord('a')
                if node.children[c] is None:
                    return word
                node = node.children[c]
                if node.val is not None:
                    return dictionary[node.val]
            return word

        # build the Trie tree
        for i in range(len(dictionary)):
            insert(self.root, dictionary[i], i)

        # search each word in the sentence
        res = []
        for word in sentence.split(' '):
            res.append(containsPrefix(self.root, word, dictionary))

        return ' '.join(res)