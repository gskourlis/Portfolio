import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("/Users/georgiosskourlis/Documents/Sports Analytics School/Final Assignment/Second task/above_average.csv")

players_age = list(df['age'])

avg_score=[]
age=[]
for i,r in df.iterrows():
    if r['age'] >=30:
        avg_score.append(r['score'])
        age.append(r['age'])


colors= np.random.rand(15,3)

plt.scatter(df['age'],df['score'],alpha=0.2,label="All Players")
plt.scatter(age,avg_score,c=colors,label="Players Over 30")
plt.grid(True, alpha=0.2)
plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.legend(loc='upper right',prop={"size":6})
plt.text(5, 0.9, 'All Players', fontsize=5, color='blue')
plt.text(5, 0.8, 'Players Over 30', fontsize=5, color='orange')
plt.show()