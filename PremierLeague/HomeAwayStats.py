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

y = np.array([TotalHomeWins, TotalDraws, TotalAwayWins])
mylabels = ["Home Wins", "Draws", "Away Wins"]
plt.title('Percentage of Home Wins, Away Wins, and Draws')
plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90, shadow=True)
plt.show() 

print(df)