class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class GroceryCart:
    def __init__(self):
        self.cart = {}
        self.cost = 0
    def __str__(self):
        theString = ""
        #totalcost = 0
        for food, quantity in (self.cart).items():
            subtotal = food.price * quantity
            #totalcost = totalcost + subtotal
            theString = theString + "\nFood: " + food.name + "\tPrice: $" + str(food.price) + "\tQuantity: " + str(quantity) + "\tSubtotal: $" + str(subtotal)
        theString = theString + "\nTotal Cost: $" + str(self.cost)
        return theString
    def total(self):
        self.cost = 0
        for food, quantity in (self.cart).items():
            self.cost = self.cost + (food.price * quantity)
        return self.cost
    def addFood(self, Food):
        if (Food in self.cart) == True:
            self.cart[Food] = self.cart[Food] + 1
        else:
            self.cart[Food] = 1
        #self.cost = total()
    def removeItem(self, food_name):
        if (food_name in self.cart) == True:
            self.cart[food_name] = self.cart[food_name] - 1
            if self.cart[food_name] == 0:
                del self.cart[food_name]
            #self.cost = total()
            return True
        else:
            print("You can't remove something that's not there, silly!!!!")
            return False

apple = Food("APPLE", 4)
tofu = Food("TOFU", 4000)
gummyworms = Food("GUMMIES", 10)

myCart = GroceryCart()
myCart.addFood(apple)
myCart.addFood(tofu)
myCart.addFood(tofu)
myCart.addFood(gummyworms)

cost = myCart.total()
print(myCart)
