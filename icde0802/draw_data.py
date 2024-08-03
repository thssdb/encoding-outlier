import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path):
    return pd.read_csv(file_path)

fontsize = 8

def rle_process_data(data):
    # Subtract the minimum value from each block of 1024 values
    n = 1024
    for start in range(0, len(data), n):
        end = min(start + n, len(data))
        data[start:end] = data[start:end] - data[start:end].min()
    # Remove adjacent duplicate values
    return data[data.shift() != data]



def plot_distribution_rle(data,file,ax,title_i):
    # print(file)
    # print(data.iloc[:1024, 1])
    processed_data = rle_process_data(data.iloc[:, 1])
    # print(processed_data)
    ax.hist(processed_data, bins=30, alpha=0.75, color='blue', edgecolor='black')
    
    ax.set_title("("+title_i+') {}'.format(file),fontsize=fontsize)
    ax.set_xlabel('value',fontsize=fontsize)
    ax.set_ylabel('Frequency',fontsize=fontsize)
    ax.tick_params(axis='both', which='major', labelsize=fontsize)

def tsdiff_process_data(data):
    # Perform differential calculation every 1024 values
    n = 1024
    processed_data = []
    for start in range(0, len(data), n):
        end = min(start + n, len(data))
        diffs = data[start:end].diff().dropna()  # Calculate differentials and drop NaN from diff
        if not diffs.empty:
            # Subtract the minimum differential value from all differentials in this block
            diffs -= diffs.min()
            processed_data.extend(diffs)
    return pd.Series(processed_data)

def plot_distribution_tsdiff(data,file,ax,title_i):
    # print(file)
    # print(data.iloc[:1024, 1])
    processed_data = tsdiff_process_data(data.iloc[:, 1])
    # print(processed_data)
    ax.hist(processed_data, bins=30, alpha=0.75, color='blue', edgecolor='black')
    
    if title_i == "h":
        # 获取x轴的数据范围
        xmin, xmax = ax.get_xlim()

# 设置x轴的刻度位置，这里我们设置为最小值，最大值和中间值
        ax.set_xticks([0, 300000, 600000])
    ax.set_title("("+title_i+') {}'.format(file),fontsize=fontsize)
    ax.set_xlabel('value',fontsize=fontsize)
    ax.set_ylabel('Frequency',fontsize=fontsize)
    ax.tick_params(axis='both', which='major', labelsize=fontsize)

def zigzag(data):
    # Apply the zigzag transformation to each element in the data
    return data.apply(lambda x: 2*(-x) - 1 if x < 0 else 2 * x)

def process_data_sprintz(data):
    # Calculate differentials every 1024 values and apply zigzag transformation
    n = 1024
    processed_data = pd.Series(dtype=float)
    for start in range(0, len(data), n):
        end = min(start + n, len(data))
        diffs = data[start:end].diff().dropna()  # Calculate differentials and drop NaN from diff
        if not diffs.empty:
            zigzag_diffs = zigzag(diffs)
            processed_data = pd.concat([processed_data, zigzag_diffs], ignore_index=True)
    return processed_data

def plot_distribution_sprintz(data,file,ax,title_i):
    # print(file)
    # print(data.iloc[:1024, 1])
    processed_data = process_data_sprintz(data.iloc[:, 1])
    # print(processed_data)
    ax.hist(processed_data, bins=30, alpha=0.75, color='blue', edgecolor='black')
    
    ax.set_title("("+title_i+') {}'.format(file),fontsize=fontsize)
    ax.set_xlabel('value',fontsize=fontsize)
    ax.set_ylabel('Frequency',fontsize=fontsize)
    ax.tick_params(axis='both', which='major', labelsize=fontsize)


file_parent_path = '../trans_data/'
dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel",'Nifty-Stocks']
file_r = ["EPM-Education/epm_0.csv","Metro-Traffic/syndata_metro.csv","Vehicle-Charge/electric_vehicle_charging.csv","CS-Sensors/test.csv","TH-Climate/syndata_climate0.csv","TY-Transport/syndata_transport0.csv","YZ-Electricity/0a.csv","GW-Magnetic/syndata_magnetic0.csv","USGS-Earthquakes/syndata_earthquakes0.csv","Cyber-Vehicle/syndata_vehicle0.csv","TY-Fuel/syndata_fuel0.csv",'Nifty-Stocks/syndata_stocks1.csv']
title_list = ['a','b','c','d','e','f','g','h','i','j','k','l']

fig, axs = plt.subplots(3, 4, figsize=(10, 6))
for i,file in enumerate(file_r):
    file_path = file_parent_path + file
    data = read_csv(file_path)
    row = i // 4
    col = i % 4
    title_i = title_list[i]
    plot_distribution_rle(data,dir_r[i],axs[row, col],title_i)
plt.subplots_adjust(wspace=0.53)  # Increase or decrease this value to adjust spacing
plt.subplots_adjust(hspace=0.6) 

# plt.tight_layout()
plt.savefig("./figs/data_dis_rle.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/data_dis_rle.png", dpi = 400,bbox_inches='tight')

fig, axs = plt.subplots(3, 4, figsize=(10, 6))
for i,file in enumerate(file_r):
    file_path = file_parent_path + file
    data = read_csv(file_path)
    row = i // 4
    col = i % 4
    title_i = title_list[i]
    plot_distribution_tsdiff(data,dir_r[i],axs[row, col],title_i)
plt.subplots_adjust(wspace=0.53)  # Increase or decrease this value to adjust spacing
plt.subplots_adjust(hspace=0.6) 

# plt.tight_layout()
plt.savefig("./figs/data_dis_diff.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/data_dis_diff.png", dpi = 400,bbox_inches='tight')

fig, axs = plt.subplots(3, 4, figsize=(10, 6))
for i,file in enumerate(file_r):
    file_path = file_parent_path + file
    data = read_csv(file_path)
    row = i // 4
    col = i % 4
    title_i = title_list[i]
    plot_distribution_sprintz(data,dir_r[i],axs[row, col],title_i)
plt.subplots_adjust(wspace=0.53)  # Increase or decrease this value to adjust spacing
plt.subplots_adjust(hspace=0.6) 

# plt.tight_layout()
plt.savefig("./figs/data_dis_sprintz.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/data_dis_sprintz.png", dpi = 400,bbox_inches='tight')