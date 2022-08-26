class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
            steps=0
            while maxDoubles>0 and target>2:
                if target & 1: 
                    target-=1
                    steps+=1
                maxDoubles-=1
                target=target>>1
                steps+=1
            return steps+target-1

        # ans = 0
        # while target > 1 and maxDoubles:
        #     if not target % 2:
        #         target = target // 2
        #         maxDoubles -= 1                
        #     else:
        #         target -= 1                
        #     ans += 1
        # if target: return ans + target - 1
        # return ans
#         for i in range(len(heights) - 1):
#             height_difference = heights[i+1] - heights[i]
#             if height_difference <= 0:
#                 continue
#             heapq.heappush(heap, height_difference)
#             if len(heap) > ladders: 
#                 b = heapq.heappop(heap)
#                 bricks -= b
#             if bricks < 0:
#                 return i 
                
#         return len(heights)-1
        