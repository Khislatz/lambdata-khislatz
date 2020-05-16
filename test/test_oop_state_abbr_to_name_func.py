

#OBEJCTIVE: test the add_state_names() function from the my_lambdata/state_abbr_to_name_func.py file  
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)
from pandas import DataFrame
import unittest 
from my_lambdata.state_abbr_to_name_func_oop import DataProcessor

class TestDataProcessor(unittest.TestCase):
        
    def test_add_state_names_oop(self):
        df = DataFrame({"abbrev":["CA", "CT", "CO", "DC", "TX", "FL", "NY"]})
        processor = DataProcessor(df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])

        processor.add_state_names() #processor is mutating the df

        self.assertEqual(list(processor.df.columns), ['abbrev', 'name'])
        self.assertEqual((processor.df.iloc[0,1]), 'California')
        self.assertEqual((processor.df.iloc[0]['abbrev']), 'CA')
        # expect that it has one more column and the same number of rows
        # expect that certain column names exist before and 
        # certain column names exist after

if __name__ == '__main__':
    unittest.main()
