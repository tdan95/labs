# boolean is either true or false 
print(10>9) #since 10 is greater than 9, python will print "True"
print (9>10) # 9 is not greater than 10, python will print "False"

print("----------------------------------------")

#booleans work for the if, while statements
a, b = 50, 49
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

print("-----------------------------")

#bool() function
print(bool("Hello")) #inside the bool function we have something that is why it is true
print(bool("")) # there is no string so it is false

print("-----------------------")

# bool in funtion
def smth():
    return 0
print(bool(smth())) #as you see the function is zero and zero is always false

print("-----------")

#isintance( ) function
x = 200
print(isinstance(x, int)) #checks if x is integer and it should return true