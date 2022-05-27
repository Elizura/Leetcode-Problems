class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        output=[]
        l= Counter(changed)
        s=len(changed)
        if s % 2:
            return []
        for i in changed:
            if i==0 and l[0]>0:
                l[0]-=2
                output.append(0)
            elif i and i*2 and l[i]>0:
                l[i]-=1
                l[i*2]-=1
                output.append(i)
        return output if len(output)==s//2 else []
        