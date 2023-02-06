class DetectSquares:
    def __init__(self):
        self.d = Counter()
        self.x_coord = defaultdict(Counter)   # x -> all y coordinates with freqs

    def add(self, point):
        x, y = point
        self.d[x, y] += 1
        self.x_coord[x][y] += 1

    def count(self, point):
        x, y = point
        ans = 0
        for y2 in self.x_coord[x]:
            if y == y2: continue
            ans += self.d[x, y2] * self.d[x + y2 - y, y] * self.d[x + y2 - y, y2]
            ans += self.d[x, y2] * self.d[x + y - y2, y] * self.d[x + y - y2, y2]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)