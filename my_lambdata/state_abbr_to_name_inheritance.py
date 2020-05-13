# #    CHANGING FROM FUNCTIONAL APPROACH TO OOP  
# #    USING MUTATION 

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)
from pandas import DataFrame 

class DataProcessor():
    def __init__(self, my_df):
        self.df = my_df # we are storing my_df on the instance itself 


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

        self.df['name'] = self.df['abbrev'].map(names_map)

    #breakpoint(): helps to stop and investigate in terminal up to the breakpoint()function

        return self.df


if __name__ == "__main__":

    df = DataFrame({"abbrev":["CA", "CT", "CO", "DC", "TX", "FL", "NY"]})

    processor = DataProcessor(df) 
    print(processor.df.head())
    processor.add_state_names()
    print(processor.df.head())
    #if we do it like last time then we will have to 
    # processor = DataProcessor(df) 
    # df2 = processor.add_state_names()
    #print(df2.head())