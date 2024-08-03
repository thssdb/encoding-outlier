import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker
plt.style.use('ggplot')
import matplotlib
def log_scale_label(x, pos):
    return f'$10^{int(math.log10(x))}$'

# "Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Cyber-Vehicle", "TH-Climate", "TY-Fuel", "TY-Transport"
sns.set_theme(style="ticks", palette="pastel")
figsize=(20,13) #(15,30)
size = 17
fmri = pd.read_csv("./compression_ratio/block_size_compression_ratio.csv")
# fmri = fmri[fmri["Encoding"]="TS2DIFF","BOS-O","BOS-A"]
# x=['8','16','32','64','128','256','512']#
# print(fmri)
fmri.replace('TS_2DIFF+BOS-V', 'BOS-V', inplace=True)
fmri.replace('TS_2DIFF+BOS-B', 'BOS-B', inplace=True)
fmri.replace('TS_2DIFF+BOS-M', 'BOS-M', inplace=True)
bbox_to_anchor=(0.5, 0.95)
sizes = []
markers_list = []
for i in range(3):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
markers_list.append('s')
markers_list.append('>')
algorithm_order = ["BOS-V","BOS-B","BOS-M"]
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]

# dataset_list = ["GW-Magnetic", "Cyber-Vehicle", "TY-Transport","YZ-Electricity"] 
int_dataset_list = ["EPM-Education","Metro-Traffic", "Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport"]
float_dataset_list = ["GW-Magnetic", "USGS-Earthquakes","Cyber-Vehicle","TY-Fuel","YZ-Electricity","Nifty-Stocks"]
# dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic","Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"] 
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
xticklabels_list = []
xticks_list = []
for i in range(6,14):
    xticklabels_list.append(r"$ 2^{{ {:2d} }}$".format(i))
    xticks_list.append(i)
length_x = 3
length_y = 4
fig, ax_arr = plt.subplots(length_x,length_y,figsize=figsize)

my_palette=["#ff7f00","#e31a1c", "#1178b4","#6a3d9a"]#,"#fb9a99"]#, "#814a19"]
fig.subplots_adjust(hspace=0.4)
fig.subplots_adjust(wspace=0.35)
fmri = fmri[(fmri['Block Size'] >= 6) & (fmri['Block Size'] <= 13)]

# print(fmri)
count = 0
for dataset in int_dataset_list:
    dx = int(count/4)
    dy = int(count%4)

    f = sns.lineplot(x="Block Size",y="Compression Ratio",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    
    ax_arr[dx][dy].get_legend().remove()
    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Compression Ratio")
    f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1



# figsize=(15,24) #(15,30)
fmri = pd.read_csv("./compression_ratio/block_size_compression_ratio.csv")
fmri.replace('TS_2DIFF+BOS-V', 'BOS-V', inplace=True)
fmri.replace('TS_2DIFF+BOS-B', 'BOS-B', inplace=True)
fmri.replace('TS_2DIFF+BOS-M', 'BOS-M', inplace=True)
algorithm_order = ["BOS-V","BOS-B","BOS-M"]
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]
fmri = fmri[(fmri['Block Size'] >= 6) & (fmri['Block Size'] <= 13)]


# count = 0
for dataset in float_dataset_list:
    dx = int(count/4)
    dy = int(count%4)
    f = sns.lineplot(x="Block Size",y="Compression Ratio",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Compression Ratio")
    f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1



lines, labels = ax_arr[0][0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=bbox_to_anchor, loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=3)


fig.savefig("./figs/vary_block_size.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_block_size.png", dpi = 400,bbox_inches='tight')