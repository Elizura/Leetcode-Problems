class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        prevPlant, ans = 0, 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            ans = max(ans, (grow + plant + prevPlant))
            prevPlant += plant
        return ans