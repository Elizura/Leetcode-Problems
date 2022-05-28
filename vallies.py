def countingValleys(steps, path):
    height=0
    vallies=0
    for i in path:
        if i=='U':
            height+=1
            if height==0:
                vallies+=1
            
        if i=='D':
            height-=1
            
    return vallies
