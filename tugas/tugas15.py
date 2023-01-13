import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\sales_data.csv")
print(data)

category = data['category']
sales = data['sales']

plt.bar(x=category,height=sales)

plt.show()