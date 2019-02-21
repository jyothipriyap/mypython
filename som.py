s = 'a=b;c=d;e=f;g=h'
st = s.replace('=',',').replace(';',',')
for i in st:
    th = tuple(st.split(","))
print th





    









