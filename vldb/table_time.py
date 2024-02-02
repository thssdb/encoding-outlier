import os
import pandas as pd
import numpy as np

dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel"]
encoding_list = ["GORILLA","CHIMP","Elf","BUFF","RLE","RLE+PFOR","RLE+NEWPFOR","RLE+OPTPFOR","RLE+FASTPFOR","RLE+BOS-O","RLE+BWS","RLE+BOS-P","SPRINTZ","SPRINTZ+PFOR","SPRINTZ+NEWPFOR","SPRINTZ+OPTPFOR","SPRINTZ+FASTPFOR","SPRINTZ+BOS-O","SPRINTZ+BWS","SPRINTZ+BOS-P","TS_2DIFF","TS_2DIFF+PFOR","TS_2DIFF+NEWPFOR","TS_2DIFF+OPTPFOR","TS_2DIFF+FASTPFOR","TS_2DIFF+BOS-O","TS_2DIFF+BWS","TS_2DIFF+BOS-P"]
datasets = ["EE","MT","VC","CS","TC","TT","YE","GM","UE","CV","TF"]

df = pd.read_csv("./compression_ratio/encode_time.csv")
df = df[df['Dataset'] != 'Nifty-Stocks']
df2 = pd.read_csv("./compression_ratio/decode_time.csv")
df2 = df2[df2['Dataset'] != 'Nifty-Stocks']
# text = text + "\\hline\n"
# text = text + "\\multirow{" + str(len(encoding_list)) + "}*{\\rotatebox[origin=c]{90}{Decoding Time/(ns/points)}}"
width = 0 #保留几位有效数字
# 对每个数据集找最佳的
df2 = df2[df2["Encoding"].isin(encoding_list)]
max_array = {}
for dataset in dir_r:
    min = df2[df2['Dataset'] == dataset]['Decoding Time'].min()
    condition = (df2['Dataset'] == dataset) & (df2['Decoding Time'] == min)
    df2.loc[condition, 'Decoding Time'] = -100
    max_array[dataset] = min
changeLine2 = "\\\\ \\cline{1-24}\n"
changeLine = "\\\\ \\cline{2-24}\n"


text = "\\hline\n"
text = text + "\\multicolumn{2}{|c||}{\\multirow{3}*{Methods}} & \multicolumn{11}{|c||}{Compression time} & \multicolumn{11}{|c|}{Decompression time}"
text = text + "\\\\ \\cline{3-24}\n"
text += "\\multicolumn{2}{|c||}{~} & \\multicolumn{6}{|c||}{Datasets without float} & \\multicolumn{5}{|c||}{Datasets with float} & \\multicolumn{6}{|c||}{Datasets without float} & \\multicolumn{5}{|c|}{Datasets with float} \\\\ \\cline{3-24}\n\\multicolumn{2}{|c||}{~}"
count = 0
# for dataset in datasets:
#     count = count + 1
#     if count == 7:
#         break
#     text = text + " & " + dataset
# count = 0
# for dataset in datasets:
#     count = count + 1
#     if count == 7:
#         break
#     text = text + " & " + dataset
# count = 0
# for dataset in datasets:
#     count = count + 1
#     if count >= 7:
#         text = text + " & " + dataset
# count = 0
# for dataset in datasets:
#     count = count + 1
#     if count >= 7:
#         text = text + " & " + dataset
for dataset in datasets:
    text = text + " & " + dataset
for dataset in datasets:
    text = text + " & " + dataset
text = text + "\\\\ \\hline\n"
text = text + "\\hline\n"


width = 0 #保留几位小数
df = df[df["Encoding"].isin(encoding_list)]
print(df)
# 对每个数据集找最佳的
for dataset in dir_r:
    min = df[df['Dataset'] == dataset]['Encoding Time'].min()
    condition = (df['Dataset'] == dataset) & (df['Encoding Time'] == min)
    df.loc[condition, 'Encoding Time'] = -min
for encoding in encoding_list:
    # if encoding != "GORILLA":
    #     text = text + "~"
    # text = text +  " & "
    if encoding == "GORILLA":
        text =  text + "\\multirow{" + str(4) + "}*{\\rotatebox[origin=c]{90}{Float}}"
    elif encoding == "RLE":
        text =  text + "\\multirow{" + str(8) + "}*{\\rotatebox[origin=c]{90}{RLE+}}"
    elif encoding == "SPRINTZ":
        text =  text + "\\multirow{" + str(8) + "}*{\\rotatebox[origin=c]{90}{SPRINTZ+}}"
    elif encoding == "TS_2DIFF":
        text =  text + "\\multirow{" + str(8) + "}*{\\rotatebox[origin=c]{90}{TS\\_2DIFF+}}"
    else:
        text = text + "~"
    text = text +  " & "
    if  encoding == "TS_2DIFF":
        text = text + "BP"
    elif encoding == "TS_2DIFF+BOS-O":
        text = text + "\\textbf{BOS-V}"
    elif encoding == "TS_2DIFF+BWS":
        text = text + "\\textbf{BOS-L}"
    elif encoding == "TS_2DIFF+PFOR":
        text = text + "PFOR"
    elif encoding == "TS_2DIFF+NEWPFOR":
        text = text + "NEWPFOR"
    elif encoding == "TS_2DIFF+OPTPFOR":
        text = text + "OPTPFOR"
    elif encoding == "TS_2DIFF+FASTPFOR":
        text = text + "FASTPFOR"
    elif encoding == "TS_2DIFF+BOS-P":
        text = text + "\\textbf{BOS-H}"
    elif encoding == "RLE":
        text = text + "BP"
    elif encoding == "RLE+BOS-O":
        text = text + "\\textbf{BOS-V}"
    elif encoding == "RLE+BWS":
        text = text + "\\textbf{BOS-L}"
    elif encoding == "RLE+PFOR":
        text = text + "PFOR"
    elif encoding == "RLE+NEWPFOR":
        text = text + "NEWPFOR"
    elif encoding == "RLE+OPTPFOR":
        text = text + "OPTPFOR"
    elif encoding == "RLE+FASTPFOR":
        text = text + "FASTPFOR"
    elif encoding == "RLE+BOS-P":
        text = text + "\\textbf{BOS-H}"
    elif encoding == "SPRINTZ":
        text = text + "BP"
    elif encoding == "SPRINTZ+BOS-O":
        text = text + "\\textbf{BOS-V}"
    elif encoding == "SPRINTZ+BWS":
        text = text + "\\textbf{BOS-L}"
    elif encoding == "SPRINTZ+PFOR":
        text = text + "PFOR"
    elif encoding == "SPRINTZ+NEWPFOR":
        text = text + "NEWPFOR"
    elif encoding == "SPRINTZ+OPTPFOR":
        text = text + "OPTPFOR"
    elif encoding == "SPRINTZ+FASTPFOR":
        text = text + "FASTPFOR"
    elif encoding == "SPRINTZ+BOS-P":
        text = text + "\\textbf{BOS-H}"
    else:
        text = text + encoding
    # count = 0
    for dataset in dir_r:
        # count = count + 1
        # if count == 7 :
        #     break
        new_df = df[df['Encoding'] == encoding]
        new_df = new_df[new_df['Dataset'] == dataset]
        ratio = new_df['Encoding Time'].values[0]
        if ratio > 0:
            text = text + " & " + str(round(ratio) + 1)
        else:
            text = text + " & " + "\\textbf{\\textcolor{red}{" + str(round(-ratio) + 1) + "}}"
    # count = 0
    for dataset in dir_r:
        # count = count + 1
        # if count == 7 :
        #     break
        new_df2 = df2[df2['Encoding'] == encoding]
        new_df2 = new_df2[new_df2['Dataset'] == dataset]
        ratio2 = new_df2['Decoding Time'].values[0]
        if ratio2 > 0:
            text = text + " & " + str(round(ratio2)+1)
        else:
            text = text + " & " + "\\textbf{\\textcolor{red}{" + str(round(max_array[dataset])+1) + "}}"
    # count = 0
    # for dataset in dir_r:
    #     count = count + 1
    #     if count >= 7 :
    #         new_df = df[df['Encoding'] == encoding]
    #         new_df = new_df[new_df['Dataset'] == dataset]
    #         ratio = new_df['Encoding Time'].values[0]
    #         if ratio > 0:
    #             text = text + " & " + str(round(ratio))
    #         else:
    #             text = text + " & " + "\\textbf{\\textcolor{red}{" + str(round(-ratio)) + "}}"
    # count = 0
    # for dataset in dir_r:
    #     count = count + 1
    #     if count >= 7 :
    #         new_df2 = df2[df2['Encoding'] == encoding]
    #         new_df2 = new_df2[new_df2['Dataset'] == dataset]
    #         ratio2 = new_df2['Decoding Time'].values[0]
    #         if ratio2 > 0:
    #             text = text + " & " + str(round(ratio2))
    #         else:
    #             text = text + " & " + "\\textbf{\\textcolor{red}{" + str(round(max_array[dataset])) + "}}"
    if encoding == encoding_list[-1]:
        text = text + "\\\\ \\hline\n"
    elif  encoding == "BUFF"  or encoding == "RLE+BOS-P" or encoding == "SPRINTZ+BOS-P":
        text = text + changeLine2
        text = text + "\\cline{1-24}\n"
    else:
        text = text + changeLine
print(text)