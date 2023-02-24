class TweetCounts:

    def __init__(self):
        self.a = defaultdict(list)

    def recordTweet(self, tn: str, time: int) -> None:
        bisect.insort(self.a[tn], time)
    def getTweetCountsPerFrequency(self, freq: str, tn: str, startTime: int, endTime: int) -> List[int]:
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        i = startTime
        res = []
        while i <= endTime:
            j = min(i + delta, endTime+1)
            res.append(bisect_left(self.a[tn], j) - bisect_left(self.a[tn], i))
            i += delta
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)