import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']

# luke = db.characters.find_one({"name": "Luke Skywalker"})
#
# droids = db.characters.find({"species.name": "Droid"})
# print(droids)
#
# droid_names = ([droid['name'] for droid in droids]) # list comprehension
# print(droid_names)
# #
# droid_names = (droid['name'] for droid in droids) # generator object
# print(droid_names)
# print(next(droid_names))
# print(next(droid_names))
# print(next(droid_names))
# print(next(droid_names))
# print(next(droid_names))


# for droid in droids:
#     print(droid["name"])

# 1. Find the height of Darth Vader, only return results for the name and the height.

darth_vader = db.characters.find_one({"name": "Darth Vader"})
print([darth_vader["name"], darth_vader["height"]])

# 2. Find all characters with yellow eyes, only return results for the names of the characters.

yellow_eyes = db.characters.find({"eye_color": "yellow"})
print([yellow['name'] for yellow in yellow_eyes])

# 3. Find male characters. Limit your results to only show the first 3.

male_characters = db.characters.find({"gender": "male"}).limit(3)
list_of_males = [male['name'] for male in male_characters]
print(list_of_males)

# 4. Find the names of all the humans whose homeworld is Alderaan.

alderaan_chars = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"})
print([ald["name"] for ald in alderaan_chars])

# 5. What is the average height of female characters?

female_characters = db.characters.find({"gender": "female", "height": {"$exists": True}})
female_heights = [female['height'] for female in female_characters]
# print(female_heights)
avg_height = sum(female_heights)/len(female_heights)
print(f"Average female height: {avg_height}")

# 6. Which character(s) is/are the tallest?
max_height = next(db.characters.aggregate([{"$group": {"_id": None, "max_height": {"$max": "$height"}}}]))['max_height']
# print(max_height)
for tallest in db.characters.find({"height": max_height}):
    print(tallest['name'], tallest['height'])









