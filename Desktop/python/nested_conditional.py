# enter your age
# age is >= 18 come in and drink but. you must have wristband
# age is >= 18 come in and drink without wristband
# age is <18 no entry

age = input("please enter your age")
age = int(age)
if age:
    if age >= 21:
        print("come in and drink but. no need wrist band")
    elif age >= 18:
        print("come in and drink .required wristband")
    else:
        print("not entry")
else:
    print("age please")
