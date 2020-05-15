# #    CHANGING FROM FUNCTIONAL APPROACH TO OOP  
# #    USING MUTATION 
## ## INHERITANCE

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)
from pandas import DataFrame 

class MyFrame(DataFrame):
    def __init__(self, my_df):
        self.my_frame = my_df # we are storing my_df on the instance itself 


    def add_state_names(self):
        """
        Adds a column of state to accompany 
        a corresponding column of state abbreviation.      
        This time we will be using mutation
        """
        #We could do it like last time:
        #new_df = self.df.copy()
        # And then new_df['name'] = new_df['abbrev'].map(names_map)

        names_map = {"CA": "California", "CT":"Connecticut", "CO": "Colorado", 
                    "DC": "District of Columbia", "TX": "Texas", "FL": "Florida",
                    "NY": "New York"}

        self['name'] = self['abbrev'].map(names_map)

    #breakpoint(): helps to stop and investigate in terminal up to the breakpoint()function

        return self.df


if __name__ == "__main__":

    my_frame = MyFrame({"abbrev":["CA", "CT", "CO", "DC", "TX", "FL", "NY"]})
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.head())
