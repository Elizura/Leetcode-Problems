class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = inf
        dic = {}
        for i in range(len(cards)):
            if cards[i] in dic:                                                    
                ans = min(ans, i - dic[cards[i]][-1] + 1)                    
                dic[cards[i]].append(i)
            else:
                dic[cards[i]] = [i]
        return -1 if ans == inf else ans
        # ans = 0
        # a = 0
        # for i in range(1, len(cards)):
        #     if card[i] == cards[a]:
        #         ans = min(ans, i - a + 1)
        #     a += 1
        # return ans