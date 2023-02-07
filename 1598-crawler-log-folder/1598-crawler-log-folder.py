class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for log in logs:
            if ".." in log:
                steps -= steps > 0
            elif "." in log:
                continue
            else:
                steps += 1
        return steps if steps > 0 else 0