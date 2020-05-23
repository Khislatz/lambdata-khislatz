                ##  INHERITANCE ##


# #    CHANGING FROM FUNCTIONAL APPROACH TO OOP  
# #    USING MUTATION 

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)
from pandas import DataFrame 

class MyFrame(DataFrame):
    #When we inherite from DataFrame class we can get rid of 
    # constructor because DataFrame already has it
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

        self['name'] = self['abbrev'].map(names_map) #self is referring to the instance inside of the 
        # method. Outside of the method the instance is my_frame 

    #breakpoint(): helps to stop and investigate in terminal up to the breakpoint()function



if __name__ == "__main__":

    # df = DataFrame({"abbrev":["CA", "CT", "CO", "DC", "TX", "FL", "NY"]})
    my_frame = MyFrame({"abbrev":["CA", "CT", "CO", "DC", "TX", "FL", "NY"]}) # my_frame is an instance
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.head())
