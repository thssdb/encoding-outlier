import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Font and style settings
fontsize = 11
matplotlib.rcParams.update({
    'font.size': fontsize,
    'axes.labelsize': fontsize,
    'axes.titlesize': fontsize,
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'legend.fontsize': fontsize
})

# # Paths to data
# base_path = 'compression_ratio'
# bos_path = os.path.join(base_path,  'bos')
# outlier_bos_path = os.path.join(base_path, 'lower_outlier_bos')
# tsdiff_path = os.path.join(base_path, 'tsdiff')

# # Function to load data from a folder
# def load_data(folder):
#     data = {}
#     for file in os.listdir(folder):
#         if file.endswith(".csv"):
#             df = pd.read_csv(os.path.join(folder, file))
#             data[file[:-4]] = df.iloc[0]  # Assuming data is in the first row
#     return data

# # Load data from both directories
# bos_data = load_data(bos_path)
# outlier_bos_data = load_data(outlier_bos_path)
# tsdiff_data = load_data(tsdiff_path)

# # Create dataframe for plotting
# data = []
# desired_order = ['TH-Climate_ratio', 'Exp_100', 'Exp_1000', 'Exp_10000', 'Exp_100000', 'Exp_1000000']

# # Create dataframe for plotting
# data = []
# for key in desired_order:
#     if key in bos_data and key in outlier_bos_data and key in tsdiff_data:
#         data.append({
#             'Dataset': key,
#             'BOS': 1 / bos_data[key]['Compression Ratio'],
#             'Only_Upper_Outlier': 1 / outlier_bos_data[key]['Compression Ratio'],
#             'BP': 1 / tsdiff_data[key]['Compression Ratio'],
#             'BOS Encoding Time': bos_data[key]['Encoding Time'] / bos_data[key]['Points'],
#             'Only Upper Outlier Encoding Time': outlier_bos_data[key]['Encoding Time'] / outlier_bos_data[key]['Points'],
#             'BP Encoding Time': tsdiff_data[key]['Encoding Time'] / tsdiff_data[key]['Points'],
#         })

desired_order= ["LZ4", "BOS+LZ4","7-Zip", "BOS+7-Zip","DCT" ,"BOS+DCT", "FFT","BOS+FFT"]
compression_order = ["LZ4", "7-Zip","DCT" , "FFT"]
compression_complementary_order = ["BOS+LZ4", "BOS+7-Zip","BOS+DCT", "BOS+FFT"]

# df = pd.DataFrame(data)
df = pd.read_csv("./compression_ratio/compression_ratio.csv")

df = df.drop(columns=['Dataset'])
df = df.groupby('Compression').mean().reset_index()
df['index'] = 'Compressions'
df = df[df["Compression"].isin(["LZ4", "BOS+LZ4","7-Zip", "BOS+7-Zip","DCT" ,"BOS+DCT", "FFT","BOS+FFT"])]
df['Compression'] = pd.Categorical(df['Compression'], categories=desired_order, ordered=True)
df = df.sort_values('Compression')
# print(df)
plot_data = {
    'Label': compression_order,
    'Without BOS': df[df['Compression'].isin(compression_order)].set_index('Compression').loc[compression_order, 'Compression Ratio'].values,
    'With BOS': df[df['Compression'].isin(compression_complementary_order)].set_index('Compression').loc[compression_complementary_order, 'Compression Ratio'].values
}
df = pd.DataFrame(plot_data)


df_time = pd.read_csv("./compression_ratio/time.csv")
df_time = df_time.drop(columns=['Dataset'])
df_time = df_time.groupby('Compression').mean().reset_index()
df_time['index'] = 'Compressions'
df_time = df_time[df_time["Compression"].isin(["LZ4", "BOS+LZ4","7-Zip", "BOS+7-Zip","DCT" ,"BOS+DCT", "FFT","BOS+FFT"])]
df_time['Compression'] = pd.Categorical(df_time['Compression'], categories=desired_order, ordered=True)
df_time = df_time.sort_values('Compression')
print(df_time)

plot_data = {
    'Label': compression_order,
    'Without BOS': df_time[df_time['Compression'].isin(compression_order)].set_index('Compression').loc[compression_order, 'Compression Time'].values,
    'With BOS': df_time[df_time['Compression'].isin(compression_complementary_order)].set_index('Compression').loc[compression_complementary_order, 'Compression Time'].values
}
df_time = pd.DataFrame(plot_data)

# print(df)
# Plotting
fig, axs = plt.subplots(1, 2, figsize=(6, 2))
# fig.subplots_adjust(hspace=0.5)
fig.subplots_adjust(wspace=0.3)
colors = ['#ff7f00', '#e31a1c', '#1178b4', '#33a02c', '#6a3d9a', '#b15928', '#cab2d6']

df.plot.bar(x='Label', y=['With BOS', 'Without BOS'], ax=axs[0], color=colors[:2], alpha=0.7)
# axs[0].bar(df['Compression'], df['Compression Ratio'],  color=colors[2])
axs[0].set_xlabel('Compression Methods')
axs[0].set_ylabel('Compression Ratio')
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=0, ha="center")
axs[0].set_title('(a) Compression Ratio')
axs[0].get_legend().remove()

# Plotting Storage Cost
# axs[1].bar(df_time['Compression'], df_time['Compression Time'], color=colors[0])


df_time.plot.bar(x='Label', y=['With BOS', 'Without BOS'], ax=axs[1], color=colors[:2], alpha=0.7)
axs[1].set_xlabel('Compression Methods')
axs[1].set_ylabel('Compression Time (ns/point)')
axs[1].set_yscale('log')
axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=00, ha="center")
axs[1].set_title('(b) Compression Time')
axs[1].get_legend().remove()

lines, labels = axs[0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 1.21), loc='upper center', fontsize=fontsize, labelspacing=0.2, handletextpad=0.2, columnspacing=0.8, ncol=3)

# Adjust layout
# plt.tight_layout()
fig.savefig("./fig/compare_compression.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./fig/compare_compression.png", dpi=400, bbox_inches='tight')
