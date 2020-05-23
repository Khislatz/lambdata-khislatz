
# lambdata-khislatz 

##  WE CREATE A NEW FOLDER my_lambdata

## Usage 

'''py
from my_lambdata.my_mod import enlarge # this works
x = 11 
print(enlarge(x)) #importing only enlarge function
#if we use from my_mod import enlarge without "if __name__ == "__main__":"
# then the entire file my_mod will be executed 

## nulls_class.py 
# OBJECTIVE Check a dataframe for nulls, print/report them in a nice "pretty" format
 
First we create class Nulls and it's corresponding constructor: __init__ and pass self and df as arguments. Then we create a function check_nulls where we check for missing values in our dataframe.
Then we create a dataframe which in if __name__ == "__main__", which will be passed into a constructor of class Nulls. Then we create an object and name it df_with_nulls = Nulls(df). And lastly we invoke the function df_with_nulls.check_nulls().



## WE CREATE A NEW FOLDER test

## test_oop_state_abbr_to_name_func.py

#OBEJCTIVE: test the add_state_names() function from the my_lambdata/state_abbr_to_name_func.py file  
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)

First we import a function DataProcessor from my_lambdata.state_abbr_to_name_func_oop.py.
We create a new class TestDataProcessor which inherites properties and methods from a parent class TestCase. Then we create a new function test_add_state_names_oop and pass self as an argument.
We are using uniitest to test that list(processor.df.columns) is equal to "abbrev". 
In this example we use mutation method where processor mutates df. Then we 
test that 1) (list(processor.df.columns) is equal to ['abbrev', 'name']
2) (processor.df.iloc[0,1]) equals 'California'
3) (processor.df.iloc[0]['abbrev']) equals 'CA' 


## test_state_abbr_to_name_func.py

#OBEJCTIVE: test the add_state_names() function from the my_lambdata/state_abbr_to_name_func.py file  
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)


First we import add_state_names function from from my_lambdata.state_abbr_to_name_func.py.
We create a new class TestAbbrNames which inherites properties and methods from a parent class TestCase. Then we create a new function test_add_state_names and pass self as an argument. We will use the same dataframe that we used in previous assignments: df that that a columnn "abbrev. 
We are using uniitest to test that list(processor.df.columns) is equal to "abbrev".
In this example we use mutation method where processor mutates df. Then we 
test that 1) (list(processor.df.columns) is equal to ['abbrev', 'name']
2) (processor.df.iloc[0,1]) equals 'California'
3) (processor.df.iloc[0]['abbrev']) equals 'CA' 
        
'''

