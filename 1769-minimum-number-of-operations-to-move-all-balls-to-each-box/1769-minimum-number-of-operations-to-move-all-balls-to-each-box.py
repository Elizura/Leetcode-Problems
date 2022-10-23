class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        box_indexes = []
        for idx in range(N):
            if boxes[idx] == '1':
                box_indexes.append(idx)
        ans = []
        for i in range(N):
            operations = 0
            for j in range(len(box_indexes)):
                turns = abs(box_indexes[j] - i)
                operations += turns
            ans.append(operations)
        return ans