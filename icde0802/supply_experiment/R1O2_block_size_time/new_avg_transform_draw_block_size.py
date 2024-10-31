import os
import pandas as pd

# path_datasets = './iotdb_datasets_lists/' 
#
dir_r = ["EPM-Education","Metro-Traffic", "Nifty-Stocks","GW-Magnetic","Cyber-Vehicle","USGS-Earthquakes", "Vehicle-Charge","CS-Sensors",  "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]
parent_dir = "/Users/zihanguo/Downloads/R/outlier/outliier_code"
# parent_dir = "/Users/xiaojinzhao/Documents/GitHub"
path_bos_ratio = parent_dir + '/encoding-outlier/icde0802/compression_ratio/block_size_bos_v/'  
path_bws_ratio = parent_dir + '/encoding-outlier/icde0802/compression_ratio/block_size_bos_m/'  
path_prune_ratio = parent_dir + '/encoding-outlier/icde0802/compression_ratio/block_size_bos_b/'
path_improve_ratio = parent_dir + '/encoding-outlier/icde0802/compression_ratio/block_size_bos_improve/'


df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Time'])
index_re = 0

for j in range(len(dir_r)):

    dir_ratio_rd = path_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x)
    # print(df_avg_rd.columns)
    for k in range(df_avg_rd.shape[0]):
        df_avg_rd.loc[k,"Encode"] = df_avg_rd.iloc[k,3] / df_avg_rd.iloc[k,5] 
    len_rd_df = df_avg_rd.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    df_avg_bws = df_bws.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x)
    for k in range(df_avg_bws.shape[0]):
        df_avg_bws.loc[k,"Encode"] = df_avg_bws.iloc[k,3] / df_avg_bws.iloc[k,5] 
    len_bws_df = df_avg_bws.shape[0]


    # dir_ratio_prune = path_prune_ratio + dir_r[j] + "_ratio.csv"
    # df_prune = pd.read_csv(dir_ratio_prune)
    # for k in range(df_prune.shape[0]):
    #     df_prune.loc[k,"Encode"] = df_prune.iloc[k,2] / df_prune.iloc[k,4] 
    # df_avg_prune = df_prune.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_prune_df = df_avg_prune.shape[0]

    dir_ratio_improve = path_improve_ratio + dir_r[j] + "_ratio.csv"
    df_improve = pd.read_csv(dir_ratio_improve)
    df_avg_improve = df_improve.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x)
    for k in range(df_avg_improve.shape[0]):
        df_avg_improve.loc[k,"Encode"] = df_avg_improve.iloc[k,3] / df_avg_improve.iloc[k,5] 
    len_improve_df = df_avg_improve.shape[0]

    for i in range(len_rd_df):
        cr = df_avg_rd.iloc[i,-1]*pow(2,df_avg_rd.iloc[i,1])
        df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        index_re += 1
    
    for i in range(len_bws_df):
        cr = df_avg_bws.iloc[i,-1]*pow(2,df_avg_bws.iloc[i,1])
        df_result.loc[index_re] = [df_avg_bws.iloc[i,0],dir_r[j],df_avg_bws.iloc[i,1],cr]
        index_re += 1

    # for i in range(len_prune_df):
    #     cr = df_avg_prune.iloc[i,-1]*pow(2,df_avg_prune.iloc[i,1])
    #     df_result.loc[index_re] = [df_avg_prune.iloc[i,0],dir_r[j],df_avg_prune.iloc[i,1],cr]
    #     index_re += 1

    for i in range(len_improve_df):
        cr = df_avg_improve.iloc[i,-1]*pow(2,df_avg_improve.iloc[i,1])
        df_result.loc[index_re] = ["TS_2DIFF+BOS-B",dir_r[j],df_avg_improve.iloc[i,1],cr]
        index_re += 1

        
# print(df_result)
df_result.to_csv('./block_size_time.csv',index=False)

df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Time'])
index_re = 0

for j in range(len(dir_r)):

    dir_ratio_rd = path_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    # print(df_rd.columns)
    df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x)
    for k in range(df_avg_rd.shape[0]):
        df_avg_rd.loc[k,"Encode"] = df_avg_rd.iloc[k,4] / df_avg_rd.iloc[k,5] 
    len_rd_df = df_avg_rd.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    df_avg_bws = df_bws.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x)
    for k in range(df_avg_bws.shape[0]):
        df_avg_bws.loc[k,"Encode"] = df_avg_bws.iloc[k,4] / df_avg_bws.iloc[k,5] 
    len_bws_df = df_avg_bws.shape[0]


    # dir_ratio_prune = path_prune_ratio + dir_r[j] + "_ratio.csv"
    # df_prune = pd.read_csv(dir_ratio_prune)
    # for k in range(df_prune.shape[0]):
    #     df_prune.loc[k,"Encode"] = df_prune.iloc[k,3] / df_prune.iloc[k,4] 
    # df_avg_prune = df_prune.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_prune_df = df_avg_prune.shape[0]

    dir_ratio_improve = path_improve_ratio + dir_r[j] + "_ratio.csv"
    df_improve = pd.read_csv(dir_ratio_improve)
    df_avg_improve = df_improve.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x)
    for k in range(df_avg_improve.shape[0]):
        df_avg_improve.loc[k,"Encode"] = df_avg_improve.iloc[k,4] / df_avg_improve.iloc[k,5] 
    len_improve_df = df_avg_improve.shape[0]  

    for i in range(len_rd_df):
        cr = df_avg_rd.iloc[i,-1]*pow(2,df_avg_rd.iloc[i,1])
        df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        index_re += 1
    
    for i in range(len_bws_df):
        cr = df_avg_bws.iloc[i,-1]*pow(2,df_avg_bws.iloc[i,1])
        df_result.loc[index_re] = [df_avg_bws.iloc[i,0],dir_r[j],df_avg_bws.iloc[i,1],cr]
        index_re += 1

    # for i in range(len_prune_df):
    #     cr = df_avg_prune.iloc[i,-1]*pow(2,df_avg_prune.iloc[i,1])
    #     df_result.loc[index_re] = [df_avg_prune.iloc[i,0],dir_r[j],df_avg_prune.iloc[i,1],cr]
    #     index_re += 1

    for i in range(len_improve_df):
        cr = df_avg_improve.iloc[i,-1]*pow(2,df_avg_improve.iloc[i,1])
        df_result.loc[index_re] = ["TS_2DIFF+BOS-B",dir_r[j],df_avg_improve.iloc[i,1],cr]
        index_re += 1

        
# print(df_result)
df_result.to_csv('./block_size_decode_time.csv',index=False)