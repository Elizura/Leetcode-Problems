class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ct = {}
        for i in range(len(s)):
            ct[s[i]] = i
        stack = []
        seen = set()
        for i in range(len(s)):
            if s[i] in seen: continue
            while stack and stack[-1] > s[i] and ct[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)