
#harini_sriya_180019
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Confidence(%)")
plt.ylabel("Rule count")
plt.title("Support level of 0.5%")
Bakery_data_set = pd.read_csv(r"G:/semester 7/Bigdata-2/Week 5/BreadBasket_DMS.csv")

Bakery_data_set= Bakery_data_set.set_index(['Item'])
filtered= Bakery_data_set.drop(['NONE'])
Bakery_data_set= Bakery_data_set.reset_index()
filtered= filtered.reset_index()
transaction_list = []


for i in filtered['Transaction'].unique():
    tlist = list(set(filtered[filtered['Transaction']==i]['Item']))
    if len(tlist)>0:
        transaction_list.append(tlist)


te = TransactionEncoder()
te_ary = te.fit(transaction_list).transform(transaction_list)
df2 = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df2, min_support=0.005, use_colnames=True)

rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.0001)

rules.sort_values('confidence', ascending=False)


rules['support']= rules['support']*100
rules['confidence']= rules['confidence']*100
rules2= rules[['antecedents','consequents', 'support', 'confidence']]

rules2.sort_values('confidence', ascending=False)
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Support Level of 0.5%: \n")
print("Confidence       count")

print(rules2['confidence'].value_counts(bins=bins, sort=False))
rules2['confidence'].value_counts(bins=bins, sort=False).plot(kind='bar', color='red')

plt.show()