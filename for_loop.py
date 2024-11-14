# for loop over list

fruits = ["apple","banana","mango","cherry"]
for i in fruits:
    print(i)

fruits = ["apple","banana","mango","cherry"]
for item in fruits:
    print(item)

# for loop over string

name= "Arafat Islam"    
for str in name:
    print(str)

#for loop over range

for i in range (1,11):
    print("5 x", i, "=", 5*i)

# for over break

fruits = ["apple","banana","mango","cherry"]
for item in fruits:
    if item == "mango":
        break
    print(item)

fruits = ["apple","banana","mango","cherry"]
for item in fruits:
    if item == "mango":
        break
    print(item)

name= "Arafat Islam"    
for str in name:
    if str == "l":
        break
    print(str)


# for over continue

fruits = ["apple","banana","mango","cherry"]
for item in fruits:
    if item == "mango":
        continue
    print(item)  

name= "Arafat Islam"    
for str in name:
    if str == "l":
        continue
    print(str)