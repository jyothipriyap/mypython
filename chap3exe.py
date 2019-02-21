#one:

hours= int(raw_input("enter hours: "))
rate = int(raw_input("eneter rate: "))
def pay(hours,rate):
    if hours > 40:
        extrahours = hours - 40
        extrapay= extrahours*rate*1.5
        totalpay= ((hours-extrahours)*rate)+extrapay
    else:
        totalpay= (hours*rate)
    return "pay: " + str(totalpay)
print pay(hours, rate)


#three

score = raw_input("eneter score: ")

try:
     score= float(score)
     if score < 0.6 and score >0:
         print 'F'
    elif score >= 0.6 and score <0.7:
         print 'D'
    elif score >= 0.7 and score < 0.8:
         print 'C'
    elif score >= 0.8 and score < 0.9:
         print 'B'
    elif score >= 0.9 and score < 1:
         print 'A'
    else:
        print "invalid"
except:
     print "invalid score"
    break
#three
try:
    h= int(raw_input("enetr hours: "))
    r = int(raw_input("enter rate: "))
except:
    print "please enter an int value"

print pay(h,r)



