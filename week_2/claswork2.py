# ================================
# Classwork Assignment: NaijaTech Intern Challenge
# ================================

# Scenario:
# You're a fresh backend intern at **NaijaTech Innovations**, based in Lagos.
# You're working on backend tasks to practice Python dictionary and list operations.

# -------------------------------
# 1. Dictionary Creation
# -------------------------------
# Create a dictionary `player` with keys: "name" (value: "Messi"), 
# "goals" (value: 30), and "club" (value: "PSG")
# No.1 Answer Here
player ={
    "name": "Messi",
    "goals" : 30,
    "club" : "PSG"
}
print(player)

# -------------------------------
# 2. Dictionary Value Update
# -------------------------------
# Update the "goals" value in the `player` dictionary to 35
# No.2 Answer Here
player = {
    "name": "Messi",
    "goals" : 30,
    "club" : "PSG"
}
player["goals"] = 35

print(player)


# -------------------------------
# 3. Adding Dictionary Key-Value
# -------------------------------
# Add a new key "assists" with value 12 to the `player` dictionary
# No.3 Answer Here
player = {
    "name": "Messi",
    "goals" : 30,
    "club" : "PSG"
}
player["goals"] = 35

player["assists"] = 12

print(player)

# -------------------------------
# 4. List Creation
# -------------------------------
# Create a list `teams` containing: "Arsenal", "Chelsea", "Liverpool"
# No.4 Answer Here
teams = ["Arsenal", "Chelsea", "Liverpool"]

print(teams)

# -------------------------------
# 5. List Modification
# -------------------------------
# Change the second item in `teams` to "Man City"
# No.5 Answer Here

teams = ["Arsenal", "Chelsea", "Liverpool"]

teams[1] = "Man City"
print(teams)    

# -------------------------------
# 6. Nested Dictionary Access
# -------------------------------
# Given this dictionary:
stats = {
    "Messi": {"goals": 35, "assists": 12},
    "Ronaldo": {"goals": 38, "assists": 10}
}


# Print Ronaldo's assists count
# No.6 Answer Here
stats = {
    "Messi": {"goals": 35, "assists": 12},
    "Ronaldo": {"goals": 38, "assists": 10}
}

print(stats["Ronaldo"]["assists"])
   



# -------------------------------
# 7. List-Dictionary Combination
# -------------------------------
# Create a list `players` containing the `stats` dictionary and `teams` list
# Then print Chelsea's position (index 0) from the nested data
# No.7 Answer Here
players = [stats, teams]
print(players[1][0])  # Accessing Chelsea's position in the teams list      
# -------------------------------




# ================================
# End of Assignment 🎯
# ================================