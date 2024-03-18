import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/PremierLeague/pl_stats_updated.csv')
df.dropna(inplace=True)

homeWinPercent = (df["HomeWins"] / 38) * 100
awayWinPercent = (df["AwayWins"] / 38) * 100
y1 = list(homeWinPercent)
y2 = list(awayWinPercent)

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
"""
y1 = [1000, 13000, 26000, 42000, 60000, 81000]
y2 = [1000, 13000, 27000, 43000, 63000, 85000]
"""
plt.figure(figsize=(7,7))
plt.plot(x, y1, label ='Home Win Percentage')
plt.plot(x, y2, label ='Away Win Percentage')

plt.xlabel("Teams in Premier League")
plt.ylabel("Win Percentage")
plt.legend()
plt.title('Home and Away Win Percentage of Premier League Teams')
#plt.xticks(np.arange(1, 21, step=1), rotation=70)
plt.xticks(np.arange(1, 21, step=1), df["Squad"], rotation=80, fontsize=8)

plt.show()

homeWinTeamsList = []
awayWinTeamsList = []
for i in range(len(list(homeWinPercent))):
    difference = homeWinPercent[i] - awayWinPercent[i]
    if difference > 18:
        homeWinTeamsList.append({df["Squad"][i], difference})
    elif difference < 3:
        awayWinTeamsList.append({df["Squad"][i], difference})

print(homeWinTeamsList)
print(awayWinTeamsList)
