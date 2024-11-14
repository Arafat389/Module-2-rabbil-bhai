"""
1 ordered
2 ()
3 imutable
4 duplicate value allow


"""

#list location check

fruits = ("apple","banana","mango","cherry")
print(fruits)
print(type(fruits))
print(id(fruits))   #tuple same mamory thake na
fruits = ("apple","banana","mango")
print(fruits)                 # so tuple imutable
print(id(fruits))   

#count

fruits = ("apple","banana","banana","mango","banana","cherry")
index = fruits.count("banana")
print(index)

# index 
fruits = ("apple","banana","banana","mango","banana","cherry")
index = fruits.index("mango")
print(index)

fruits = ("apple","banana","banana","mango","banana","cherry")
index = fruits.index("banana")
print(index)

# tuple convert list

fruits = ("apple","banana","banana","mango","banana","cherry")
list1 =list(fruits)
print(list1)


fruits = ("apple","banana","banana","mango","banana","cherry")
fruits.clear()
print(fruits)