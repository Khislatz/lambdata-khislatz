import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine 

# construct a path to wherever your database exists
#DB_FILEPATH = "rpg_db.db"

buddymove_df = pd.read_csv (r'C:\Users\Khisl\Desktop\lambdata-khislatz\SQL_data\buddymove_holidayiq.csv')   
engine = create_engine('sqlite:///buddymove_holidayiq.db')
buddymove_df.to_sql('review', con=engine, if_exists='replace', index_label='id')
# buddymove_df = buddymove_df.rename(columns={'id':'Id', 'User Id': 'User_Id', 'Sports':'Sports', 
# 'Religious':'Religious', 'Nature':'Nature', 'Theater':'Theater', 'Shopping':'Shopping', 'Picnic':'Picnic'})

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", 'buddymove_holidayiq.db')
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
print("CONNECTION:", connection)

## Count how many rows you have - it should be 249!

query = "SELECT count(Sports) FROM review;"
result = cursor.execute(query).fetchone()
print("There are ", list(result), " rows")

## How many users who reviewed at least 100 Nature in the category
# also reviewed at least 100 in the Shopping category?

query1 = """
SELECT 
	count(`User Id`) 
FROM review
WHERE Nature >=100 AND Shopping >= 100;
"""
result1 = cursor.execute(query1).fetchone()
print("There are ", list(result1), " users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category")

## What are the average number of reviews for each category?

query2 = """
SELECT AVG(Sports) as Avg_sports_reviews
FROM review;"""
result2 = cursor.execute(query2).fetchone()
print("There average number of reviews for Sports category is ", list(result2)) 

query3 = """
SELECT AVG(Religious) as Avg_religious_reviews
FROM review;"""
result3 = cursor.execute(query3).fetchone()
print("There average number of reviews for Religious category is ", list(result3)) 

query4 = """
SELECT AVG(Nature) as Avg_nature_reviews
FROM review;"""
result4 = cursor.execute(query4).fetchone()
print("There average number of reviews for Nature category is ", list(result4)) 

query5= """
SELECT AVG(Theatre) as Avg_theater_reviews
FROM review;"""
result5 = cursor.execute(query5).fetchone()
print("There average number of reviews for Theatre category is ", list(result5)) 

query6 = """
SELECT AVG(Shopping) as Avg_shopping_reviews
FROM review;"""
result6 = cursor.execute(query6).fetchone()
print("There average number of reviews for Shopping category is ", list(result6)) 

query7 = """
SELECT AVG(Picnic) as Avg_picnic_reviews
FROM review;"""
result7 = cursor.execute(query7).fetchone()
print("There average number of reviews for Picnic category is ", list(result7)) 
