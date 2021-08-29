
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

print("Question_1")
def map_indexesValues(df, col):
    df_col = df[col].value_counts()
    a = df_col.index.tolist()
    b = df_col.values.tolist()
    return a, b

Map = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
print('')

popularitems, popular_itemscount = map_indexesValues(Bakery_data_set, 'Item')
plt.bar(popularitems[:10], popular_itemscount[:10])


plt.xlabel('10 Popular items')
plt.ylabel('No of Transactions')
plt.show()

print("Top 10  popular items in bakery:","\n", popularitems[:10])