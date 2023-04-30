import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import csv
hittingstats = pd.read_csv('/kaggle/input/teamstats/tonyleadoff_teamstats.csv')

# rename columns
hittingstats.rename(columns={'Date': 'date', 'Opposing Team': 'opponent', 'Inning': 'inning', 'Tony PA Result': 'tony result', 'PA': 'plate appearances', 'AB': 'at bats', 'H': 'hits', 'BB': 'walks', 'RBI': 'runs batted in', 'AVG': 'average', 'Runs': 'runs scored', '1B': 'singles', '2B': 'doubles', '3B': 'triples', 'HR': 'homeruns', 'SO': 'strikeouts', 'GIDP': 'ground into double plays', 'SB': 'stolen bases', 'CS': 'caught stealing'}, inplace=True)

# add OBP column
hittingstats['on base percentage'] = (hittingstats['hits'] + hittingstats['walks']) / \
                      (hittingstats['at bats'] + hittingstats['walks'])

# check for missing data
hittingstats.isnull().values.any()

# covert to float data type
hittingstats[['plate appearances','at bats','hits','walks','runs batted in','runs scored','singles','doubles','triples','homeruns','strikeouts','ground into double plays','stolen bases','caught stealing']] = hittingstats[['plate appearances','at bats','hits','walks','runs batted in','runs scored','singles','doubles','triples','homeruns','strikeouts','ground into double plays','stolen bases','caught stealing']].astype(int)
hittingstats[['opponent','inning','tony result']] = hittingstats[['opponent','inning','tony result']].astype('category')
hittingstats['date'] = pd.to_datetime(hittingstats['date'])

# check that data types are correct
hittingstats.dtypes

# create a subset of the hittingstats dataframe that only includes the team's stats
teamstats = hittingstats.groupby('opponent').sum()

# create a figure with two axes for the two plots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(17, 7))

# plot the total hits and runs scored
teamstats[['hits', 'runs scored']].plot(kind='bar', ax=ax1)
ax1.set_xlabel('Opponent')
ax1.set_title("LAA hits and runs scored during innings that Tony bats first")
ax1.tick_params(axis='x', labelrotation=0)

# group the hittingstats dataframe by opponent and calculate the mean of average and OBP columns
stats_vs_opp = hittingstats.groupby('opponent')[['average', 'on base percentage']].mean()

# create a stacked bar chart of opponent average and OBP in the second axis
stats_vs_opp.plot(kind='bar', ax=ax2)

# add horizontal line for LAA team average
laa_avg = .253
ax2.axhline(y=laa_avg, color='blue', linestyle='--', label='LAA team AVG')
ax2.legend()

# add horizontal line for LAA team average OBP
laa_obp = .333
ax2.axhline(y=laa_obp, color='orange', linestyle='--', label='LAA avg OBP')
ax2.legend()

# add title and labels
ax2.set_xlabel('Opponent')
ax2.set_title("LAA team avg and obp during innings that Tony bats first")
ax2.tick_params(axis='x', labelrotation=0)

# move legend outside the plot area
ax2.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

plt.savefig('teamstats.png')
