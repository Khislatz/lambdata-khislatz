

class Polo:
    def __init__(self, size, color, price=69.99): #constructor 
        self.size = size
        self.color = color
        self.price = price

    def wash(self):
        print('Washing...')
        print(f'Washing the {self.size.upper()} {self.color.upper()} Polo!')

if __name__ == "__main__":
    

    polo = Polo(size = 'Large', color = 'Blue')  
    #size and color are attributes

    print(polo.size, polo.color)
    polo.wash() # invoking a method
 
    polo2 = Polo(size = 'Small', color = 'Yellow')
    print(polo2.size, polo2.color)
    polo2.wash()