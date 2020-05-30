import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "rpg_db.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "SQL_data", "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
# connection.row_factory = sqlite3.Row
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

## How many total Characters are there?
query = "SELECT count(distinct character_id) FROM charactercreator_character as total_character;"

result = cursor.execute(query).fetchall()
print("There are ", result, " characters")


## How many of each specific subclass?

query1 = "SELECT count (distinct character_ptr_id) as cleric_total FROM charactercreator_cleric;"

result1 = cursor.execute(query1).fetchall()
print("There are ", result1, " cleric characters")

query2 = "SELECT count (distinct character_ptr_id) as fighter_total FROM charactercreator_fighter;"

result2 = cursor.execute(query2).fetchall()
print("There are ", result2, " fighter characters")

query3 = "SELECT count (distinct character_ptr_id) as mage_total FROM charactercreator_mage;"

result3 = cursor.execute(query3).fetchall()
print("There are ", result3, " mage characters")


query5 = "SELECT count (distinct character_ptr_id) as thief_total FROM charactercreator_thief;"

result5 = cursor.execute(query5).fetchall()
print("There are ", result5, " thief characters")


## How many total Items?

query6 = "SELECT count (distinct item_id) FROM armory_item as total_items;"

result6 = cursor.execute(query6).fetchall()
print("There are ", result6, " items in total")


## How many of the Items are weapons? How many are not?

query7 = """SELECT count (distinct item_id) as num_weapons 
            FROM armory_item JOIN armory_weapon on armory_item.item_id = armory_weapon.item_ptr_id;"""

result7 = cursor.execute(query7).fetchall()
print("There are ", result7, " weapons out of total items;")

## How many are not?

query8 = "SELECT count (distinct item_id) as non_weapons FROM armory_item JOIN armory_weapon on armory_item.item_id <> armory_weapon.item_ptr_id;"

result8 = cursor.execute(query8).fetchall()
print("There are ", result8, " non-weapon items;")
# for row in result8:
# 	print(row)

# -- How many Items does each character have? (Return first 20 rows)
# -- row per character (even the ones that have zero)
# -- three cols: char id, char name, item_count 

query9 = "SELECT charactercreator_character.character_id,charactercreator_character.name as character_name,count(distinct charactercreator_character_inventory.item_id) as items FROM charactercreator_character LEFT JOIN charactercreator_character_inventory on charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY charactercreator_character.character_id LIMIT 20;"

result9 = cursor.execute(query9).fetchall()

# for row in result9:
# 	print(row)
print("There are ", result9, " items per each character;")



# -- How many Weapons does each character have? 
# -- (Return first 20 rows) 
# -- row per character (302, including ones that have zero)
# -- three cols: char id, char name, weapon_count

query10 = "SELECT charactercreator_character.character_id,charactercreator_character.name as character_name, count(distinct armory_weapon.item_ptr_id) as weapon_count FROM charactercreator_character LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id GROUP BY 1 LIMIT 20;"

result10 = cursor.execute(query10).fetchall()
print("There are ", result10, " weapons per each character;")


## On average, how many Items does each Character have?

query11 = "SELECT avg(items) as avg_items FROM (SELECT charactercreator_character.character_id,charactercreator_character.name as character_name,count(distinct charactercreator_character_inventory.item_id) as items FROM charactercreator_character LEFT JOIN charactercreator_character_inventory on charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY charactercreator_character.character_id) LIMIT 20;"

result11 = cursor.execute(query11).fetchall()
print("In average there are ", result11, " items per each character;")


## On average, how many Weapons does each character have ?

query12 = """
SELECT avg(weapon_count) as avg_weapons
FROM (
	SELECT 
	  charactercreator_character.character_id
	  ,charactercreator_character.name as character_name
	  ,count(distinct armory_weapon.item_ptr_id) as weapon_count
	FROM charactercreator_character 
	LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
	GROUP BY 1 -- same as charactercreator_character.character_id 
	)
LIMIT 20;
"""
result12 = cursor.execute(query12).fetchall()
print("In average there are ", result12, " weapons per each character;")

