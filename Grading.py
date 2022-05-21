def gradingStudents(grades):
    # Write your code here
    a=[]
    for i in grades:
        if i< 38 or i%5==0:
            a.append(i)
        elif i%5==4:
            a.append(i+1)
        elif i%5==3:
            a.append(i+2)
        else:
            a.append(i)
    return a
