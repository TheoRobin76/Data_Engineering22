import json

car_data = {"name": "tesla", "engine": "electric"}

# car_data_json_string = json.dumps(car_data)
#
# print(car_data_json_string)
# print(type(car_data_json_string))

# with open('new_json_file.json', 'w') as jsonfile: #writing a json file (dump)
#     json.dump(car_data, jsonfile)


with open('new_json_file.json') as jsonfile: #reading a json file (load)
    car = json.load(jsonfile)
    print(type(car))
    print(car['name'])
    print(car['engine'])

