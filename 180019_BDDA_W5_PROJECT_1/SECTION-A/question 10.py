
#harini_sriya_180019
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Week Days")
plt.ylabel("Sales")

Bakery_data_set = pd.read_csv(r"H:/semester 7/Bigdata-2/Week 5/BreadBasket_DMS.csv")

Bakery_data_set= Bakery_data_set.set_index(['Item'])
Bakery_data_set= Bakery_data_set.drop(['NONE'])
Bakery_data_set.reset_index(inplace = True)

bread= Bakery_data_set['Item']== 'Bread'
breaddata= Bakery_data_set[bread]

breaddata['Date'] = pd.to_datetime(breaddata['Date'],format='%d-%m-%Y', errors='coerce')
breaddata['weekday'] = breaddata['Date'].dt.weekday
sales=breaddata['weekday'].value_counts()
new= sales.sort_index()
renamed= new.rename(index={0:'Monday',1:'Tuesday', 2:'Wednesday',3: 'Thursday', 4:'Friday', 5:'Saturday', 6: 'Sunday'})

print("\nBreads sold per weekday: \n")

print(renamed)

average=renamed.sum()/7
print("\nTransactions of bread per weekday: " + str(average)+ "\n")

renamed.plot(kind='line', color='green', marker='*')

plt.show()