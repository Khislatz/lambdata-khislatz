
#OBEJCTIVE: test the add_state_names() function from the my_lambdata/state_abbr_to_name_func.py file  
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)
from pandas import DataFrame
import unittest 
from my_lambdata.state_abbr_to_name_func import add_state_names

class TestAbbrNames(unittest.TestCase):
        
    def test_add_state_names(self):
        df = DataFrame({"abbrev":["CA", "CT", "CO", "DC", "TX", "FL", "NY"]})
        self.assertEqual(list(df.columns), ['abbrev'])
        result = add_state_names(df)
        self.assertEqual(list(result.columns), ['abbrev', 'name'])
        # expect that it has one more column and the same number of rows
        # expect that certain column names exist before and 
        # certain column names exist after

if __name__ == '__main__':
    unittest.main()
