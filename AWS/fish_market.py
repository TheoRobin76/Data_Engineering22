import boto3
from pprint import pprint
import pandas as pd
import io

# Length1     Length from the nose to the beginning of the tail (in cm)
# Length2     Length from the nose to the notch of the tail (in cm)
# Length3     Length from the nose to the end of the tail (in cm)

s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'

# how to access the data within the objects:
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market-mon.csv'
)
# pprint(s3_object["Body"])
df_mon = pd.read_csv(s3_object["Body"])
# print(df_mon)

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market-tues.csv'
)
# pprint(s3_object["Body"])
df_tues = pd.read_csv(s3_object["Body"])
# print(df_tues)

# working out the averages
# first group by the fish species

fish_mon = df_mon.groupby('Species')
fish_tues = df_tues.groupby('Species')

avg_fish_mon = fish_mon.mean()
avg_fish_tues = fish_tues.mean()

# adding 'Mon' and 'Tues' to row headings for easy comparison
renamed_mon = (avg_fish_mon.rename(index=lambda s: s+' Mon'))
renamed_tues = (avg_fish_tues.rename(index=lambda s: s+' Tues'))

# put both dataframes into one dataframe for easier comparison
avg_fish_table = pd.concat([renamed_mon, renamed_tues], axis=0)
# print(avg_fish_table)

# reorder dataframe for easier comparison between species over the two days
fin_table = avg_fish_table.sort_values('Species')
# print(fin_table)

# adding to s3, AWS
# str_buffer = io.StringIO()
# fin_table.to_csv(str_buffer)
#
# s3_client.put_object(
#     Bucket='data-eng-resources',
#     Key='Data22/fish/tgluckstein.csv',
#     Body=str_buffer.getvalue()
# )

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Data22/fish/tgluckstein.csv'
)
pprint(s3_object["Body"])
fin_df = pd.read_csv(s3_object["Body"])
pprint(fin_df)