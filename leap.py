def is_leap(year):
    if(year%400==0):
        leap=True
    elif(year%100==0):
        leap=False
    elif(year%4==0):
        leap=True
    else:
        leap=False
    
    return leap
a=int(input())
if(is_leap(a)==True):
    print("Leap")
else:
    print("Not leap")
