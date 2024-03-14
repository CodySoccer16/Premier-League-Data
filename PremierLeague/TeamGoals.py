import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

df = pd.read_csv('data/PremierLeague/pl_stats_3.csv')
df.dropna(inplace=True)
df.sort_values(by=["Squad"], inplace=True)

newdf = df[["Squad", "Wins", "Win%", "Poss", "Gls"]]
squads = list(newdf['Squad'])

x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
y = np.array(list(df['Gls']))
my_xticks = squads
plt.xticks = (x, my_xticks)
plt.xlabel('Team')
plt.ylabel('Goals Scored')
plt.title('Goals scored for each Premier League Teams')
plt.plot(my_xticks, y)
plt.show()
"""
x = np.array([0,1,2,3])
y = np.array([20,21,22,23])
my_xticks = ['John','Arnold','Mavis','Matt']
plt.xticks(x, my_xticks)
plt.plot(x, y)
plt.show()
"""

#Working without label
"""
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
y = np.array(df['Win%'])
my_xticks = newdf['Squad']
plt.xticks = (x, my_xticks)
plt.plot(x, y)
plt.xlabel('Team')
plt.ylabel('Win Percentage')
plt.title('Win Percentage of Premier League Teams')
plt.show()
"""