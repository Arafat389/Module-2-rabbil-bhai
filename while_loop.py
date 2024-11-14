# while loop over list

fruits = ["apple","banana","mango","cherry"]
index = 0
while index<len(fruits):   # while loop index and lenth bole dite hoi
    print(fruits[index])
    index +=1


 # while loop over string  

name = "arafat islam"
index = 0
while index<len(name):
    print(name[index])
    index +=1

# while loop over range

str =1
end = 11
while str<end:
    print("5 x",str,"=",5*str)
    str+=1

# while over break

fruits = ["apple","banana","mango","cherry"]
index = 0
while index<len(fruits):      # while loop index and lenth bole dite hoi
    if fruits[index]=="cherry":
        break   
    print(fruits[index])
    index +=1

# while over continue

counter =0
while counter<50:
    counter+=1
    if counter%2==0:
        continue
    print(counter)