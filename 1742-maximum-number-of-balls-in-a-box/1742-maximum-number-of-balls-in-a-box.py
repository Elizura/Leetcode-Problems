class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = defaultdict(int)
        for num in range(lowLimit, highLimit + 1):
            s = sum(list(map(int, list(str(num)))))
            count[s] = count.get(s, 0) + 1
        return max([i for i in count.values()])
        