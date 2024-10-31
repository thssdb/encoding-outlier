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
bos_path = os.path.join(base_path,  'bos')
# outlier_bos_path = os.path.join(base_path, 'lower_outlier_bos')
outlier_bos_path = os.path.join(base_path, 'lower_outlier_bos')
# tsdiff_path = os.path.join(base_path, 'tsdiff')

# Function to load data from a folder
def load_data(folder):
    data = {}
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, file))
            data[file[:-4]] = df.iloc[0]  # Assuming data is in the first row
    return data

# Load data from both directories
bos_data = load_data(bos_path)
outlier_bos_data = load_data(outlier_bos_path)
# tsdiff_data = load_data(tsdiff_path)

######
# TSDIFF BOS-B real datasets bos
# RLE BOS-B synthetic datasets bos
#  TSDIFF BOS-B OUO real datasets lower_outlier_bos
#  RLE BOS-B OUO synthetic datasets lower_outlier_bos
######


# Create dataframe for plotting
data = []
dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]
dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel",'Nifty-Stocks']
for i in range(len(dir_r)):
    dir_r[i] = dir_r[i] + "_ratio"
# desired_order = ["EPM-Education_ratio","GW-Magnetic_ratio","Metro-Traffic_ratio", "Nifty-Stocks_ratio", "USGS-Earthquakes_ratio", "Vehicle-Charge_ratio","CS-Sensors_ratio", "Cyber-Vehicle_ratio",
#                 "TH-Climate_ratio", "TY-Fuel_ratio","TY-Transport_ratio","YZ-Electricity_ratio"]
                # 'Exp_100', 'Exp_1000', 'Exp_10000', 'Exp_100000', 'Exp_1000000',
                # 'Normal_100', 'Normal_1000', 'Normal_10000', 'Normal_100000', 'Normal_1000000']

desired_order1 = [ 'Metro-Traffic_ratio',  'Vehicle-Charge_ratio', 'CS-Sensors_ratio', 'TH-Climate_ratio']
desired_order2 = ['GW-Magnetic_ratio','TY-Transport_ratio','USGS-Earthquakes_ratio', 'Nifty-Stocks_ratio', 'EPM-Education_ratio','Cyber-Vehicle_ratio',  'TY-Fuel_ratio',  'YZ-Electricity_ratio'] 
desired_order3 = ['Exp_100', 'Exp_1000', 'Exp_10000', 'Exp_100000', 'Exp_1000000']
desired_order4 = ['Normal_100', 'Normal_1000', 'Normal_10000', 'Normal_100000', 'Normal_1000000']


# Create dataframe for plotting  Upper and Lower Outliers vs Lower Outliers Only
data = []
for key in dir_r:
    if key in bos_data and key in outlier_bos_data : #and key in tsdiff_data:
        data.append({
            'Dataset': key,
            'Upper and Lower Outliers': 1 / bos_data[key]['Compression Ratio'],
            'Upper Outliers Only': 1 / outlier_bos_data[key]['Compression Ratio'],
            # 'BP': 1 / tsdiff_data[key]['Compression Ratio'],
            'BOS Encoding Time': bos_data[key]['Encoding Time'] / bos_data[key]['Points'],
            'Only Upper Outlier Encoding Time': outlier_bos_data[key]['Encoding Time'] / outlier_bos_data[key]['Points'],
            # 'BP Encoding Time': tsdiff_data[key]['Encoding Time'] / tsdiff_data[key]['Points'],
        })
def format_label(label):
    parts = label.split('-')
    if len(parts) > 1:
        return parts[0] + '-' + parts[1].replace('_ratio', '')
    return label
# print(data)
df = pd.DataFrame(data)

def assign_label(row):
    if row['Dataset'] in desired_order1:
        return 'Normal Real'
    elif row['Dataset'] in desired_order2:
        return 'Exp Real'
    elif row['Dataset'] in desired_order3:
        return 'Normal Synthetic'
    elif row['Dataset'] in desired_order4:
        return 'Exp Synthetic'
    else:
        return 'Unknown'

# Apply labels
# df['Label'] = df.apply(assign_label, axis=1)
# print(df)
# print(df)
# df = df.drop(columns=['Dataset'])

# Calculate averages by label
# average_results = df.groupby('Label').mean().reset_index()


# Plotting
fig, axs = plt.subplots(1, 1, figsize=(6, 2))
fig.subplots_adjust(wspace=0.8)
fig.subplots_adjust(hspace=0.8)
colors = ['#e31a1c',"#1178b4", '#ff7f00'] 

# Compression Ratio Comparison
df.plot.bar(x='Dataset', y=['Upper and Lower Outliers', 'Upper Outliers Only'],
            ax=axs, color=colors, alpha=0.7)
# axs.set_title('(a) Compression Ratio')
axs.set_ylabel('Compression Ratio')
axs.set_xlabel('Dataset')
# axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=30, ha="right")
# print(axs[0].get_xticklabels())
axs.set_xticklabels([format_label(label) for label in df['Dataset']], rotation=30, ha="right")
axs.get_legend().remove()

# axs[0].set_xlabel('Dataset')

# Encoding Time Comparison
# df.plot.bar(x='Dataset', y=['BOS Encoding Time', 'Only Upper Outlier Encoding Time'],
#             ax=axs[1], color=colors, alpha=0.7)
# axs[1].set_title('(b) Compression Time')
# axs[1].set_ylabel('Compression Time (ns/point)')
# axs[1].set_xlabel('Dataset')
# axs[1].set_yscale('log')
# axs[1].set_yticks([10, 100, 1000])
# # axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=30, ha="right")
# axs[1].set_xticklabels([format_label(label) for label in df['Dataset']], rotation=30, ha="right")
# # axs[1].set_xlabel('Dataset')
# for ax in axs:
#     ax.get_legend().remove()

# Create a unified legend at a specified location
lines, labels = axs.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 1.07), loc='upper center', fontsize=fontsize, labelspacing=0.2, handletextpad=0.2, columnspacing=0.8, ncol=3)

# Adjust layout
# plt.tight_layout()
fig.savefig("./fig/down_outlier_compare.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./fig/down_outlier_compare.png", dpi=400, bbox_inches='tight')
