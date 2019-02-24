i1 = int(raw_input("enter first internal marks:"))
i2= int(raw_input("enter second internal marks: "))
i3 = int(raw_input("enter third internal marks: "))
try:
    if i1>i2 and i1>i3:
        maax = i1
    elif i2>i1 and i2>i3:
        maax = i2
    else:
        maax = i3
    if i2<i1<maax and i3<i1<maax:
        ma= i1
    elif i1<i2<maax and i3<i2<maax:
        ma = i2
    else:
        ma = i3
    average= (maax+ma)/2
    print average
except:
    print "please enter a number within 20"

