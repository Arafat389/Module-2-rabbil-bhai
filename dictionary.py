student ={
    "first_name": "arafat",
    "last_name":"islaam",
    "age":24,
    "email":"arafat15-3672@diu.edu.bd",
    "movile_number":"01773454389",
    "hight":5.9,
    "b":True

}
print(student)
print(student["age"])


# only keys
student ={
    "first_name": "arafat",
    "last_name":"islaam",
    "age":24,
    "email":"arafat15-3672@diu.edu.bd",
    "movile_number":"01773454389",
    "hight":5.9,
    "b":True

}
print(student.keys())

#only values

student ={
    "first_name": "arafat",
    "last_name":"islaam",
    "age":24,
    "email":"arafat15-3672@diu.edu.bd",
    "movile_number":"01773454389",
    "hight":5.9,
    "b":True

}
print(student.values())

#update

student ={
    "first_name": "arafat",
    "last_name":"islaam",
    "age":24,
    "email":"arafat15-3672@diu.edu.bd",
    "movile_number":"01773454389",
    "hight":5.9,
    "b":True

}
student.update({"name":"karim"})
print(student)
student.clear()
print(student)