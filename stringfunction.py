s= 'a=b;c=d;e=f;g=h'
print(s)
def convert(s= 'a=b;c=d;e=f;g=h'):
    n1=s[0]
    n2=s[2]
    n3=s[4]
    n4=s[6]
    n5=s[8]
    n6=s[10]
    n7=s[12]
    n8=s[14]
    s1='("'+n1+'","'+n2+'")'
    s2='("'+n3+'","'+n4+'")'
    s3='("'+n5+'","'+n6+'")'
    s4='("'+n7+'","'+n8+'")'

    print(s1,',',s2,',',s3,',',s4)
convert(s)




