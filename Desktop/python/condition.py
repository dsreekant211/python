#<2 ticket is free
# 2-8 ticket cost 7rs
# 9-65 ticket cost 14rs
# >65 ticket is free
age  = input("enter the  age")
if int(age)>8 and int(age)<65:
    print("ticket cost is 14rs")
elif  (int(age)<2 or int(age)>65):
    print("ticket wil be free")
else:
    print("else ticket cost is 7rs")

