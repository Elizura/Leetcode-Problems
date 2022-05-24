class Solution:
    def sortSentence(self, s: str) -> str:
        a=[]
        sl=s.split(' ')
        b=[0]*len(sl)
        c=''

        for i in s:
            if i in '123456789':
                a.append(int(i)-1)
        for i in range(len(sl)):
            b[a[i]]=sl[i]

        e= ' '.join(map(str,b))
        for i in e:
            if i not in '123456789':
                c+=i
        return c