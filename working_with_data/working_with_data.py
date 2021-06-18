import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_data = sns.load_dataset('titanic')
pd.set_option('display.max_columns', None)
print(titanic_data.head(), '\n')

print('FALSE VALUES :\n', titanic_data.isna().sum(), '\n')
print('TYPES: \n', titanic_data.dtypes, '\n')

# we want to be rid of unneccesary columns - those with lots of missing data.
# deck has many missing values and must be removed
# some columns say the same thing, duplicates must be removed
# pclass == class
# sex == who
# probably don't need adult_male
# what age makes a man
# survived the same as alive
# sibsp and parch are unclear
# embarked town == embarked

new_titanic_data = titanic_data.drop(columns=['deck', 'pclass', 'embarked', 'survived'], inplace=False)
print(new_titanic_data, '\n')
# print(new_titanic_data.who.value_counts())

print(new_titanic_data.describe(), '\n')
print(new_titanic_data.age.value_counts(),'\n')

child_index = new_titanic_data['who'] == 'child'
print(new_titanic_data[child_index].describe(), '\n') # therefore maximum age for a child is 15


# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='alive', y='age', data=titanic_data, style = 'who', hue= 'who', s=50);
# plt.show()

plt.figure(figsize=(12, 8))
plt.style.use('fivethirtyeight') # changes the style of the chart
sns.barplot(x='embark_town', y='age', data=titanic_data, hue= 'who');
plt.show()












