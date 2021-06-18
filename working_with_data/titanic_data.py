import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_data = sns.load_dataset('titanic')

pd.set_option('display.max_columns', None)
# print(titanic_data.head())
# Columns:  survived, pclass, sex, age, sibsp, parch, fare embarked, class, who, adult_male, deck, embark_town, alive, alone

new_titanic_data = titanic_data.drop(columns=['survived', 'deck', 'pclass', 'embarked'], inplace=False)  # drop columns
# print(new_titanic_data.head())

# maximum age of a child is 15
child_index = new_titanic_data['who'] == 'child'
# print(new_titanic_data[child_index].describe())


first_class_index = new_titanic_data['class'] == 'First'
second_class_index = new_titanic_data['class'] == 'Second'
third_class_index = new_titanic_data['class'] == 'Third'

first_class_rows = new_titanic_data[first_class_index]
rose = first_class_rows.query('age == 17 & alive == "yes" & embark_town == "Southampton" & sex == "female"')
print(rose)

third_class_rows = new_titanic_data[third_class_index]
jack = third_class_rows.query('age == 20 & alive == "no" & embark_town == "Southampton" & sex == "male"')
print(jack)

# print(third_class_rows[South_dead])
# print(third_class_rows[dead])

# shows who survived in categories of men, women and children
plt.figure(figsize=(12, 8))
plt.style.use('fivethirtyeight')
# sns.scatterplot(x='alive', y='age', data=titanic_data, style='who', hue='who', s=50)  # shows who survived in categories of men, women and children
sns.barplot(x='embark_town', y='age', data=titanic_data, hue= 'who');  # average age of men/women/children from embark_town
# plt.show()

# boarder 781 is Rose
# boarders who could be Jack: 12, 91, 131, 441, 640, 682, *725*, 840, 876
