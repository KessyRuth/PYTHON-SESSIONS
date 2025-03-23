my_list = [] #Creating an empty list

#Adding elements to my_list using the append method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting the value 15 at the second position
my_list.insert(1,15)

#Extending my_list with another list2
list2 = [50,60,70]
my_list.extend(list2)

my_list.pop()  # Remove the last element from my_list

my_list.sort()  #Sort my_list in ascending order

#Find and print the index of value 30
print(my_list.index(30))
