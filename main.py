import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('QueryResults.csv', names =['DATE', 'TAG', 'POSTS'], header=0)


df.shape
df.groupby('TAG').sum()
df.groupby('TAG').count()
type(df['DATE'][1])
df.DATE=pd.to_datetime(df.DATE)
#pivot
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS').fillna(0)
print(reshaped_df)

#specific chart/graph creation
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('Number of Posts', fontsize = 14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df['java'])
plt.plot(reshaped_df.index, reshaped_df['python'])

#The window is the number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

#chart/graph creation for a columns
for column in roll_df.columns:
  plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)