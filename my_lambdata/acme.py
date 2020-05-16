
from random import randint

class Product():
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, 
                indentifier = randint(1000000, 9999999)):
                self.name = name 
                self.price = price
                self.weight = weight 
                self.flammability = flammability
                self.identifier = indentifier



if __name__ == "__main__":
        
    prod = Product('A Cool Toy')
    print(prod.name)
    print(prod.price)
    print(prod.weight)
    print(prod.flammability)
    print(prod.identifier)


# Save the class in `acme.py`, and you can test your code in a Python repl as
# follows:

# ```python
# >>> from acme import Product
# >>> prod = Product('A Cool Toy')
# >>> prod.name
# 'A Cool Toy'
# >>> prod.price
# 10
# >>> prod.weight
# 20
# >>> prod.flammability
# 0.5
# >>> prod.identifier
# 2812086  # your value will vary
# ```
