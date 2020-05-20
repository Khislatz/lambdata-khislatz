import unittest
from random import randint
from acme import Product
from acme_report import generate_products

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Check if the function receives a list of length 30"""
        len_of_prod = 30
        products = generate_products()
        self.assertEqual(len(products), len_of_prod)

    def test_legal_names(self):
        """Check that the generated names for a
        default batch of products are all valid possible names to generate (adjective,
        space, noun, from the lists of possible words)"""
        products = generate_products()
        names = [i.name for i in products]
        for x in names:
            self.assertEqual(len(x.split(' ')), 1)

if __name__ == '__main__':
    unittest.main() 