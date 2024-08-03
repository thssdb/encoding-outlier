import os
import pandas as pd

# path_datasets = './iotdb_datasets_lists/' 

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]
path_bos_ratio =  './compression_ratio/block_size_bos_v/'  
path_bws_ratio =  './compression_ratio/block_size_bos_b/'  
path_prune_ratio =  './compression_ratio/block_size_bos_m/'
# path_ratio_amortization =  './compression_ratio/block_size_amortization/'  
# path_ratio_ts2diff =  './compression_ratio/block_size_ts2diff/'

df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Compression Ratio'])
index_re = 0


for j in range(len(dir_r)):

    dir_ratio_rd = path_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rd_df = df_avg_rd.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    df_avg_bws = df_bws.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bws_df = df_avg_bws.shape[0]

    dir_ratio_prune = path_prune_ratio + dir_r[j] + "_ratio.csv"
    df_prune = pd.read_csv(dir_ratio_prune)
    df_avg_prune = df_prune.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_prune_df = df_avg_prune.shape[0]


    for i in range(len_rd_df):
        cr = 1/df_avg_rd.iloc[i,-1]
        df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        index_re += 1
    
    for i in range(len_bws_df):
        cr = 1/df_avg_bws.iloc[i,-1]
        df_result.loc[index_re] = [df_avg_bws.iloc[i,0],dir_r[j],df_avg_bws.iloc[i,1],cr]
        index_re += 1

    for i in range(len_prune_df):
        cr = 1/df_avg_prune.iloc[i,-1]
        df_result.loc[index_re] = [df_avg_prune.iloc[i,0],dir_r[j],df_avg_prune.iloc[i,1],cr]
        index_re += 1


        
# print(df_result)
df_result.to_csv('./compression_ratio/block_size_compression_ratio.csv',index=False)

df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Time'])
index_re = 0

for j in range(len(dir_r)):

    dir_ratio_rd = path_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    # print(df_rd.columns)
    for k in range(df_rd.shape[0]):
        df_rd.loc[k,"Encode"] = df_rd.iloc[k,2] / df_rd.iloc[k,4] 
    df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rd_df = df_avg_rd.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    for k in range(df_bws.shape[0]):
        df_bws.loc[k,"Encode"] = df_bws.iloc[k,2] / df_bws.iloc[k,4] 
    df_avg_bws = df_bws.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bws_df = df_avg_bws.shape[0]


    dir_ratio_prune = path_prune_ratio + dir_r[j] + "_ratio.csv"
    df_prune = pd.read_csv(dir_ratio_prune)
    for k in range(df_prune.shape[0]):
        df_prune.loc[k,"Encode"] = df_prune.iloc[k,2] / df_prune.iloc[k,4] 
    df_avg_prune = df_prune.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_prune_df = df_avg_prune.shape[0]
  

    for i in range(len_rd_df):
        cr = df_avg_rd.iloc[i,-1]*pow(2,df_avg_rd.iloc[i,1])
        df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        index_re += 1
    
    for i in range(len_bws_df):
        cr = df_avg_bws.iloc[i,-1]*pow(2,df_avg_bws.iloc[i,1])
        df_result.loc[index_re] = [df_avg_bws.iloc[i,0],dir_r[j],df_avg_bws.iloc[i,1],cr]
        index_re += 1

    for i in range(len_prune_df):
        cr = df_avg_prune.iloc[i,-1]*pow(2,df_avg_prune.iloc[i,1])
        df_result.loc[index_re] = [df_avg_prune.iloc[i,0],dir_r[j],df_avg_prune.iloc[i,1],cr]
        index_re += 1


        
# print(df_result)
df_result.to_csv('./compression_ratio/block_size_time.csv',index=False)

df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Time'])
index_re = 0

for j in range(len(dir_r)):

    dir_ratio_rd = path_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    # print(df_rd.columns)
    for k in range(df_rd.shape[0]):
        df_rd.loc[k,"Encode"] = df_rd.iloc[k,3] / df_rd.iloc[k,4] 
    df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rd_df = df_avg_rd.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    for k in range(df_bws.shape[0]):
        df_bws.loc[k,"Encode"] = df_bws.iloc[k,3] / df_bws.iloc[k,4] 
    df_avg_bws = df_bws.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bws_df = df_avg_bws.shape[0]


    dir_ratio_prune = path_prune_ratio + dir_r[j] + "_ratio.csv"
    df_prune = pd.read_csv(dir_ratio_prune)
    for k in range(df_prune.shape[0]):
        df_prune.loc[k,"Encode"] = df_prune.iloc[k,3] / df_prune.iloc[k,4] 
    df_avg_prune = df_prune.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_prune_df = df_avg_prune.shape[0]
  

    for i in range(len_rd_df):
        cr = df_avg_rd.iloc[i,-1]*pow(2,df_avg_rd.iloc[i,1])
        df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        index_re += 1
    
    for i in range(len_bws_df):
        cr = df_avg_bws.iloc[i,-1]*pow(2,df_avg_bws.iloc[i,1])
        df_result.loc[index_re] = [df_avg_bws.iloc[i,0],dir_r[j],df_avg_bws.iloc[i,1],cr]
        index_re += 1

    for i in range(len_prune_df):
        cr = df_avg_prune.iloc[i,-1]*pow(2,df_avg_prune.iloc[i,1])
        df_result.loc[index_re] = [df_avg_prune.iloc[i,0],dir_r[j],df_avg_prune.iloc[i,1],cr]
        index_re += 1



        
# print(df_result)
df_result.to_csv('./compression_ratio/block_size_decode_time.csv',index=False)