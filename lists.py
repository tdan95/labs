#lists to store items
#lists are changable, ordered, duplicable, and indexed
planes = ["Airbus", "Boeing", "Embraer", "Cessna"] #lists are in square brackets
print(planes)
print("--------------------------------------")


planes_duplicate = ["Airbus", "Airbus", "Airbus"] #duplicated list to prove that lists can contain duplicates
print(planes_duplicate)
print(f"the lenght of the list is {len(planes_duplicate)}") # len(your_list) can show you a lenght of ur list
print("--------------------------------------")

info = ["Python", 1991, True, "Guido Van Rossum"] # can contain multiple data
print("--------------------------------------")



numbers = list((1, 2, 3, 4)) #other way to create list by using list()
#note that when we use list(), we use double round brackets
print(numbers)
print(numbers[1]) 
print(numbers[-1]) #negative indexes available
print("--------------------------------------")



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:3])

print("--------------------------------------")


f_ruits = ["apple", "banana", "cherry"] #this is for changing
f_ruits[1] = "blackcurrant" # banana -> blackcurrant
print(f_ruits)


print("--------------------------------------")


l_i_s_t = ["apple", "banana", "cherry"]
l_i_s_t[1:2] = ["blackcurrant", "watermelon"] #banana >>> blackcurrant, watermelon
print(l_i_s_t)

print("--------------------------------------")

veges = ["potato", "tomato", "cucumber"]
veges[1:3] = ["eggplant"] #tomato and cucumber merged to eggplant
print(veges)


print("--------------------------------------")


cars = ["Mercedes", "Toyota", "Ferrari"]
cars1 = ["Lexus", "Renault"]
cars.insert(1, "Mclaren") #insert(position, new element) you specify a index and element you wanna put
cars.append("Honda") #adds elements at the end
cars.extend(cars1) # attaches another list to the back
print(cars)


print("--------------------------------------")

nums = [10, 20, 30, 40, 50, 60, 70, 70, 80]
nums.remove(10) #removes the number 10
nums.remove(70) #note there are two 70 values but remove deleted only the first one
nums.pop(3) #removes the element in index 3
nums.pop() #if you don't specify an index 3, it just removes the last element
del nums[1] #another way of removal by index
print(nums)

print("--------------------------------------")

phone = ["iphone", "samsung", "xiaomi"]
for element in phone: # 1.to loop through every element in list
    print(element)
for i in range(len(phone)): #2.another way to loop through list
    print(phone[i])    
[print(x) for x in phone]  #3.another way to loop(list comprehension)

print("--------------------------------------")

nums1 = [5, 6, 7, 1, 2, 3, 9 ,10]
nums1.sort() #sort numerically
print("sort numerically:", nums1)
nums1.sort(reverse = True) #sort numerically descending
print("descended numerically sort:", nums1)
nums1.reverse()
print("reversed of descended list: ", nums1)


print("--------------------------------------")


nums2 = [1, 3, 5, 7, 9, 11]
nums3 = nums2.copy() #copy method 1
nums4 = list(nums2) #copy method 2
nums5 = nums2[:] #copy method 3
print(nums3,
      nums4,
      nums5
      )
nums6 = nums4 + nums5 #joining lists and another method is extend() which was mentioned above 
print(nums6)
