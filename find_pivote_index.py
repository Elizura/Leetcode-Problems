class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans=[0]
        for i in nums:
            ans.append(ans[-1]+i)
        ans_=[ans[-1]-nums[0]]
        for i in nums[1:]:
            ans_.append(ans_[-1]-i)

        i=0
        j=0

        while j<len(ans_):
            if ans[i]==ans_[j]:
                return i
            i += 1
            j += 1

        return -1
