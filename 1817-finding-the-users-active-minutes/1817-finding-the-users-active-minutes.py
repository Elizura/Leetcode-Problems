class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        m = defaultdict(set)
        for user, minute in logs:
            m[user].add(minute)        
        result = [0] * k
        for user_minutes in m.values():
            uam = len(user_minutes)            
            result[uam-1] += 1
        return result