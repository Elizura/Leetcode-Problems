class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_indexes=[i for i in range(len(citations),0,-1)]
        l=0
        for i in range(len(citations)):
            if citations[l]>=h_indexes[l]:
                return h_indexes[l]
            l+=1            
        return 0 
        