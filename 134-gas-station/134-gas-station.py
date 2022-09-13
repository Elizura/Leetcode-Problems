class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        dif = [gas[i] - cost[i] for i in range(len(gas))]
        ans = -1
        pref = 0
        for i in range(len(dif)):
            pref += dif[i]
            if pref < 0:
                pref = 0
                ans = -1
            else:
                if ans == -1:
                    ans = i                
        return ans
        
        
        
        # @lru_cache
        # def dfs(st, idx, curg, rounded):
        #     if idx == len(gas):
        #         idx = idx % len(gas)
        #         rounded = True
        #     if rounded and idx == st: return True
        #     curg += gas[idx]
        #     if cost[idx] > curg: return False
        #     return dfs(st, idx + 1, curg - cost[idx], rounded)
        # for i in range(len(gas)):
        #     if dfs(i, i, 0, False) == True: return i
        # return -1