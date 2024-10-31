import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Font and style settings
fontsize = 12
matplotlib.rcParams.update({
    'font.size': fontsize,
    'axes.labelsize': fontsize,
    'axes.titlesize': fontsize,
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'legend.fontsize': fontsize
})

# Load data from CSV
df = pd.read_csv('./time/query_time.csv')  # Assuming 'a.csv' is your data file
df_storage = pd.read_csv('./time/storage_cost.csv')
df['Encoding'] = df['Encoding'].replace({
    'TS_2DIFF': 'BP',
    'TS_2DIFF+BOS-M': 'BOS',
    'TS_2DIFF+FASTPFOR':'FASTPFOR',
'TS_2DIFF+NEWPFOR':'NEWPFOR',
'TS_2DIFF+OPTPFOR':'OPTPFOR',
'TS_2DIFF+PFOR':'PFOR'
})
df_storage['Encoding'] = df_storage['Encoding'].replace({
    'TS_2DIFF': 'BP',
    'TS_2DIFF+BOS-M': 'BOS',
        'TS_2DIFF+FASTPFOR':'FASTPFOR',
'TS_2DIFF+NEWPFOR':'NEWPFOR',
'TS_2DIFF+OPTPFOR':'OPTPFOR',
'TS_2DIFF+PFOR':'PFOR'
})
# Prepare the data for plotting

df = df.drop(columns=['Dataset'])
df = df.groupby('Encoding').mean().reset_index()
df['index'] = 'Compressions'


df_storage = df_storage.drop(columns=['Dataset'])
df_storage = df_storage.groupby('Encoding').mean().reset_index()
df_storage['index'] = 'Compressions'

# print(df)
# print(df_storage)

# df_storage_grouped = df_storage.pivot(index='index', columns='Encoding', values='Storage Cost')

# df_grouped_input = df.pivot(index='index', columns='Encoding', values='Output Time')
# df_grouped_encode = df.pivot(index='index', columns='Encoding', values='Decode Time')

fig, axs = plt.subplots(1, 2, figsize=(6, 2))
fig.subplots_adjust(wspace=0.3)
# fig.subplots_adjust(wspace=0.9)
colors = ['#ff7f00', '#e31a1c',"#1178b4", "#33a02c", "#6a3d9a","#ffff00"]   # Orange and Red for TS_2DIFF and TS_2DIFF+BOS-M respectively
# Plotting Storage Cost
axs[0].bar(df_storage['Encoding'], df_storage['Storage Cost'], color=colors[2])
axs[0].set_xlabel('Operators')
axs[0].set_ylabel('Storage Cost (byte)')
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=30, ha="right")
axs[0].set_title('(a) Storage Cost')

axs[1].bar(df['Encoding'], df['Decode Time'], label='Decompression Time', color=colors[0])
axs[1].bar(df['Encoding'], df['Output Time'], bottom=df['Decode Time'], label='IO Time', color=colors[1])
axs[1].set_xlabel('Operators')
axs[1].set_ylabel('Query Time (ns/point)')
axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=30, ha="right")
axs[1].set_title('(b) Query Time')
# axs[1].legend()
# axs[0].get_legend().remove()



# df_grouped_input = df_grouped_input.reindex_like(df_grouped_encode)

# df_grouped_input.plot.bar(ax=axs[0], stacked=True, color=colors, alpha=0.7, label='Output Time')

# bottom_values = df_grouped_input.values #.flatten()

# df_grouped_encode.plot.bar(ax=axs[0], stacked=True, bottom=bottom_values, color=colors, alpha=0.5, label='Decode Time')

# axs[0].set_xticklabels([])
# axs[0].set_xlabel('Encoding')
# axs[0].set_ylabel('Time (ns/byte)')
# axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=45, ha="center")

# axs[0].get_legend().remove()

# df_storage_grouped.plot.bar(ax=axs[1], color=colors, alpha=0.7)
# axs[1].set_xticklabels([])
# axs[1].set_xlabel('Encoding')
# axs[1].set_ylabel('Storage Cost (byte)')
# axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=45, ha="center")

# axs[1].get_legend().remove()

lines, labels = axs[1].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.64, 1.2), loc='upper center', fontsize=fontsize, labelspacing=0.1, handletextpad=0.1, columnspacing=0.1, ncol=2)

# plt.tight_layout()

fig.savefig("./fig/query_time_comparison.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./fig/query_time_comparison.png", dpi=400, bbox_inches='tight')


