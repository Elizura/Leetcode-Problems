class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:        
        dic = defaultdict(int)
        left, right = 0, 1
        N = len(arr)
        if k >= N: return max(arr)
        while right < N:
            if arr[left] > arr[right]:
                dic[arr[left]] += 1
            else:
                dic[arr[right]] += 1
                left = right
            if dic[arr[left]] == k:
                return arr[left]
            right += 1
            if right >= N: right %= N