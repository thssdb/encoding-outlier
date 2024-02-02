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
figsize=(15,24) #(15,30)
size = 21
fmri = pd.read_csv("./compression_ratio/block_size_compression_ratio.csv")
# fmri = fmri[fmri["Encoding"]="TS_2DIFF","TS_2DIFF+BOS-O","TS_2DIFF+BOS-A"]
# x=['8','16','32','64','128','256','512']#
sizes = []
markers_list = []
for i in range(3):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
markers_list.append('s')
markers_list.append('>')
algorithm_order = ["TS_2DIFF+BOS-V","TS_2DIFF+BOS-L","TS_2DIFF+BOS-H"]
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]

# dataset_list = ["GW-Magnetic", "Cyber-Vehicle", "TY-Transport","YZ-Electricity"] 
int_dataset_list = ["EPM-Education","Metro-Traffic", "Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport"]
float_dataset_list = ["GW-Magnetic", "USGS-Earthquakes","Cyber-Vehicle","TY-Fuel","YZ-Electricity"]
# dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic","Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"] 
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
xticklabels_list = []
xticks_list = []
for i in range(5,14):
    xticklabels_list.append(r"$ 2^{{ {:2d} }}$".format(i))
    xticks_list.append(i)
length_x = 6
length_y = 3
fig, ax_arr = plt.subplots(length_x,length_y,figsize=figsize)

my_palette=["#ff7f00","#e31a1c", "#1178b4","#6a3d9a"]#,"#fb9a99"]#, "#814a19"]
fig.subplots_adjust(hspace=0.50)
fig.subplots_adjust(wspace=0.35)

count = 0
for dataset in int_dataset_list:
    dx = int(count )
    dy = 0
    f = sns.lineplot(x="Block Size",y="Compression Ratio",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count*3] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Ratio")
    f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1


fmri = pd.read_csv("./compression_ratio/block_size_time.csv")
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]


count = 0
for dataset in int_dataset_list:
    dx = int(count)
    dy = 1
    f = sns.lineplot(x="Block Size",y="Time",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    ax_arr[dx][dy].set_yscale("log")
    ax_arr[dx][dy].yaxis.set_major_formatter(ticker.FuncFormatter(log_scale_label))

    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count*3+1] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Compression")
    # f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1


fmri = pd.read_csv("./compression_ratio/block_size_decode_time.csv")
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]


count = 0
for dataset in int_dataset_list:
    dx = int(count)
    dy = 2
    f = sns.lineplot(x="Block Size",y="Time",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    ax_arr[dx][dy].set_yscale("log")
    ax_arr[dx][dy].yaxis.set_major_formatter(ticker.FuncFormatter(log_scale_label))

    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count*3+2] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Decompression")
    # f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1

lines, labels = ax_arr[0][0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 0.95), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=3)


fig.savefig("./figs/vary_block_size_int.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_block_size_int.png", dpi = 400,bbox_inches='tight')

# -------------------------------------------------------------------------

figsize=(15,21) #(15,30)
fmri = pd.read_csv("./compression_ratio/block_size_compression_ratio.csv")

algorithm_order = ["TS_2DIFF+BOS-V","TS_2DIFF+BOS-L","TS_2DIFF+BOS-H"]
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]


length_x = 5
length_y = 3
fig, ax_arr = plt.subplots(length_x,length_y,figsize=figsize)

fig.subplots_adjust(hspace=0.5)
fig.subplots_adjust(wspace=0.35)

count = 0
for dataset in float_dataset_list:
    dx = int(count )
    dy = 0
    f = sns.lineplot(x="Block Size",y="Compression Ratio",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count*3] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Ratio")
    f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1


fmri = pd.read_csv("./compression_ratio/block_size_time.csv")
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]


count = 0
for dataset in float_dataset_list:
    dx = int(count)
    dy = 1
    f = sns.lineplot(x="Block Size",y="Time",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    ax_arr[dx][dy].set_yscale("log")
    ax_arr[dx][dy].yaxis.set_major_formatter(ticker.FuncFormatter(log_scale_label))

    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count*3+1] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Compression")
    # f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1


fmri = pd.read_csv("./compression_ratio/block_size_decode_time.csv")
fmri = fmri[fmri["Encoding"].isin(algorithm_order)]


count = 0
for dataset in float_dataset_list:
    dx = int(count)
    dy = 2
    f = sns.lineplot(x="Block Size",y="Time",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    ax_arr[dx][dy].get_legend().remove()
    ax_arr[dx][dy].set_yscale("log")
    ax_arr[dx][dy].yaxis.set_major_formatter(ticker.FuncFormatter(log_scale_label))

    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count*3+2] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("Block Size")
    f.set_ylabel("Decompression")
    # f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1

lines, labels = ax_arr[0][0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 0.95), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=3)


fig.savefig("./figs/vary_block_size_float.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_block_size_float.png", dpi = 400,bbox_inches='tight')