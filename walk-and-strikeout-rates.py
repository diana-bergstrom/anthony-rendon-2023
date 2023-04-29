import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import csv and create column names
columns = ['season','split','BB%','K%','BB/K','AVG','OBP','SLG','OPS','ISO','BABIP','wRC','wRAA','wOBA','wRC+']
standard = pd.read_csv('/kaggle/input/anthony-rendon-advanced/Tony_splits_2023 - advanced.csv', header=None, names=columns)

# use Boolean indexing to drop unwanted rows
# create copy of df
stats = standard[standard['season'] != 'Season'].copy()

# check for missing data
stats.isnull().values.any()

# convert data types of columns with numbers to float so that mathematical operations can be performed if desired
stats['BB%'] = stats['BB%'].str.replace('%', '').astype(float)
stats['K%'] = stats['K%'].str.replace('%', '').astype(float)
stats[['BB/K','AVG','OBP','SLG','OPS','ISO','BABIP','wRC','wRAA','wOBA','wRC+']] = stats[['BB/K','AVG','OBP','SLG','OPS','ISO','BABIP','wRC','wRAA','wOBA','wRC+']].astype(float)

# check that data types are correct
stats.dtypes

# copy stats df
# create df for hitting stats based on basepaths during plate appearances
desired_splits = ['Bases Empty', 'Men on Base', 'Men In Scoring']
stats_basepaths = stats.loc[stats['split'].isin(desired_splits)].copy()

# rename columns to describe basepath situation
stats_basepaths.rename(columns={43: 'Bases Empty', 44: 'Men on Base', 45: 'Men In Scoring'}, inplace=True)
# pull the desired hitting stats to plot and create bar plot
hitting_stats = ['BB%', 'K%']
stats_basepaths[hitting_stats].plot(kind='bar')

# create title
# label xaxis and xticks
plt.title('Anthony Rendon')
plt.xlabel('Basepaths')
labels = ['Bases Empty', 'Men on Base', 'Men In Scoring']
plt.xticks(range(len(labels)), labels, rotation = 0)

# save image of bar plot
plt.savefig('anthony_rendon.png')
