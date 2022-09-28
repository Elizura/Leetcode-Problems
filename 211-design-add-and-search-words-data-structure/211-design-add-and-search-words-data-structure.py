class Node:
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        
        
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node()
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            if idx >= len(word): return node.is_end
            elif word[idx] == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1): return True                    
            elif word[idx] in node.children:
                return dfs(node.children[word[idx]], idx + 1)
            else: return False
        
        return dfs(self.root, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)