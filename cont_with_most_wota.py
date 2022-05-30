def maxArea(self, height: List[int]) -> int:
        max=0
        l=0
        r=len(height)-1
        i=0
        while i<=len(height) and r>l:
            m=min(height[l],height[r])
            a=m*(r-l)
            if a >max:
                max=a
            if m==height[l]:
                l+=1
            if m==height[r]:
                r-=1
                i+=1
        return max
