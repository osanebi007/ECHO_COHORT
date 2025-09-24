# ================================
# Python Collections & Loops Assignment
# 20 Progressive Questions (Simple → Hard)
# ================================

# print("\n=== Level 1: Basic List Operations ===")
# 1. Create a list called 'fruits' containing "apple", "banana", and "cherry". Print it.
fruits = ["apple", "banana", "cherry"]
print(fruits)


# 2. Using slicing, extract the first two items from 'fruits'. Print the result.
slicing_fruits = fruits[0:2]
print(slicing_fruits)

# 3. Add "orange" to the end of the list and print the updated list.
fruits.append("orange")
print(fruits)

# 4. Create a tuple named 'colors' with "red", "green", and "blue". Print it.
colors = ("red", "green", "blue")
print(colors)


# 5. Check if "yellow" exists in the tuple. Print True or False.
checking_yellow = "yellow" in colors
print(checking_yellow)

# 6. Repeat the tuple 3 times and store it in 'repeated_colors'. Print it.
repeat_colors = colors * 3
print(repeat_colors)

# 7. Create two sets: setA = {1,2,3} and setB = {3,4,5}. Print both.
setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA)
print(setB)


# 8. Find and print the union of setA and setB.
union = setA.union(setB)
print("Union: ", union)


# 9. Find and print the intersection of setA and setB.
intersection = setA.intersection(setB)
print("Intersection: ", intersection)


# 10. Given the list: clubs = ["Chelsea","Arsenal","Liverpool"], insert "Man City" at position 1.
clubs = ["Chelsea", "Arsenal", "Liverpool"]
clubs.insert(1, "Man City")
print(clubs)

# 11. Remove "Arsenal" from the list and print the final list
clubs.remove("Arsenal")
print(clubs)

# 12. Check if the number 15 exists in this list: [10,20,30,40]. Print the result.
checking_15 = 15 in [10, 20, 30, 40]
print(checking_15)

# 13. Classify a score of 85: 80+ = "A", 70+ = "B", else "C". Print the grade.if score >= 80:
score = 85
if score >= 80:
    grade = "A, Excellent Score!"
elif score >= 70:
    grade = "B, Good Score!"
else:
    grade = "C, Needs Improvement!"
print(grade)



# 14. Using a loop, print all even numbers between 1-10 (inclusive).



# 15. Convert these names to email addresses: ["dapo","tunde"] → ["dapo@gmail.com", ...]
names = ["dapo", "tunde"]
emails = []
for index, user in enumerate(names):
   emails.append(user + "@gmail.com")
print(emails)


# 16. Find and print the highest number in [4,14,12,8,22,19].
random_numbers = [4, 14, 12, 8, 22, 19]
highest_number = 0
for numb in random_numbers:
   if numb  > highest_number:
      highest_number = numb
print(highest_number)



# 17. In the string "124682937", replace all digits >5 with "*". Print result.
str_of_numbers = "124682937"
new_str = ""
for index, num in enumerate(str_of_numbers):
      if int(num) > 5:
         new_str = new_str + "*"
      else:
         new_str = new_str + num
print(new_str)


# 18. Create a dictionary from keys ["name","age"] and values ["Alice",25].
keys = ["name", "age"]
values = ["Alice", 25]



# 19. Flatten this 2D list: [[1,2],[3,4],[5,6]] → [1,2,3,4,5,6].



# 20. Find elements in {1,2,3,4} that aren't in {3,4,5,6} (set difference).
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set_diff = set1.difference(set2)
print("Set Difference: ", set_diff)