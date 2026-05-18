import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
matches = pd.read_csv(r"C:\Users\Siri Reddy\OneDrive\Desktop\KODBUD\Task 3\archive (3)\matches.csv")
deliveries = pd.read_csv(r"C:\Users\Siri Reddy\OneDrive\Desktop\KODBUD\Task 3\archive (3)\deliveries.csv")

# -----------------------------------
# Most Winning Teams
# -----------------------------------

wins = matches['winner'].value_counts().head(10)

print("Most Winning Teams:\n")
print(wins)

plt.figure(figsize=(10,5))
wins.plot(kind='bar')

plt.title("Most Winning IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.show()

# -----------------------------------
# Top Scorers
# -----------------------------------

top_scorers = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

print("\nTop Scorers:\n")
print(top_scorers)

plt.figure(figsize=(10,5))
top_scorers.plot(kind='bar')

plt.title("Top IPL Scorers")
plt.xlabel("Players")
plt.ylabel("Runs")

plt.show()

# -----------------------------------
# Stadium Trends
# -----------------------------------

stadium_matches = matches['venue'].value_counts().head(10)

print("\nTop Stadiums:\n")
print(stadium_matches)

plt.figure(figsize=(10,5))
stadium_matches.plot(kind='bar')

plt.title("Matches Played in Stadiums")
plt.xlabel("Stadium")
plt.ylabel("Number of Matches")

plt.show()