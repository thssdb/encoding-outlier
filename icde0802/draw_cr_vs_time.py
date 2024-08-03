import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

path_ratio = './compression_ratio.csv'  
dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","Nifty-Stocks","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel"]
# encoding_list = ["GORILLA","CHIMP","Elf","BUFF","FASTPFOR","NEWPFOR","OPTPFOR","RLE","RLE+BOS-O","RLE+BOS-A","RLE+PFOR","SPRINTZ","SPRINTZ+BOS","SPRINTZ+Amortization","SPRINTZ+PFOR","TS_2DIFF","TS_2DIFF+BOS-O","TS_2DIFF+BOS-A","TS_2DIFF+PFOR"]
encoding_list = ["GORILLA","CHIMP","Elf","BUFF","RLE+BP","RLE+PFOR","RLE+NEWPFOR","RLE+OPTPFOR","RLE+FASTPFOR","RLE+BOS-V","RLE+BOS-B","RLE+BOS-M",
                 "SPRINTZ+BP","SPRINTZ+PFOR","SPRINTZ+NEWPFOR","SPRINTZ+OPTPFOR","SPRINTZ+FASTPFOR","SPRINTZ+BOS-V","SPRINTZ+BOS-B","SPRINTZ+BOS-M",
                 "TS2DIFF+BP","TS2DIFF+PFOR","TS2DIFF+NEWPFOR","TS2DIFF+OPTPFOR","TS2DIFF+FASTPFOR","TS2DIFF+BOS-V","TS2DIFF+BOS-B","TS2DIFF+BOS-M"]
datasets = ["EE","MT","VC","CS","TC","TT","YE","GM","UE","CV","TF"]
size = 23

df = pd.read_csv("./compression_ratio/compression_ratio.csv")

df.replace('RLE', 'RLE+BP', inplace=True)
df.replace('SPRINTZ', 'SPRINTZ+BP', inplace=True)
df.replace('TS_2DIFF', 'TS_2DIFF+BP', inplace=True)
df.replace(to_replace=r'TS_2DIFF', value='TS2DIFF', regex=True, inplace=True)
# df.replace('TS_2DIFF', 'TS2DIFF', inplace=True)
# df = df[df['Dataset'] != 'Nifty-Stocks']

result_df = df.groupby('Encoding')['Compression Ratio'].mean().reset_index()
# print(result_df)
compression_ratios = []
for encoding in encoding_list:
    new_df = result_df[result_df['Encoding'] == encoding]
    ratio = new_df['Compression Ratio'].values[0]
    compression_ratios.append(ratio)

df = pd.read_csv("./compression_ratio/encode_time.csv")
df.replace('RLE', 'RLE+BP', inplace=True)
df.replace('SPRINTZ', 'SPRINTZ+BP', inplace=True)
df.replace('TS_2DIFF', 'TS_2DIFF+BP', inplace=True)
# df.replace('TS_2DIFF', 'TS2DIFF', inplace=True)
df.replace(to_replace=r'TS_2DIFF', value='TS2DIFF', regex=True, inplace=True)
# df = df[df['Dataset'] != 'Nifty-Stocks']

result_df = df.groupby('Encoding')['Encoding Time'].mean().reset_index()
average_times = []
for encoding in encoding_list:
    new_df = result_df[result_df['Encoding'] == encoding]
    encoding_time = new_df['Encoding Time'].values[0]
    average_times.append(encoding_time)

plt.figure(figsize=(10, 15))

plt.xlabel('Compression Ratio',fontsize=size)
plt.ylabel('Compression Time (ns/point)',fontsize=size)


colors= ["#000000", "#000000", "#000000", "#000000",  
          "#0000ff" , "#0000ff" ,  "#0000ff","#0000ff","#0000ff","#0000ff","#0000ff","#0000ff",
         "#007f00" , "#007f00" ,  "#007f00","#007f00","#007f00","#007f00","#007f00","#007f00",
          "#ff0000" , "#ff0000" ,  "#ff0000","#ff0000","#ff0000","#ff0000","#ff0000","#ff0000"]
markers = ['x', '+', '_',  '|',
           '*', '<', '>', '^', 'v','D', 'o','s', 
           '*','<',  '>','^','v' ,'D', 'o', 's',
           '*' ,'<', '>' , '^','v' , 'D','o','s']  
# colors = ['b', 'g', 'r', 'c']
for i in range(len(encoding_list)):
    marker_index = i % len(markers)
    color_index = i % len(colors)
    plt.scatter(compression_ratios[i], average_times[i], label=encoding_list[i], marker=markers[marker_index],sizes = [size*10]*23,color=colors[color_index])


plt.tick_params(axis='both', which='major', labelsize=size)
plt.legend(encoding_list, bbox_to_anchor=(0.4, 1.43), loc = 'upper center',fontsize=19,labelspacing=0.05,handletextpad=0.05,columnspacing =0.05,ncol=3)

x1, y1 = compression_ratios[11], average_times[11]
x2, y2 = compression_ratios[18], average_times[18]

slope = (y2 - y1) / (x2 - x1)

intercept = y1 - slope * x1


x = np.linspace(0, max(compression_ratios)+0.18, 400)


y = slope * x + intercept
plt.plot(x, y, color="grey",linestyle='-.', label='Fitted line through specific points')  # 绘制穿过特定两点的线
plt.xlim(2, max(compression_ratios)+0.18)
plt.ylim(0, max(average_times)+60)

plt.subplots_adjust(top=0.60)
plt.savefig("./figs/cr_vs_ct.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/cr_vs_ct.png", dpi = 400,bbox_inches='tight')
# plt.show()