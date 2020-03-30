dict1 = {"student1":"Aman","student2":"Dheeraj","student3":"Mohit","student4":"Kanika","student5":"Amrita"}
a = sorted(dict1.items(),key=lambda x:x[1])
print(a)