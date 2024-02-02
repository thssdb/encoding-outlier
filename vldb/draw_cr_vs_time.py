import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

path_ratio = './compression_ratio.csv'  
dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","Nifty-Stocks","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel"]
# encoding_list = ["GORILLA","CHIMP","Elf","BUFF","FASTPFOR","NEWPFOR","OPTPFOR","RLE","RLE+BOS-O","RLE+BOS-A","RLE+PFOR","SPRINTZ","SPRINTZ+BOS","SPRINTZ+Amortization","SPRINTZ+PFOR","TS_2DIFF","TS_2DIFF+BOS-O","TS_2DIFF+BOS-A","TS_2DIFF+PFOR"]
encoding_list = ["GORILLA","CHIMP","Elf","BUFF",
                 "RLE","RLE+PFOR","RLE+NEWPFOR","RLE+OPTPFOR","RLE+FASTPFOR","RLE+BOS-V","RLE+BOS-L","RLE+BOS-H",#"RLE+BWS",
                 "SPRINTZ","SPRINTZ+PFOR","SPRINTZ+NEWPFOR","SPRINTZ+OPTPFOR","SPRINTZ+FASTPFOR","SPRINTZ+BOS-V","SPRINTZ+BOS-L","SPRINTZ+BOS-H",#"SPRINTZ+BWS",
                 "TS_2DIFF","TS_2DIFF+PFOR","TS_2DIFF+NEWPFOR","TS_2DIFF+OPTPFOR","TS_2DIFF+FASTPFOR","TS_2DIFF+BOS-V","TS_2DIFF+BOS-L","TS_2DIFF+BOS-H"]#,"TS_2DIFF+BWS"]
datasets = ["EE","MT","VC","CS","TC","TT","YE","GM","UE","CV","TF"]
size = 30

df = pd.read_csv("./compression_ratio/compression_ratio.csv")
df.replace("RLE+BOS-O", "RLE+BOS-V", inplace=True)
df.replace("RLE+BWS", "RLE+BOS-L", inplace=True)
df.replace("RLE+BOS-P", "RLE+BOS-H", inplace=True)
df.replace("SPRINTZ+BOS-O", "SPRINTZ+BOS-V", inplace=True)
df.replace("SPRINTZ+BWS", "SPRINTZ+BOS-L", inplace=True)
df.replace("SPRINTZ+BOS-P", "SPRINTZ+BOS-H", inplace=True)
df.replace("TS_2DIFF+BOS-O", "TS_2DIFF+BOS-V", inplace=True)
df.replace("TS_2DIFF+BWS", "TS_2DIFF+BOS-L", inplace=True)
df.replace("TS_2DIFF+BOS-P", "TS_2DIFF+BOS-H", inplace=True)
df = df[df['Dataset'] != 'Nifty-Stocks']

result_df = df.groupby('Encoding')['Compression Ratio'].mean().reset_index()
# print(result_df)
compression_ratios = []
for encoding in encoding_list:
    new_df = result_df[result_df['Encoding'] == encoding]
    ratio = new_df['Compression Ratio'].values[0]
    compression_ratios.append(ratio)

df = pd.read_csv("./compression_ratio/encode_time.csv")
df.replace("RLE+BOS-O", "RLE+BOS-V", inplace=True)
df.replace("RLE+BWS", "RLE+BOS-L", inplace=True)
df.replace("RLE+BOS-P", "RLE+BOS-H", inplace=True)
df.replace("SPRINTZ+BOS-O", "SPRINTZ+BOS-V", inplace=True)
df.replace("SPRINTZ+BWS", "SPRINTZ+BOS-L", inplace=True)
df.replace("SPRINTZ+BOS-P", "SPRINTZ+BOS-H", inplace=True)
df.replace("TS_2DIFF+BOS-O", "TS_2DIFF+BOS-V", inplace=True)
df.replace("TS_2DIFF+BWS", "TS_2DIFF+BOS-L", inplace=True)
df.replace("TS_2DIFF+BOS-P", "TS_2DIFF+BOS-H", inplace=True)
df = df[df['Dataset'] != 'Nifty-Stocks']

result_df = df.groupby('Encoding')['Encoding Time'].mean().reset_index()
average_times = []
for encoding in encoding_list:
    new_df = result_df[result_df['Encoding'] == encoding]
    encoding_time = new_df['Encoding Time'].values[0]
    average_times.append(encoding_time)

plt.figure(figsize=(10, 15))

plt.xlabel('Compression Ratio',fontsize=size)
plt.ylabel('Compression Time (ns/points)',fontsize=size)

colors= ["#1178b4", "#33a02c", "#ff7f00", "#6a3d9a",  
          "#0e2c82" , "#b6b51f" ,  "#fb9a99","#814a19","#333333","#ff0000","#ff0000","#ff0000",
         "#0e2c82" , "#b6b51f" ,  "#fb9a99","#814a19","#333333","#ff0000","#ff0000","#ff0000",
          "#0e2c82" , "#b6b51f" ,  "#fb9a99","#814a19","#333333","#ff0000","#ff0000","#ff0000"]
markers = ['o', 's', '^',  'x',
           '+', '<', '>', '.', '2','H', 'h','*', 
           '3','1',  '|','+','1' ,'P', 'D', 'v',
           '2' ,'3', '4' , '_','d' , 'X','p','8']  
# colors = ['b', 'g', 'r', 'c']
for i in range(len(encoding_list)):
    marker_index = i % len(markers)
    color_index = i % len(colors)
    plt.scatter(compression_ratios[i], average_times[i], label=encoding_list[i], marker=markers[marker_index],sizes = [size*10]*23,color=colors[color_index])

plt.tick_params(axis='both', which='major', labelsize=size*1.1)
plt.legend(encoding_list, bbox_to_anchor=(0.4, 2.1), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=2)
plt.subplots_adjust(top=0.60)
plt.savefig("./figs/cr_vs_ct.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/cr_vs_ct.png", dpi = 400,bbox_inches='tight')
# plt.show()