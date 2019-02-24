i1 = float(raw_input("enter first internal marks: "))
i2 = float(raw_input("enter second internal marks:"))
i3 = float(raw_input("enter third internal marks:"))
num = [i1, i2, i3]
small = min(num)
num.remove(small)
average = (num[0] + num[1])/2
print average 


