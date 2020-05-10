import numpy as np
import pandas as pd
# Check a dataframe for nulls, print/report them in a nice "pretty" format


# Create a class
class Nulls:
    # Create constructor
    def __init__(self, df):
        self.df = df

    def check_nulls(self):
        # Checking for missing values and counting them
        new_df = self.df.copy()
        print(new_df.isna())
        print(new_df.isna().sum())


if __name__ == "__main__":

    df = pd.DataFrame({'Name': ['John', 'Peter', 'Sam', np.nan],
                       'Age': [30, np.nan, np.nan, 45],
                       'Income': [100000, 75000, np.nan, 50000]})
    print(df.head())

    df_with_nulls = Nulls(df)
    df_with_nulls.check_nulls()  # Invoking the function


    
  
