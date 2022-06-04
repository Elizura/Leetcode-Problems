def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate (temperatures):
            while stack and temp>stack[-1][0]:
                    temp_pop,i_pop=stack.pop()
                    output[i_pop]=i-i_pop
            stack.append([temp,i])
    
        return output
