def sortSentence(self, s: str) -> str:
        a=[]
        list_of_the_sentence =s.split(' ')
        b=[0]*len(list_of_the_sentence)
        Final_String=''

        for i in s:
            if i in '123456789':
                a.append(int(i)-1)
        for i in range(len(list_of_the_sentence)):
            b[a[i]]=list_of_the_sentence[i]

        e= ' '.join(map(str,b))
        for i in e:
            if i not in '123456789':
                Final_String+=i
        return Final_String
