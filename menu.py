sederplate = ["Matzah", "Zeroa", "Charoset", "Beitzah", "Maror", "Karpas", "Hazeret"]
dinner = ["Mazto ball soup", "Brisket, "Challah"]
dessert = ["Chocolate cake"]
import random
x = random.randint(0,6)
y = random.randint(0,1)
z = random.randint(0, 0)
printseder = sederplate[x]
printdinner = dinner[y]
printdessert = dessert[z]
print("You'll have " + printseder + ", " + printdinner + ", and " + printdessert + " during Pesach!")
