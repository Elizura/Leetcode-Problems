def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_arr(arr):
            for i in range(len(arr)-1):
                if (arr[i + 1] - arr[i]) != arr[1] - arr[0]:
                    return False
            return True
        ans = []
        for i in range(len(r)):
            newl = nums[l[i]:r[i]+1]
            newl.sort()
            print(newl)
            ans.append(check_arr(newl))
            newl=[]
        return ans
