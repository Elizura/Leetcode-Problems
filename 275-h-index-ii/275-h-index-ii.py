class Solution:
    def hIndex(self, citations: List[int]) -> int:
        dic = {}
        for i in range(len(citations)):
            if citations[i] not in dic:
                dic[citations[i]] = len(citations[i:])
        h_index = 0
        for key in dic:
            if dic[key] >= h_index:
                if dic[key] < key:
                    h_index = dic[key]
                else:
                     h_index = key
        return h_index
