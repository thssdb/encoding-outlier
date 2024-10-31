import os
import pandas as pd

path_test_beta_ratio = ['./time/bos_m/','./time/tsdiff/']
path_pfor_ratio = ['./time/pfor_ratio/']

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]

df_result = pd.DataFrame(columns=['Encoding','Dataset','Decode Time','Output Time'])
result_i = 0
result_count = 0
for j in range(len(dir_r)):

    for path_test_ratio in path_test_beta_ratio:
        
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        # print(df_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Decode"] = df_test.iloc[k,3] / df_test.iloc[k,6]    
            df_test.loc[k,"Output"] = df_test.iloc[k,5] / df_test.iloc[k,6] 
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]
        # print(df_avg_test)

        for i in range(len_test_df):
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],df_avg_test.iloc[i,-2],df_avg_test.iloc[i,-1]]
            result_count += 1 
    
    for path_test_ratio in path_pfor_ratio:
        
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df = pd.read_csv(dir_ratio_test)
        df_test= df[df['Encoding Algorithm'].str.contains('TS_2DIFF')].reset_index(drop=True)
        # print(df_test["Points"]) 
        # print(df_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Decode"] = df_test.iloc[k,5] / df_test.iloc[k,8]    
            df_test.loc[k,"Output"] = df_test.iloc[k,7] / df_test.iloc[k,8]   
        # print(df_test) 
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # print(df_avg_test)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],df_avg_test.iloc[i,-2],df_avg_test.iloc[i,-1]]
            result_count += 1 

df_result.to_csv("./time/query_time.csv",index=False)

df_result = pd.DataFrame(columns=['Encoding','Dataset','Storage Cost'])
res_index = 0
for j in range(len(dir_r)):

    for path_test_ratio in path_test_beta_ratio:
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Cost"] = df_test.iloc[k,8] * 32
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            cr = df_avg_test.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_test.iloc[i,0],dir_r[j],cr]
            res_index += 1

    for path_test_ratio in path_pfor_ratio:
        
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df = pd.read_csv(dir_ratio_test)
        df_test= df[df['Encoding Algorithm'].str.contains('TS_2DIFF')].reset_index(drop=True)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Cost"] = df_test.iloc[k,10] * 32
        # for k in range(df_test.shape[0]):
        #     df_test.loc[k,"Decode"] = df_test.iloc[k,9] / df_test.iloc[k,8]    
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            cr = df_avg_test.iloc[i,-1]
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],cr]
            result_count += 1 

df_result.to_csv("./time/storage_cost.csv",index=False)
