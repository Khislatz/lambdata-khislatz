from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30) -> list:
    products = []
    for prod in range(num_products):
        adj = ADJECTIVES[randint(0, 4)]
        nouns = NOUNS[randint(0, 4)]
        prod = Product(adj, nouns)
        prod.weight = randint(5, 100)
        prod.price = randint(5, 100)
        prod.flammability = uniform(0.0, 2.5)
        products.append(prod)

    return products

def inventory_report(products: list) -> str:

    unique_names = len(set([i.name for i in products]))
    avg_price = sum([i.price for i in products]) / len(products)
    avg_weight = sum([i.weight for i in products]) / len(products)
    avg_flamm = sum([i.flammability for i in products]) / len(products)

    report = f'''ACME CORPORATION OFFICIAL INVENTORY REPORT
    Unique product names: {unique_names}
    Average price: {avg_price}
    Average weight: {avg_weight}
    Average flammability: {avg_flamm}'''

    return print(report)

if __name__ == '__main__':
    inventory_report(generate_products())