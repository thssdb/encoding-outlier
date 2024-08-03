import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib.ticker import FormatStrFormatter
import matplotlib
from matplotlib.ticker import LogFormatter
from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib.ticker as ticker

fontsize = 18
matplotlib.rcParams.update({
    'font.size': fontsize,
    'axes.labelsize': fontsize,
    'axes.titlesize': fontsize,
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'legend.fontsize': fontsize
})
# Data Preparation
path_ratio_v = './compression_ratio/exp_v/'
path_ratio_b = './compression_ratio/exp_b/'
path_ratio_m = './compression_ratio/exp_m/'

dir_r_exp = ['Exp_100','Exp_1000','Exp_10000','Exp_100000','Exp_1000000'] 
dir_r_normal = ['Normal_100','Normal_1000','Normal_10000','Normal_100000','Normal_1000000'] 
stds = [100,1000,10000,100000,1000000]

# Collect data for all experiments and normals for v, b, m
def collect_data(path, dirs):
    results = []
    for j in dirs:
        file_path = os.path.join(path, j + ".csv")
        df = pd.read_csv(file_path)
        # print(path)
        method = ''
        if str(path).split('_')[2] == 'v/':
            method = "BOS-V"
        elif str(path).split('_')[2] == 'b/':
            method = "BOS-B"
        elif str(path).split('_')[2] == 'm/':
            method = "BOS-M"

        results.append({
            'std': int(j.split('_')[1]),
            'Compression Ratio': 1 / df['Compression Ratio'].values[0],
            'Encoding Time': df['Encoding Time'].values[0] / 10240,
            'Decoding Time': df['Decoding Time'].values[0] / 10240,
            'Type': 'Exp' if 'Exp' in j else 'Normal',
            'Method': method  # 'V', 'B', 'M'
        })
    return pd.DataFrame(results)

# Combine data from all methods and types
data = pd.concat([
    collect_data(path_ratio_v, dir_r_exp + dir_r_normal),
    collect_data(path_ratio_b, dir_r_exp + dir_r_normal),
    collect_data(path_ratio_m, dir_r_exp + dir_r_normal)
], ignore_index=True)

# Styling and plotting
sns.set_theme(style="ticks", palette="pastel")
# plt.rcParams.update({'font.size': 20})
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
fig.subplots_adjust(hspace=0.35, wspace=0.3)
palette = {"BOS-V": "#ff7f00", "BOS-B": "#e31a1c", "BOS-M": "#1178b4"}

plot_data = [
    ("Compression Ratio", 'Compression Ratio',None)
    # ("Encoding Time", 'Compression Time', 'log'),
    # ("Decoding Time", 'Decompression Time', 'log')
]

def log_tick_formatter(val, pos):
    return f'$10^{{{int(np.log10(val))}}}$' if val != 0 else '1'
sizes = []
markers_list = []
for i in range(3):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
markers_list.append('s')
markers_list.append('>')
for i, (metric, ylabel, scale) in enumerate(plot_data):

    for j, type_group in enumerate(['Exp', 'Normal']):
        ax = axs[j]
        sns.lineplot(data=data[data['Type'] == type_group], x='std', y=metric, hue='Method',
                      markers=markers_list, markersize=10, ax=ax, style='Method', 
                      dashes=False, palette=palette,size='Method',sizes=sizes)
        ax.set_xscale('log')
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'$10^{{{int(math.log10(x))}}}$'))
        ax.set_xticks([100, 1000, 10000, 100000, 1000000])
        # ax.xaxis.set_major_formatter(FuncFormatter(log_tick_formatter))
        if scale == 'log':
            ax.set_yscale('log')
            if ylabel == "Decompression Time":
                ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'$10^{{{int(math.log10(y))}}}$'))
                ax.set_yticks([1, 10, 100, 1000])
        ax.tick_params(labelsize = fontsize)
        if type_group == 'Exp':
            ax.set_title(f"({chr(97 + j + i)}) Exponential Distribution", fontsize=fontsize)
            ax.set_xlabel(r'$\lambda^{-1}$', fontsize=fontsize)
        else:
            ax.set_title(f"({chr(97 + j + i)}) {type_group} Distribution", fontsize=fontsize)
            ax.set_xlabel(r'Standard Deviation', fontsize=fontsize)
        
        ax.set_yticks(np.linspace(1,4,num = 7))
        ax.set_ylabel(ylabel, fontsize=fontsize)
        
        # Remove individual legends
        ax.get_legend().remove()
        # ax.xaxis.set_major_formatter(formatter) 
        # ax.set_xticks(stds)  # Show all standard deviations as ticks
        # ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())  # Ensure non-scientific format

# Create a unified legend
lines, labels = axs[0].get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3, fontsize=fontsize)
fig.legend(lines, labels, bbox_to_anchor=(0.5, 1.10), loc = 'upper center',fontsize=fontsize,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=3)

# Save and show
fig.savefig("./figs/normal_data_test.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./figs/normal_data_test.png", dpi=400, bbox_inches='tight')
# plt.show()
