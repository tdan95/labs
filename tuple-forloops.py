#  PYTHON TUPLES
mytuple = ("apple", "banan", "cherry") # round brackets ()
print(mytuple) # tuples are unchangeable meaning that it can't be removed added etc

mytuple2 = ("cheese", "cheese", "cheese") # allow duplicates
print("the lenght of the tuple is" , len(mytuple2)) #len() works

oneitem = ("item",) #  To create a tuple with only one item, you have to add a comma after the item
print(oneitem)

mytuple3 = tuple(("cheese", 12, True)) #don't forget about the double brackets when using a tuple()
print(mytuple3[0:2]) #index works

x = ("car", "plane", "motorcycle")
y = list(x)      
y[1] = "bicycle"  # the one way to change the values
x = tuple(y) # we do it like this because tuples are unchangebale
print(x)

# to add, remove we covert the tuple to list then do operation then again convert the list into tuple

mytuple4 = ("potato", "carrot")
oneitem2 = ("tomato",)
mytuple4 += oneitem2
print(mytuple4) # to add two tuples we do this

mytuple5 = ("apple", "pear", "banana")
(red, orange, yellow) = mytuple5 # assign a variable
print(red, orange, yellow)

mytuple6 = (1, 2, 3, 4, 5, 6, 7)
(red, orange, *yellow) = mytuple6 # asterisk use when the variables are less than the values 
print(red)
print(orange)
print(yellow) # it contains the rest of the item in a tuple

mytuple7 = ("apple", "banana")
mytuple7 *= 2 # you can double the tuple
print(mytuple7)


print ("---------------------------------------------------------------------------------------")



# PYTHON SETS
myset = {"apple", "banana", "pear"} #it is unoredered meaning that a it will pop up in ur terminal randomly
print(myset)

# you can add and remove the values

myset1 = {"apple", "banana", "apple"} # duplicates will be ignored 
print(myset1)

# set can contain mixed data types

myset2 = set(("apple", "banana", "pear")) #set() function to create a set from list
print(myset2)

for elements in myset2:
    print(elements) #for looping throught the set

# index doesn't work for set
# you can't change the value in a set
myset3 = {"apple", "banana", "cherry"}
myset3.add("orange")
print(myset3) #adds in random place

myset4 = {1, 2, 3}
testset = {4, 5, 6}
myset4.update(testset) # combines the sets but it also combines set to the other iterable object
print(myset4)

myset5 = {10, 20, 30, 40, 50}
myset5.remove(10) # 1st way to remove
myset5.discard(20) # 2nd way to remove
myset5.pop() # deletes random item
print(myset5)

myset6 = {1,2}
myset7 = {3, 4}
temp = {5,6}
myset8 = myset6.union(myset7) # new variables to use union
myset9 = myset8 | temp # it is alternative for union()
print(myset8)
print(myset9)



print("--------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------")


#   PYTHON DICTIONARIES
# it is like the map: key : value
# they are changeable and no duplicates
mydict = {
    "brand" : "Ford",
    "model" : "Mustsng",
    "year" : 1964
}
print(mydict)
print(mydict["brand"]) # we call the key and it shows its value

mydict1 = {
    "brand" : "Toyota",
    "model" : "Camry",
    "year" : 2021,
    "year" : 2022 #duplicates are not allowed, if there is one then it takes the last one
}
print(mydict1)

mydict2 = dict(name = "Nurali", age = 17, country = "KZ")
print(mydict2)

print(mydict.items()) # prints key:value
print(mydict.keys()) #prints keys
print(mydict.values()) # prints values

mydict3 = {
    "name" : "Gennadiy",
    "surname" : "Golovkin"
}
mydict3["age"] = 42 #add new key:value
print(mydict3) 
mydict3["age"] = 41 # changing the value
print(mydict3) 
mydict3.update({"age" : 43}) #change the value 2nd way and can be used to add
print(mydict3)

mydict4 = {
    "name" : "KBTU",
    "year" : 2001,
    "status" : "Best"
}
mydict4.pop("status") # ways to delete items
del mydict4["year"]
print(mydict4)

mydict5 = {
    "name" : "almaty",
    "year" : 2025
}
for x in mydict5: #this is only to loop a key
    print(x)
for x in mydict5: # to loop a values
    print(mydict5[x]) 
for x, y in mydict5.items(): # to print both
    print(x, y)

thisdict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict7 = thisdict6.copy()
print(mydict7)

family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(family)



print("----------------------------------------------------------")
print("------------------------------------------------------------------")


# PYTHON IF ELSE
a = 50
b = 50
c = 40
mylist = [10, 50, 20]
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
elif a in mylist and b in mylist:
    print(f"{a} and {b} are in mylist")

if a == b:
    print("a and b are equal")          


print("----------------------------------------------------------")
print("------------------------------------------------------------------")



# PYTHON WHILE LOOPS
i = 1
while i < 10:
    print(i)
    i += 1
j = 1
while j < 6:
    if j == 3:
        break
    else:
        print(j)
        j += 1    

        

print("----------------------------------------------------------")
print("------------------------------------------------------------------")




# PYTHON FOR LOOPS
fruits = [1, 2, 3, 5, 6]
for number in fruits:
    print(number)
    if number == 5:
        break
for i in range(1, 6, 2): # printing from 1 to 5 skipping one num
    print(i)    