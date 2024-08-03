import os
import pandas as pd
path_ratio = './compression_ratio.csv'  
dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel","Nifty-Stocks"]
# encoding_list = ["GORILLA","CHIMP","Elf","BUFF","FASTPFOR","NEWPFOR","OPTPFOR","RLE","RLE+BOS-O","RLE+BOS-A","RLE+PFOR","SPRINTZ","SPRINTZ+BOS","SPRINTZ+Amortization","SPRINTZ+PFOR","TS_2DIFF","TS_2DIFF+BOS-O","TS_2DIFF+BOS-A","TS_2DIFF+PFOR"]
encoding_list = ["GORILLA","CHIMP","Elf","BUFF",
                 "RLE","RLE+PFOR","RLE+NEWPFOR","RLE+OPTPFOR","RLE+FASTPFOR","RLE+BOS-V","RLE+BOS-M", #"RLE+BOS-B",
                 "SPRINTZ","SPRINTZ+PFOR","SPRINTZ+NEWPFOR","SPRINTZ+OPTPFOR","SPRINTZ+FASTPFOR","SPRINTZ+BOS-V","SPRINTZ+BOS-M", # "SPRINTZ+BOS-B",
                 "TS_2DIFF","TS_2DIFF+PFOR","TS_2DIFF+NEWPFOR","TS_2DIFF+OPTPFOR","TS_2DIFF+FASTPFOR","TS_2DIFF+BOS-V","TS_2DIFF+BOS-M"] #"TS_2DIFF+BOS-B",
datasets = ["EE","MT","VC","CS","TC","TT","YE","GM","UE","CV","TF","NS"]

df = pd.read_csv("./compression_ratio/compression_ratio.csv")
# df = df[df['Dataset'] != 'Nifty-Stocks']
print(df.shape)
changeLine = "\\\\ \\cline{2-14}\n"
text = "\\hline\n\\multicolumn{2}{|c||}{\\multirow{2}*{Methods}} & \\multicolumn{6}{|c||}{Datasets without float} & \\multicolumn{6}{|c|}{Datasets with float} \\\\ \\cline{3-14}\n\\multicolumn{2}{|c||}{~}"
for dataset in datasets:
    text = text + " & " + dataset
text = text + "\\\\ \\hline\n"
text = text + "\\hline\n"
width = 2 
max_array = {}
smax_array = {}
for dataset in dir_r:
    max = df[df['Dataset'] == dataset]['Compression Ratio'].max()
    condition = (df['Dataset'] == dataset) & (df['Compression Ratio'] == max)
    df.loc[condition, 'Compression Ratio'] = -0.01
    max_array[dataset] = max
    # smax = df[(df['Dataset'] == dataset) & (df['Encoding'] != "RLE+BOS") & (df['Encoding'] != "TS_2DIFF+BOS") & (df['Encoding'] != "SPRINTZ+BOS")]['Compression Ratio'].max()
    # condition = (df['Dataset'] == dataset) & (df['Compression Ratio'] == smax)
    # df.loc[condition, 'Compression Ratio'] = -0.02
    # smax_array[dataset] = smax

for encoding in encoding_list:
    if encoding == "GORILLA":
        text =  text + "\\multirow{" + str(4) + "}*{\\rotatebox[origin=c]{90}{Float}}"
    elif encoding == "RLE":
        text =  text + "\\multirow{" + str(7) + "}*{\\rotatebox[origin=c]{90}{RLE+}}"
    elif encoding == "SPRINTZ":
        text =  text + "\\multirow{" + str(7) + "}*{\\rotatebox[origin=c]{90}{SPRINTZ+}}"
    elif encoding == "TS_2DIFF":
        text =  text + "\\multirow{" + str(7) + "}*{\\rotatebox[origin=c]{90}{TS2DIFF+}}"
    else:
        text = text + "~"
    text = text +  " & "
    if  encoding == "TS_2DIFF":
        text = text + "BP"
    elif encoding == "TS_2DIFF+BOS-V":
        text = text + "\\textbf{BOS-V / B}"
    elif encoding == "TS_2DIFF+BOS-M":
        text = text + "\\textbf{BOS-M}"
    elif encoding == "TS_2DIFF+PFOR":
        text = text + "PFOR"
    elif encoding == "TS_2DIFF+NEWPFOR":
        text = text + "NEWPFOR"
    elif encoding == "TS_2DIFF+OPTPFOR":
        text = text + "OPTPFOR"
    elif encoding == "TS_2DIFF+FASTPFOR":
        text = text + "FASTPFOR"
    # elif encoding == "TS_2DIFF+BOS-B":
    #     text = text + "\\textbf{BOS-V / B}"
    elif encoding == "RLE":
        text = text + "BP"
    elif encoding == "RLE+BOS-V":
        text = text + "\\textbf{BOS-V / B}"
    elif encoding == "RLE+BOS-M":
        text = text + "\\textbf{BOS-M}"
    elif encoding == "RLE+PFOR":
        text = text + "PFOR"
    elif encoding == "RLE+NEWPFOR":
        text = text + "NEWPFOR"
    elif encoding == "RLE+OPTPFOR":
        text = text + "OPTPFOR"
    elif encoding == "RLE+FASTPFOR":
        text = text + "FASTPFOR"
    # elif encoding == "RLE+BOS-B":
    #     text = text + "\\textbf{BOS-V / B}"
    elif encoding == "SPRINTZ":
        text = text + "BP"
    elif encoding == "SPRINTZ+BOS-V":
        text = text + "\\textbf{BOS-V / B}"
    elif encoding == "SPRINTZ+BOS-M":
        text = text + "\\textbf{BOS-M}"
    elif encoding == "SPRINTZ+PFOR":
        text = text + "PFOR"
    elif encoding == "SPRINTZ+NEWPFOR":
        text = text + "NEWPFOR"
    elif encoding == "SPRINTZ+OPTPFOR":
        text = text + "OPTPFOR"
    elif encoding == "SPRINTZ+FASTPFOR":
        text = text + "FASTPFOR"
    # elif encoding == "SPRINTZ+BOS-B":
    #     text = text + "\\textbf{BOS-V / B}"
    else:
        text = text + encoding
    for dataset in dir_r:
        new_df = df[df['Encoding'] == encoding]
        new_df = new_df[new_df['Dataset'] == dataset]
        ratio = new_df['Compression Ratio'].values[0]
        if ratio > 0:
            text = text + " & " + format(round(ratio,width),'.' + str(width) +'f')
        elif ratio == -0.01:
            text = text + " & " + "\\textbf{\\textcolor{red}{" + format(round(max_array[dataset],width),'.' + str(width) +'f') + "}}"
    if encoding == encoding_list[-1] or encoding == "BUFF"  or encoding == "RLE+BOS-M" or encoding == "SPRINTZ+BOS-M":
        text = text + "\\\\ \\hline\n"
        if encoding != encoding_list[-1]:
            text = text + " \\hline\n"
    else:
        text = text + changeLine
print(text)