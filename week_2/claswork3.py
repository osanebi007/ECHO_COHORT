# ================================
# Classwork Assignment: Python Collections
# ================================

# -------------------------------
# 1. List Slicing (10/10)
# -------------------------------
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Slice from index 2 to 5 (inclusive) and print
sliced_numbers = numbers[2:5]
print(sliced_numbers)


# -------------------------------
# 2. List Operations (10/10)
# -------------------------------
# Concatenate these lists and print the result
list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated_list = list_a + list_b
print(concatenated_list)


# -------------------------------
# 3. List Methods (10/10)
# -------------------------------
clubs = ["Chelsea", "Arsenal", "Liverpool"]
# Add "Man City" to the end, then remove "Arsenal"
clubs.append("Man City")
clubs.remove("Arsenal")
print(clubs)


# -------------------------------
# 4. Tuple Operations (10/10)
# -------------------------------
colors = ("red", "green", "blue")
# Repeat the tuple 3 times and check if "yellow" exists
repeat_colors = colors * 3
print(repeat_colors)
checking_yellow = "yellow" in colors
print(checking_yellow)

# -------------------------------
# 5. Set Operations (10/10)
# -------------------------------
set_x = {1, 2, 3}
set_y = {3, 4, 5}
# Find and print the union and intersection
union = set_x.union(set_y)
intersection = set_x.intersection(set_y)
print("Union: ", union)
print("Intersection: ", intersection)


# -------------------------------
# 6. Advanced Set Operations (10/10)
# -------------------------------
numbers_set = {10, 20, 30}
# Add 40, remove 10, update with {50, 60}
numbers_set.add(40)
numbers_set.remove(10)
numbers_set.update({50, 60})


# -------------------------------
# 7. Membership Testing (10/10)
# -------------------------------
mixed_list = [1, "apple", True, 3.14]
# Check if "apple" exists and 2 doesn't exist
checking_apple = "apple" in mixed_list
checking_two = 2 not in mixed_list
print(checking_apple)
print(checking_two)



# -------------------------------
# 8. List Manipulation (10/10)
# -------------------------------
nums = [5, 2, 8, 1, 9]
# Insert 10 at index 2, then pop the last element
nums.insert(2, 10)
nums.pop()
print(nums)


# -------------------------------
# 9. Tuple Slicing (10/10)
# -------------------------------
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
# Slice from index 1 to end and print
slice_days = days[1:]
print(slice_days)


# -------------------------------
# 10. Set Differences (10/10)
# -------------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Find elements in set1 but not in set2
set_diff = set1.difference(set2)
print(set_diff)
