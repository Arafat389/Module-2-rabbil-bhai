#list location check

fruits = ["apple","banana","mango","cherry"]
print(fruits)
print(type(fruits))
print(id(fruits))   #list same mamory thake 
fruits.append("pynaple")
print(fruits)                 # so list mutable
print(id(fruits))    #list same mamory thake list kico add korar por


#append
fruits = ["apple","banana","mango","cherry","abc"]
fruits.append("pynaple")
print(fruits)


#insert

fruits = ["apple","banana","mango","cherry"]
fruits.insert(2,"mango")
print(fruits)

#remove

fruits = ["apple","banana","mango","cherry","abc"]
fruits.remove("mango")
print(fruits)

#clear

fruits = ["apple","banana","mango","cherry","abc"]
fruits.clear()
print(fruits)

#sort

list=[1,2,3,4,5,2,13,45,32,21,5,8,]
list.sort()   #assinding order
print(list)



#reverse
list=[1,2,3,4,5,2,13,45,32,21,5,8,]
list.sort()   # assinding order
list.reverse() # biporit dik theke  
print(list)

# list allow duplicate value

list=[1,2,3,4,5,2,13,45,32,21,5,8]
print(list)


#extend

list1 =[1,2,3,4,5]
list2 =[6,7,8,9,10]
list1.extend(list2)
print(list1)

# pop

list=[1,2,3,4,5,2,13,45,32,21,5,8,]
list.pop()    # last theke one value delete
print(list)

#count

list=[1,2,3,4,5,2,13,2,2,2,2,45,32,21,5,8,]
count = list.count(2)    # last theke one value delete
print(count)


#index

fruits = ["apple","banana","mango","cherry","abc"]
index = fruits.index("banana")

print(index)