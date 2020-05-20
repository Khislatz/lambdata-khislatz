from random import randint


class Product():
    """Creating a class Product"""
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5,
                indentifier = randint(1000000, 9999999)):
                self.name = name
                self.price = price
                self.weight = weight
                self.flammability = flammability
                self.identifier = indentifier

    def stealability(self):
        steal_answer = self.price / self.weight
        if steal_answer < 0.5:
            return "Not so stealable..."
        elif (steal_answer >= 0.5) and (steal_answer < 1):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        exp_answer = self.flammability * self.weight
        if exp_answer < 10:
            return "...fizzle."
        elif (exp_answer >= 10) and (exp_answer < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"

if __name__ == "__main__":

    prod = Product('A Cool Toy')
    """Invoking functions"""
    print(prod.stealability()) 
    print(prod.explode())
    print(prod.name)
    print(prod.price)
    print(prod.weight)
    print(prod.flammability)
    print(prod.identifier)


