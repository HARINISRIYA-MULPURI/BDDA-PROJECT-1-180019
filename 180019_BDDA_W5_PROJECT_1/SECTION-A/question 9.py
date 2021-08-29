#harini_sriya_180019
import pandas as pd
import matplotlib.pyplot as plt

Bakery_data_set = pd.read_csv("G:/semester 7/Bigdata-2/Week 5/BreadBasket_DMS.csv")
Bakery_data_set.dropna()
Bakery_data_set = Bakery_data_set[Bakery_data_set['Item'] != 'NONE']

Bakery_data_set['Date'] = pd.to_datetime(Bakery_data_set['Date'])
Bakery_data_set['Time'] = pd.to_datetime(Bakery_data_set['Time'])
Bakery_data_set['Year'] = Bakery_data_set['Date'].dt.year
Bakery_data_set['Month'] = Bakery_data_set['Date'].dt.month
Bakery_data_set['Day'] = Bakery_data_set['Date'].dt.day
Bakery_data_set['Weekday'] = Bakery_data_set['Date'].dt.weekday
Bakery_data_set['Hour'] = Bakery_data_set['Time'].dt.hour

def map_indexes_and_values(df, col):
    df_col = df[col].value_counts()
    x = df_col.index.tolist()
    y = df_col.values.tolist()
    return x, y

def coffee_ext(group):
    match = group['Item'].str.contains('Coffee')
    return Bakery_data_set.loc[match]

coffee_item = Bakery_data_set[ Bakery_data_set['Item'].str.contains('Coffee')]['Transaction'].unique()


#
coffee_item = pd.DataFrame(coffee_item,columns=['Transaction'])
coffee_m=coffee_item.merge(Bakery_data_set, left_on='Transaction',right_on='Transaction',how='right')

coffee_m = coffee_m[~coffee_m.Item.str.contains('Coffee')]['Item'].value_counts()

print("This is Question 9")
Bakery_data_set['Date'] = pd.to_datetime(Bakery_data_set['Date'], format='%d-%m-%Y', errors='coerce')
Bakery_data_set['year'] = Bakery_data_set['Date'].dt.year

yearsetup=Bakery_data_set.loc[Bakery_data_set['year']==2017]

coffee=yearsetup.set_index(['Item'])
onlycoffee=coffee.loc['Coffee']
onlycoffee.reset_index(inplace=True)

popular=onlycoffee['Date'].value_counts()
print(popular.head())
popular.head().plot(kind='line', color='red', marker='*')
plt.xlabel('Day/Date')
plt.ylabel('Number of Transactions')
plt.title('Top 5 Coffee Sales day in 2017')
plt.show()
coffee_item = pd.DataFrame(coffee_item,columns=['Transaction'])
coffee_m=coffee_item.merge(Bakery_data_set, left_on='Transaction',right_on='Transaction',how='right')

coffee_m = coffee_m[~coffee_m.Item.str.contains('Coffee')]['Item'].value_counts()

print("This is Qestion 8")
plt.figure(figsize=(10,6))
coffee_m[:5].plot(kind='bar')
plt.show()