import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/PremierLeague/epl_results_2022-23.csv') 
TotalHomeWins = df["Result"].str.count("H").sum()
TotalAwayWins = df["Result"].str.count("A").sum()
TotalDraws = df["Result"].str.count("D").sum()
print(TotalHomeWins)
print(TotalAwayWins)
print(TotalDraws)

explode = (0.1, 0, 0)

y = np.array([TotalHomeWins, TotalDraws, TotalAwayWins])
mylabels = ["Home Wins", "Draws", "Away Wins"]

#Fix legend
plt.legend(title = "Results", loc = "upper right", bbox_to_anchor = (1, 0, 0.5, 1), labels = mylabels, shadow = True, fontsize = "small")

plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90, shadow=True)
plt.show() 