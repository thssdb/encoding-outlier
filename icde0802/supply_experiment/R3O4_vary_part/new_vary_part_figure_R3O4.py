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

# Paths to data
base_path = 'compression_ratio'
folders = ['bos_1','bos_2','bos_3', 'bos_4', 'bos_5', 'bos_6','bos_7']
parts = [1, 2, 3, 4, 5, 6, 7]

# Create data structures for storing the values
compression_ratios = []
encoding_times = []
datasets_list = ["EPM-Education","Metro-Traffic", "Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","GW-Magnetic", "USGS-Earthquakes","Cyber-Vehicle","TY-Fuel","YZ-Electricity","Nifty-Stocks"] 


# Initialize DataFrame
df_data = []

# Load data from CSV files in the specified folders
for dataset in datasets_list:
    for folder, part in zip(folders, parts):
        file_path = os.path.join(base_path, folder, dataset+"_ratio.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            compression_ratio = 1/df['Compression Ratio'].iloc[0]
            compression_time = df['Encoding Time'].iloc[0]/df['Points'].iloc[0]
            df_data.append({
                'Dataset': dataset,
                'Part': part,
                'Compression Ratio': compression_ratio,
                'Compression Time': compression_time
            })
        else:
            df_data.append({
                'Dataset': dataset,
                'Part': part,
                'Compression Ratio': None,
                'Compression Time': None
            })

# Create DataFrame
df = pd.DataFrame(df_data)

df = df.drop(columns=['Dataset'])
df = df.groupby('Part').mean().reset_index()
# Plotting
fig, axs = plt.subplots(1, 2, figsize=(6, 3))
# colors = [
#     '#ff7f00', '#377eb8', '#4daf4a', '#e41a1c',  
#     '#984ea3', '#ff7f00', '#ffff33', '#a65628',  
#     '#f781bf', '#999999', '#1b9e77', '#d95f02'   
# ]
# for idx, dataset in enumerate(datasets_list):
#     dataset_df = df[df['Dataset'] == dataset]
#     axs[0].plot(dataset_df['Part'], dataset_df['Compression Ratio'], marker='o', label=dataset, color=colors[idx % len(colors)])
#     axs[1].plot(dataset_df['Part'], dataset_df['Compression Time'], marker='o', label=dataset, color=colors[idx % len(colors)])


# Compression Ratio plot
axs[0].plot(df['Part'], df['Compression Ratio'], marker='o', color='#ff7f00')
axs[0].set_title('(a) Compression Ratio')
axs[0].set_xlabel('# Parts')
axs[0].set_ylabel('Compression Ratio')

# Encoding Time plot
axs[1].plot(df['Part'], df['Compression Time'], marker='o', color='#e31a1c')
axs[1].set_title('(b) Compression Time')
axs[1].set_xlabel('# Parts')
axs[1].set_ylabel('Compression Time (ns/point)')
# axs[1].set_yscale('log')

# Adjust layout and legend
for ax in axs:
    ax.set_xticks(parts)  # Ensure all parts are marked on x-axis

plt.tight_layout()

# handles, labels = [], []
# for ax in axs:
#     for handle, label in zip(*ax.get_legend_handles_labels()):
#         handles.append(handle)
#         labels.append(label)

# Create a figure-wide legend at the top
# fig.legend(handles, labels, bbox_to_anchor=(0.5, 1.00), loc='lower center', fontsize=fontsize, labelspacing=0.2, handletextpad=0.2, columnspacing=0.8, ncol=len(datasets_list)/3)


# Save figures
fig.savefig("./fig/varying_part.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./fig/varying_part.png", dpi=400, bbox_inches='tight')

# Show the plot
# plt.show()
