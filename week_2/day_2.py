
# list = [1,2,3,4,5,6,7,8,9]

slicing_numbers = list[0:6]

# print(slicing_numbers)
slicing_numbers_from_end = list[-4:-1]

# print(slicing_numbers_from_end)

# Basic operations with a list 

# len_in_list = len(list)

# print(len_in_list)
concat = [1,2,3,4] + [5,6,7,8]
# print(concat)
# Repition
repeat = ["Yes"] * 5
# print(repeat)

# Membership
# checking = 16 in list
# print(checking)

#----- List built in methods -----
# premier_league_clubs = ["Arsenal", "Manchester United","Chelsea", "Manchester City", "Liverpool"]

# premier_league_clubs.append("Tottenham Hotspur")

# premier_league_clubs.insert(2, "Aston Villa")

# premier_league_clubs.remove("Chelsea")

# premier_league_clubs.pop(1)

# print(premier_league_clubs)

# tuple

tuple_datas = (1, 2, 3, 4, 5, 6)

# Repition
repeat = tuple_datas * 2

# print(repeat)
# print(tuple_datas)

# Membership
# checking = 21 in tuple_datas
# print(checking)

# slicing
slicing_tuple = tuple_datas[1:4]
# print(slicing_tuple)

#----- Set -----
collection_of_numbers = {1, 2, 3, 4, 5, 6}
# print(type(collection_of_numbers))
setA = {1, 9}
setB = {1,3,9,6}
setA

union = setA.union(setB)
intersection = setA.intersection(setB)

# print("set A: ", setA)
# print("set B: ", setB)
# print("Union: ", union)
# print("Intersection: ", intersection)
# print("Membership: ",1 in setA, 14 not in setB)

concat_set = {1, 2, 3}

concat_set.add(4)

# concat_set.remove(5)
concat_set.pop()
concat_set.update({5,6,7,})
# print(concat_set)

#---- conditional statements ----
# if statement

# if True:
#     print("It's true")
#     else:
#         print("It's not true")

# score = 80
# if score >= 80:
#     print("Excellent work, well done!")
# elif score > 60:
#     print("Fair, you tried")
# else:
#      print("Oops, Try Again")

#---- loops ------
# Examples of iterables
# list
# strings
# tuple
# dictionary
# set
# ------


numbers = [1,2,3,4,5,6,7,8]
for num in numbers:
    if num == 6:
      print("I have found the number 6,")
      continue
    # print(num)

students = ["Adam", "Bob", "Sam"]

for index, stud in enumerate(students):
   if stud == "Bob":
       students[index] = "Sam"

# print(students)

random_numbers = [4,14,12,8,22,19]
highest_number = 0
for numb in random_numbers:
   if numb  > highest_number:
      highest_number = numb
# print(highest_number)

users = ["dapo", "tunde", "jesse", "joseph"]
emails = []

for index, user in enumerate(users):
   emails.append(user + "@gmail.com")

#    print(emails)

for index, user in enumerate(users):
   users[index] = user + "@gmail.com"

#    print(users)

   str_of_numbers = "124682937"

   new_str = ""
   for index, num in enumerate(str_of_numbers):
      if int(num) > 5:
         new_str = new_str + "*"
      else:
         new_str = new_str + num

# print(new_str)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_list = []

for num in numbers:
   if num % 2 == 0:
      new_list.append(num)
   else:
      print(new_list)