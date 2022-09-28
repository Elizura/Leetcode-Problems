class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode("")
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)                
                node.children[char] = new_node
                node = new_node
        node.is_end = True
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else: return False
        return node.is_end

    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for char in wordDict:
            trie.insert(char)
        N = len(s)
        dp = [False for _ in range(N + 1)]
        dp[0] = True        
        
        for i in range(N + 1):
            for j in range(i):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
        return dp[-1]
        
        
        
        
        
        
        




class TrieNode:
    def __init__(self):
        self.child = {}
        self.terminal = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, w):
        n = len(w)
        head = self.root
        
        for i in range(n):
            if w[i] in head.child:
                head = head.child[w[i]]
            else:
                head.child[w[i]] = TrieNode()
                head = head.child[w[i]]
        
        head.terminal = True
    
    def search(self, w):
        n = len(w)
        head = self.root
        
        for i in range(n):
            if w[i] not in head.child:
                return False
            
            head = head.child[w[i]]
        
        return True if head.terminal else False
    
class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
        n = len(s)
        trie = Trie()
        for i in dic:
            trie.insert(i)

        dp = [False for _ in range(n+1)]
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
                    break

        return dp[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        