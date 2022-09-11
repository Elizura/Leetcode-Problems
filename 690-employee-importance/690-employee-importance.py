"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        def dfs(idx):
            nonlocal ans
            for i in employees:
                if i.id == idx:
                    ans += i.importance
                    for j in i.subordinates:
                        dfs(j)
        dfs(id)
        return ans