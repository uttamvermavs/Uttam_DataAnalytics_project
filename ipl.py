import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


ipl_data = {
    'Player': ['Virat Kohli', 'Rohit Sharma', 'Suryakumar', 'Shubman Gill', 'MS Dhoni', 'Rishabh Pant'],
    'Team':   ['RCB', 'MI', 'MI', 'GT', 'CSK', 'DC'],
    'Runs':   [741, 417, 518, 610, 220, 446],
    'Strike_Rate': [154.7, 150.0, 167.6, 147.0, 209.5, 155.4]
}

df = pd.DataFrame(ipl_data)
df.to_csv('ipl_short.csv', index=False)

print("\n--- IPL 2026 BATTING STATS ---")
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))


team_runs = df.groupby('Team')['Runs'].sum()


plt.figure(figsize=(12, 7))
plt.suptitle('IPL 2026 Performance Dashboard', fontsize=14, fontweight='bold')

# Graph 1: Vertical Bar Chart 
plt.subplot(2, 2, 1)
plt.bar(df['Player'], df['Runs'], color='skyblue', edgecolor='black')
plt.title('1. Runs by Player (Vertical Bar)')
plt.ylabel('Runs')
plt.xticks(rotation=20)

# Graph 2: Horizontal Bar Chart 
plt.subplot(2, 2, 2)
plt.barh(team_runs.index, team_runs.values, color='lightgreen', edgecolor='black')
plt.title('2. Team-wise Runs (Horizontal Bar)')
plt.xlabel('Total Runs')

# Graph 3: Pie Chart 
plt.subplot(2, 2, 3)
plt.pie(team_runs.values, labels=team_runs.index, autopct='%1.1f%%', startangle=140)
plt.title('3. Team Runs Contribution (Pie Chart)')

# Graph 4: Histogram 
plt.subplot(2, 2, 4)
plt.hist(df['Strike_Rate'], bins=4, color='orange', edgecolor='black')
plt.title('4. Strike Rate Distribution (Histogram)')
plt.xlabel('Strike Rate')
plt.ylabel('Players Count')

plt.tight_layout()
plt.show()