import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
# 设置图表风格
sns.set_theme(style="ticks", palette="pastel")
# plt.style.use('ggplot')
size = 12
bbox_to_anchor=(0.5, 1.3)
sizes = []
markers_list = []
for i in range(4):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
markers_list.append('s')
markers_list.append('>')
my_palette=["#ff7f00","#e31a1c", "#1178b4","#6a3d9a"]
xticklabels_list = []
xticks_list = []
for i in range(6,14):
    xticklabels_list.append(r"$ 2^{{ {:2d} }}$".format(i))
    xticks_list.append(i)
algorithm_order = ["BOS-V","BOS-B","BOS-M"] #"BOS-B-Improve",

# 读取数据
data = pd.read_csv("./block_size_decode_time.csv")

# 替换编码名称简化
data.replace({'TS_2DIFF+BOS-V': 'BOS-V', 'TS_2DIFF+BOS-B': 'BOS-B', 'TS_2DIFF+BOS-M': 'BOS-M', 'TS_2DIFF+BOS-B-Improve': 'BOS-B-Improve'}, inplace=True)

# 筛选数据
data = data[data["Encoding"].isin(["BOS-V", "BOS-B", "BOS-M","BOS-B-Improve"]) & (data['Block Size'] >= 6) & (data['Block Size'] <= 13)]

# 计算每种编码在所有数据集中的平均压缩时间
average_data = data.groupby(['Block Size', 'Encoding'])['Time'].mean().reset_index()

data_ratio = pd.read_csv("./block_size_time.csv")

# 替换编码名称简化
data_ratio.replace({'TS_2DIFF+BOS-V': 'BOS-V', 'TS_2DIFF+BOS-B': 'BOS-B', 'TS_2DIFF+BOS-M': 'BOS-M', 'TS_2DIFF+BOS-B-Improve': 'BOS-B-Improve'}, inplace=True)

# 筛选数据
data_ratio = data_ratio[data_ratio["Encoding"].isin(["BOS-V", "BOS-B", "BOS-M","BOS-B-Improve"]) & (data_ratio['Block Size'] >= 6) & (data_ratio['Block Size'] <= 13)]

average_data_ratio = data_ratio.groupby(['Block Size', 'Encoding'])['Time'].mean().reset_index()

fig, ax_arr = plt.subplots(1,2,figsize=(6,2))
fig.subplots_adjust(wspace=0.35)
f = sns.lineplot(x="Block Size",y="Time",hue="Encoding",hue_order=algorithm_order,
                    markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                    ,data=average_data_ratio,ax=ax_arr[0],size='Encoding',sizes=sizes)
ax_arr[0].get_legend().remove()
# ax_arr[0].yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y:.1e}'))

f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_yscale("log")
f.set_title("(a) Compression Time").set_fontsize(size)
f.set_xlabel("Block Size")
f.set_ylabel("Compression Time (ns/block)")

f = sns.lineplot(x="Block Size",y="Time",hue="Encoding",hue_order=algorithm_order,
                    markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                    ,data=average_data,ax=ax_arr[1],size='Encoding',sizes=sizes)
ax_arr[1].get_legend().remove()
# ax_arr[1].yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y:.1e}'))

f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_yscale("log")
f.set_title("(b) Decompression Time").set_fontsize(size)
f.set_xlabel("Block Size")
f.set_ylabel("Decompression Time (ns/block)")


lines, labels = ax_arr[0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=bbox_to_anchor, loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=4)

plt.savefig("./fig/vary_block_size_time.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./fig/vary_block_size_time.png", dpi=300, bbox_inches='tight')
