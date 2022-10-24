class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = 0
        dic = {0: 1}
        ans = 0
        for num in nums:
            pref += num
            if (pref - goal) in dic:
                ans += dic[pref - goal]                
            dic[pref] = dic.get(pref, 0) + 1
        return ans
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        	presum=ans=0
			store={}
			for n in nums:
				if presum in store: store[presum]+=1 
				else:store[presum]=1
				presum+=n
				if presum-goal in store: 
					ans+=store[presum-goal]      

			return ans
            [0, 1, 0, 1, 1]
            [0, 1, 1, 2, 3]
            {0: 1
             1: 2
             2: 1
             3: 1}
        '''
        pref = 0
        ans = 0
        left, right = 0, 0
        N = len(nums)        
        for right in range(N):
            pref += nums[right]
            while pref > goal:
                pref -= nums[left]
                flag = False
                while pref == goal:  
                    flag = True
                    ans += 1       
                    pref -= nums[left]
                    left += 1
                if not flag:
                    left += 1            
            if pref == goal:
                ans +=  1
        return ans