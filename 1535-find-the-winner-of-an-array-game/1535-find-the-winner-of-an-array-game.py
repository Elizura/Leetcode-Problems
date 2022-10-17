class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:   
        left, wins = 0, 0
        N = len(arr)
        if k >= N: return max(arr)
        if k == 1: return max(arr[0], arr[1])
        for right in range(1, N):
            if arr[left] > arr[right]:
                wins += 1
                if wins == k: return arr[left]
            elif arr[right] > arr[left]:
                left = right
                wins = 1    
        return max(arr)
                
        # dic = defaultdict(int)
        # left, right = 0, 1
        # N = len(arr)
        # if k >= N: return max(arr)
        # while right < N:
        #     if arr[left] > arr[right]:
        #         dic[arr[left]] += 1
        #     else:
        #         dic[arr[right]] += 1
        #         left = right
        #     if dic[arr[left]] == k:
        #         return arr[left]
        #     right += 1
        #     if right >= N: right %= N