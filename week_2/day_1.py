# Dictionary
footballer = {
    "name": "Lionel Messi",
    "age": 36,
    "team": "Paris Saint-Germain",
    "position": "Forward",
    "bio": {
        "birth_year": 1987,
        "nationality": "Argentinian",
        "height_cm": 170,
        "weight_kg": 72
    }
}

sentence_with_concatenation = footballer["name"] + " plays for " + footballer["team"] + " as a " + footballer["position"] + "."
sentence_with_interpolation = f"{footballer['name']} plays for {footballer['team']} as a {footballer['position']}."

# print(sentence_with_concatenation)
# print(sentence_with_interpolation)

footballer["position"] = "forward, attacking midfielder"

footballer["jersey_number"] = 30

del footballer["bio"]["weight_kg"]

footballer.clear()

# print(footballer)

# list

list = ["dapo", "joseph", "james", "david", "micheal", [1,2,["ate", False, ["go ghana"]]], True, 45]

deep = ["item", False,[4,14,2,9, [1,[2,"jesse"]]], "wish", ["Arsenal", "football", {"league_structure": ["20", "champions league"]}]]

print(list[5][2][2][0])

print(deep[2][4][1][1])

print(deep[4][2]["league_structure"][1])

numbers = [4,3,2,1]

numbers[2] = 30

deep[4][0] = ["Sheffield United"]

del deep[3]
del deep[3][2]
print(deep)

# print(list)