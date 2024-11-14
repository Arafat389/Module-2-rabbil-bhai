"""
1 unordered
2 {}
3 mutable
4 duplicate value not allow


"""

#list location check

fruits = {"apple","banana","mango","cherry"}
print(fruits)
print(type(fruits))
print(id(fruits))   #set same mamory thake 
fruits.add("mango")
print(fruits)                 # so tuple mutable
print(id(fruits)) 

# clear
fruits = {"apple","banana","mango","cherry"}
fruits.clear()
print(fruits)

# remove
fruits = {"apple","banana","mango","cherry"}
fruits.remove("apple")
print(fruits)

# update
fruits = {"apple","banana","mango","cherry"}
fruits.update(['a','b','c'])
print(fruits)

# update
fruits = {"apple","banana","mango","cherry"}
fruits.update('a','b','c')
print(fruits)

