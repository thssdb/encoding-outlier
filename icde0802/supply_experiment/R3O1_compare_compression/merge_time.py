import os
import pandas as pd

# path_datasets = '../iotdb_test_small/'  
dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]
path_bp = './compression_ratio/bos_m_comp/'  
path_bos = './compression_ratio/bp_comp/'  
path_dct = './compression_ratio/dct_comp/'
path_dct2 = './compression_ratio/dct_comp2/'
path_lz4 = './compression_ratio/lz4_comp/'
path_lz42 = './compression_ratio/bos_m_lz4_comp/'
path_fft = './compression_ratio/fft_comp/'
path_fft2 = './compression_ratio/fft_bos_comp/'
# path_bp = './compression_ratio/bp_c_ratio/'  
# path_rle = './compression_ratio/rle_m_c/'  
# path_sprintz = './compression_ratio/sprintz_m_c/'  
# path_ts = './compression_ratio/bos_m_c/'  
# path_test_beta_ratio = ['./compression_ratio/bp_c_ratio/' ,'./compression_ratio/rle_m_c/'  ,'./compression_ratio/sprintz_m_c/'  ,'./compression_ratio/bos_m_c/'  ]
path_test_beta_ratio = [path_bp,path_bos,path_dct2,path_dct,path_lz4,path_lz42,path_fft,path_fft2]
df_result = pd.DataFrame(columns=['Compression','Dataset','Compression Time'])
res_index = 0
# for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
for j in range(len(dir_r)):

    for path_test_ratio in path_test_beta_ratio:
        dir_ratio_rd = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_rd = pd.read_csv(dir_ratio_rd)
        df_avg_rd = df_rd.groupby(by = df_rd['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        for k in range(df_avg_rd.shape[0]):
            df_avg_rd.loc[k,"Encode"] = df_avg_rd.iloc[k,2] / df_avg_rd.iloc[k,4]    
            # df_test.loc[k,"Output"] = df_test.iloc[k,5] / df_test.iloc[k,6]        
        len_rd_df = df_avg_rd.shape[0]
        # print(df_avg_rd)
        
        for i in range(len_rd_df):
            cr = df_avg_rd.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_rd.iloc[i,0],dir_r[j],cr]
            res_index += 1

path_test_beta_ratio = ['./compression_ratio/fft/','./compression_ratio/fft_bos/','./compression_ratio/dwt/','./compression_ratio/dwt_bos/']
# for j in range(len(dir_r)):



for path_test_ratio in path_test_beta_ratio:
# dir_ratio_rd = path_test_ratio + dir_r[j] + "_ratio.csv"
# df_rd = pd.read_csv(dir_ratio_rd)
# df_avg_rd = df_rd.groupby(by = df_rd['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)       
# len_rd_df = df_avg_rd.shape[0]
# 
    # print(df_avg_rd)
    dir_ratio_rd = path_test_ratio + "compression_results.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    df_avg_rd = df_rd.groupby(by = df_rd['folder'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)       
    len_rd_df = df_avg_rd.shape[0]
    # print(df_avg_rd)

    for i in range(len_rd_df):
        # cr = 1/df_avg_rd.iloc[i,-1]
        dataset_name = df_avg_rd.iloc[i,0].split("/")[-1]
        if dataset_name in dir_r:
            if path_test_ratio == './compression_ratio/fft/':
                df_result.loc[res_index] = ["FFT",dataset_name,df_avg_rd.iloc[i,-1]]
            elif path_test_ratio == './compression_ratio/fft_bos/':
                df_result.loc[res_index] = ["BOS+FFT",dataset_name,df_avg_rd.iloc[i,-1]]
            # elif path_test_ratio == './compression_ratio/dwt/':
            #     df_result.loc[res_index] = ["DCT",dataset_name,df_avg_rd.iloc[i,-1]]
            # elif path_test_ratio == './compression_ratio/dwt_bos/':
            #     df_result.loc[res_index] = ["BOS+DCT",dataset_name,df_avg_rd.iloc[i,-1]]
            res_index += 1


df_result.to_csv("./compression_ratio/time.csv",index=False)