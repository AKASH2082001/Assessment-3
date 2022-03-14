person1=int(input("enter age of person1:"))
person2=int(input("enter age of person2:"))
person3=int(input("enter age of person3:"))
if person1>person2 and person1>person3:
    print("person1 is oldest")
elif person2>person1 and person2>person3:
    print("person2 is oldest")
else:
    print("person3 is oldest")
if person1<person2 and person1<person3:
    print("person1 is youngest")
elif person2<person1 and person2<person3:
    print("person2 is youngest")
else:
    print("person3 is youngest")