class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            hash= {n:i for i,n in enumerate(nums1)}
            stack=[]
            ans=[-1]*len(nums1)
            for i,num in enumerate(nums2):
                while stack and num > stack[-1][0]:
                    pop_no, pop_i = stack.pop()
                    ans[hash[pop_no]] = num
                if num in hash:
                    stack.append([num,i])
            return ans