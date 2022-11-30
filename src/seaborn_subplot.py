import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'r1': np.random.randint(1, 31, 200),
                    'dvr1': np.random.uniform(100, 1000, 200),
                    'Sample ID': np.random.randint(1, 5, 200)})
df2 = pd.DataFrame({'r1': np.random.randint(1, 31, 300),
                    'dvlnr1': np.random.uniform(300, 1200, 300),
                    'Sample ID': np.random.randint(1, 5, 300)})

# add an extra column to tell to which df the data belongs
df1['source'] = 'dvr'
# the corresponding columns in both df need to have the same name for the merge
df2 = df2.rename(columns={'dvlnr1': 'dvr1'})
df2['source'] = 'dvrnr'
df_merged = pd.concat([df1, df2]).reset_index()

g = sns.relplot(data=df_merged, x='r1', y='dvr1', hue='source', col='Sample ID', col_wrap=2,
                kind="line", height=4, aspect=1.5, palette='turbo') #
plt.subplots_adjust(bottom=0.06, left=0.06)  # plt.tight_layout() doesn't work due to legend
plt.show()