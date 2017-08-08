'''● Recipe Book
    ○ Recipes are dictionaries that map ingredients to amounts
    ○ A recipe book is a dictionary that maps foods to recipes
● Shop
    ○ A shop is a dictionary that maps ingredients to prices
● Pantry
    ○ A pantry is a dictionary from ingredients to amounts'''

mainmenu = input("Type 'v' to view inventory"
"\nType 'm' to make a dish"
"\nType 's' to sell an item"
"\nType 'r' to view the recipe book")

money = 100

inv = {
"Apple : 5",
"Wheat : 5"
}

price_ingredients = {
"Radish : 3",
"Hydromelon : 4",
"Voltfruit : 4",
"Fresh Milk : 3",
"Apple : 2",
"Tabantha : 5",
"Wheat : 1",
"Cane Sugar : 2",
"Goat Butter : 2"
"Monster Extract : 8",
"Raw Meat : 6",
"Hylian Rice : 2",
"Rock Salt : 3",
"Hylian Shroom : 4",
"Enduring Carrot : 5",
"Hyrule Bass : 5",
"Spicy Pepper : 3",
"Swift Violet : 6",
"Fortified Pumpkin : 5"
}

price_dishes = {
"Creamy Heart Soup : 8",
"Apple Pie : 10",
"Monster Cake : 20",
"Meat and Rice Bowl : 10",
"Fruit and Mushroom Mix : 10",
"Enduring Milk : 6",
"Spicy Pepper Seafood : 12",
"Hasty Veggie Rice Balls : 15",
"Hearty Clam Chower : 25",
"Tough Hot Buttered Apple : 30"
}

recipes = {
    "Creamy Heart Soup" : {"Radish : 1", "Hydromelon : 1", "Voltfruit : 1", "Fresh Milk : 1"},
    "Apple Pie" : {"Apple : 2", "Tabantha : 1", "Wheat : 1", "Cane Sugar : 2", "Goat Butter : 2"},
    "Monster Cake" : {"Monster Extract : 2", "Tabantha : 2", "Wheat : 5", "Cane Sugar : 3", "Goat Butter : 1"},
    "Meat and Rice Bowl" : {"Raw Meat : 4", "Hylian Rice : 3", "Rock Salt : 3"},
    "Fruit and Mushroom Mix" : {"Apple : 3", "Hylian Shroom : 3"},
    "Enduring Milk" : {"Enduring Carrot : 3", "Fresh Milk : 2"},
    "Spicy Pepper Seafood" : {"Hyrule Bass : 2", "Spicy Pepper : 2"},
    "Hasty Veggie Rice Balls" : {"Hylian Rice : 3", "Swift Violet : 4"},
    "Hearty Clam Chowder" : {"Fresh Milk : 1", "Tabantha : 1", "Wheat : 3", "Goat Butter : 2"},
    "Tough Hot Buttered Apple" : {"Apple : 2", "Fortified Pumpkin : 1", "Goat Butter : 2"},
}

'''for key in recipes:
    print(key)
user = input("What dish would you like to view the ingredients for? ")
for key in recipes[user]:
    print(key)

for key, val in recipes.items():
    print("Dish: " + key + "\tIngredients: " + str(val))'''
