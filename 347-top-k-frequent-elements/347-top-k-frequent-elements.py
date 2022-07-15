class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        a= sorted(d.items(), key=lambda x:x[1],reverse=True)
        a= dict(a)
        a= list(a)
        return a[:k]