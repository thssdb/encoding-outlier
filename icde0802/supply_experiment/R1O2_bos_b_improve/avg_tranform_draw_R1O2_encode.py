import os
import pandas as pd

# parent_dir = "/Users/xiaojinzhao/Documents/GitHub/encoding-outlier/icde0802/compression_ratio/"
parent_dir = "/Users/zihanguo/Downloads/R/outlier/outliier_code/encoding-outlier/icde0802/compression_ratio/"
# path_bos_ratio = parent_dir + 'bos/'  


path_prune_ratio = parent_dir + 'block_size_bos_improve/'#path_improve_ratio = parent_dir + '/encoding-outlier/icde0802/compression_ratio/block_size_bos_improve/'

path_test_beta_ratio =[path_prune_ratio]# ['./compression_ratio/bos_m/','./compression_ratio/bos_b/','./compression_ratio/bos_v/']

path_bws_ratio = parent_dir + 'bos_b/'  
path_bos_improve_ratio = parent_dir + 'bos_b_improve/' 
path_bos_m = parent_dir + 'bos_m/'  
path_bos_m_improve = parent_dir + 'bos_m_improve/' 
path_pfor_ratio = [path_bws_ratio,path_bos_improve_ratio,path_bos_m,path_bos_m_improve]

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]

df_result = pd.DataFrame(columns=['Encoding','Dataset','Decode Time','Compression Ratio'])
result_i = 0
result_count = 0
for j in range(len(dir_r)):

    # for path_test_ratio in path_test_beta_ratio:
        
    #     dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
    #     df_test = pd.read_csv(dir_ratio_test)
    #     df_test['Encoding Algorithm'] = df_test['Encoding Algorithm'].replace({
    #     'TS_2DIFF+BOS-V': 'BOS-V',   
    #     'TS_2DIFF+BOS-M': 'BOS-M',
    #     'TS_2DIFF+BOS-B':'BOS-B'
    #     })
        
    #     df_test = df_test[df_test['Block Size']==10].reset_index()
        
    #     # print(df_test)
    #     # print(df_test)
    #     for k in range(df_test.shape[0]):
    #         df_test.loc[k,"Decode"] = df_test.iloc[k,3] / df_test.iloc[k,5]    
    #         # df_test.loc[k,"Output"] = df_test.iloc[k,5] / df_test.iloc[k,6] 
    #     df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    #     len_test_df = df_avg_test.shape[0]
    #     # print(df_avg_test)

    #     for i in range(len_test_df):
    #         df_result.loc[result_count] = ["BOS-B-Improve",dir_r[j],df_avg_test.iloc[i,-1]]
    #         result_count += 1 
    
    for path_test_ratio in path_pfor_ratio:
        
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        df_test['Encoding Algorithm'] = df_test['Encoding Algorithm'].replace({
        'TS_2DIFF+BOS-V': 'BOS-V',   
        'TS_2DIFF+BOS-M': 'BOS-M',
        'TS_2DIFF+BOS-B':'BOS-B'
        })
        # df_test= df[df['Encoding Algorithm'].str.contains('TS_2DIFF')].reset_index(drop=True)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Decode"] = df_test.iloc[k,2] / df_test.iloc[k,4]    
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]
        encoding_name = "BOS-B"
        if path_test_ratio == path_bos_improve_ratio:
            encoding_name = "BOS-B-Improve"
        elif path_test_ratio == path_bos_m:
            encoding_name = "BOS-M"
        elif path_test_ratio == path_bos_m_improve:
            encoding_name = "BOS-M-Improve"


        for i in range(len_test_df):
            df_result.loc[result_count] = [encoding_name,dir_r[j],df_avg_test.iloc[i,-1],1/df_avg_test.iloc[i,-2]]
            result_count += 1 


df_result.to_csv("./encode_time.csv",index=False)

# df_result = pd.DataFrame(columns=['Encoding','Dataset','Storage Cost'])
# res_index = 0
# for j in range(len(dir_r)):

#     for path_test_ratio in path_test_beta_ratio:
#         dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
#         df_test = pd.read_csv(dir_ratio_test)
#         for k in range(df_test.shape[0]):
#             df_test.loc[k,"Cost"] = df_test.iloc[k,8] * 32
#         df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
#         len_test_df = df_avg_test.shape[0]

#         for i in range(len_test_df):
#             cr = df_avg_test.iloc[i,-1]
#             df_result.loc[res_index] = [df_avg_test.iloc[i,0],dir_r[j],cr]
#             res_index += 1

#     for path_test_ratio in path_pfor_ratio:
        
#         dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
#         df = pd.read_csv(dir_ratio_test)
#         df_test= df[df['Encoding Algorithm'].str.contains('TS_2DIFF')].reset_index(drop=True)
#         for k in range(df_test.shape[0]):
#             df_test.loc[k,"Cost"] = df_test.iloc[k,10] * 32
#         # for k in range(df_test.shape[0]):
#         #     df_test.loc[k,"Decode"] = df_test.iloc[k,9] / df_test.iloc[k,8]    
#         df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
#         len_test_df = df_avg_test.shape[0]

#         for i in range(len_test_df):
#             cr = df_avg_test.iloc[i,-1]
#             df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],cr]
#             result_count += 1 

# df_result.to_csv("./time/storage_cost.csv",index=False)
