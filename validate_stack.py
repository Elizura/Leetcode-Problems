def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l=0
        r=0
        output=[]
        for i in range(2*len(pushed)):
            if (not output or output[-1]!=popped[r]) and l<len(pushed):
                output.append(pushed[l])
                l+=1
            elif output[-1]==popped[r] and r<len(popped):
                output.pop()
                r+=1
        return True if not output else False
