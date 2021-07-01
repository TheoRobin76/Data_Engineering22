import json

import boto3
from pprint import pprint

s3_client = boto3.client('s3')  # granular, not abstract

# bucket_list = s3_client.list_buckets()
# pprint(bucket_list, sort_dicts=False)
# list the names of the buckets
# pprint([i['Name'] for i in bucket_list['Buckets']])

bucket_name = 'data-eng-resources'
# bucket_contents = s3_client.list_objects_v2(
#     Bucket=bucket_name,
#     # Prefix='python' # limits to objects that start with 'python'
# )
# pprint(bucket_contents)
# # list the names of the objects in the bucket
# pprint([i['Key'] for i in bucket_contents['Contents']])

# s3_resource = boto3.resource('s3')  # object oriented approach, not capped at 1000
# bucket = s3_resource.Bucket(bucket_name)
# # print(bucket)
# # objects = bucket.objects
# # print(objects)
# # contents = objects.all()
# # print(contents) # collection can be iterated through
# # for object in contents:
# #     print(object.key)
# keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]  # this does it all in one line
# pprint(keys)

# how to access the data within the objects:
# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key= 'python/chatbot-intent.json'
# )
# # pprint(s3_object, sort_dicts=False)
# s3_data = json.loads(s3_object['Body'].read())
# # strbody = s3_data.read()
# # pprint(json.loads(strbody), sort_dicts=False)
# print(s3_data['intents'])

import pandas as pd

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/happiness-2019.csv'
)
# pprint(s3_object)
pprint(s3_object["Body"])
df = pd.read_csv(s3_object["Body"])
# print(df)

# creating your own json file:

my_dict = {
    'name': 'Cheddar',
    'mature': True,
}
# with open('cheese.json', 'w') as jsonfile:
#     json.dump(my_dict, jsonfile)
#
# s3_client.upload_file(
#     Filename='cheese.json',
#     Bucket='data-eng-resources',
#     Key='Data22/test/tgluckstein.json'
# )
# s3_client.put_object(
#     Bucket='data-eng-resources',
#     Key='Data22/test/tgluckstein2.json',
#     Body=json.dumps(my_dict)
# )
# print(type(json.dumps(my_dict)))

import pandas as pd
import io
df = pd.DataFrame([[1,2,3,4,5], [10,20,30,40,50]])
print(df)

str_buffer = io.StringIO()
# print(str_buffer)
df.to_csv(str_buffer)

# s3_client.put_object(
#     Bucket='data-eng-resources',
#     Key='Data22/test/tgluckstein.csv',
#     Body=str_buffer.getvalue()
# )

s3_resource = boto3.resource('s3')
s3_resource.Object(
    'data-eng-resources',
    'Data22/test/tgluckstein2.csv'
).put(
    Body=str_buffer.getvalue()
)
