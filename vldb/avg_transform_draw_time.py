import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]
# path_datasets = '../iotdb_test_small/' 
path_ratio = './compression_ratio/sota_ratio/' 
path_rr_ratio =  './compression_ratio/elf/'  
path_ratio_outlier =  './compression_ratio/bos/'  
path_pfor_ratio =  './compression_ratio/pfor_ratio/' 
path_sprintz_bos_ratio =  './compression_ratio/sprintz_bos/' 
path_rle_bos_ratio =  './compression_ratio/rle_bos/' 
path_amortization_bos_ratio =  './compression_ratio/bos_amortization/' 
path_rle_bos_amo_ratio = './compression_ratio/rle_bos_amortization/'
path_sprintz_bos_amo_ratio = './compression_ratio/sprintz_bos_amortization/'
path_bws_ratio = './compression_ratio/bws/'
path_rle_bws_ratio = './compression_ratio/rle_bws/'
path_sprintz_bws_ratio = './compression_ratio/sprintz_bws/'
path_pruning_bos_ratio = './compression_ratio/pruning_bos/'
path_pruning_sprintz_ratio = './compression_ratio/sprintz_pruning/'
path_pruning_rle_ratio = './compression_ratio/rle_pruning/'


df_result = pd.DataFrame(columns=['Encoding','Dataset','Encoding Time'])
result_count = 0
# for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
for j in range(len(dir_r)):
    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    # print(dir_ratio)
    df = pd.read_csv(dir_ratio)
    # df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('TS_2DIFF', 'FOR-DELTA')
    # print(df)
    for k in range(df.shape[0]):
        df.loc[k,"Encode"] = df.iloc[k,4] / df.iloc[k,8]
    df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_6_df = df_avg.shape[0]


    dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
    df_rr = pd.read_csv(dir_ratio_rr)
    df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor32', 'Elf')
    for k in range(df_rr.shape[0]):
        df_rr.loc[k,"Encode"] = df_rr.iloc[k,4] / df_rr.iloc[k,8] 
    df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rr_df = df_avg_rr.shape[0]

    dir_ratio_outlier = path_ratio_outlier + dir_r[j] + "_ratio.csv"
    df_outlier = pd.read_csv(dir_ratio_outlier)
    # df_outlier['Encoding Algorithm'] = df_outlier['Encoding Algorithm'].replace('Outlier', "TS_2DIFF+BOS")
    for k in range(df_outlier.shape[0]):
        df_outlier.loc[k,"Encode"] = df_outlier.iloc[k,2] / df_outlier.iloc[k,4]
    df_avg_outlier = df_outlier.groupby(by = df_outlier['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_df_outlier = df_avg_outlier.shape[0]

    dir_ratio_pfor = path_pfor_ratio + dir_r[j] + "_ratio.csv"
    df_pfor = pd.read_csv(dir_ratio_pfor)
    for k in range(df_pfor.shape[0]):
        df_pfor.loc[k,"Encode"] = df_pfor.iloc[k,4] / df_pfor.iloc[k,8]
    df_avg_pfor = df_pfor.groupby(by = df_pfor['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pfor_df = df_avg_pfor.shape[0]

    dir_ratio_sprintz_bos = path_sprintz_bos_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos = pd.read_csv(dir_ratio_sprintz_bos)
    for k in range(df_sprintz_bos.shape[0]):
        df_sprintz_bos.loc[k,"Encode"] = df_sprintz_bos.iloc[k,2] / df_sprintz_bos.iloc[k,4]

    df_avg_sprintz_bos = df_sprintz_bos.groupby(by = df_sprintz_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_df = df_avg_sprintz_bos.shape[0]

    dir_ratio_rle_bos = path_rle_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos = pd.read_csv(dir_ratio_rle_bos)
    for k in range(df_rle_bos.shape[0]):
        df_rle_bos.loc[k,"Encode"] = df_rle_bos.iloc[k,2] / df_rle_bos.iloc[k,4]
    df_avg_rle_bos = df_rle_bos.groupby(by = df_rle_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_df = df_avg_rle_bos.shape[0]

    dir_ratio_amortization_bos = path_amortization_bos_ratio + dir_r[j] + "_ratio.csv"
    df_amortization_bos = pd.read_csv(dir_ratio_amortization_bos)
    for k in range(df_amortization_bos.shape[0]):
        df_amortization_bos.loc[k,"Encode"] = df_amortization_bos.iloc[k,2] / df_amortization_bos.iloc[k,4]
    df_avg_amortization_bos = df_amortization_bos.groupby(by = df_amortization_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_amortization_bos_df = df_avg_amortization_bos.shape[0]

    dir_ratio_rle_bos_amo = path_rle_bos_amo_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos_amo = pd.read_csv(dir_ratio_rle_bos_amo)
    for k in range(df_rle_bos_amo.shape[0]):
        df_rle_bos_amo.loc[k,"Encode"] = df_rle_bos_amo.iloc[k,2] / df_rle_bos_amo.iloc[k,4]
    df_avg_rle_bos_amo = df_rle_bos_amo.groupby(by = df_rle_bos_amo['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_amo_df = df_avg_rle_bos_amo.shape[0]

    dir_ratio_sprintz_bos_amo = path_sprintz_bos_amo_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos_amo = pd.read_csv(dir_ratio_sprintz_bos_amo)
    for k in range(df_sprintz_bos_amo.shape[0]):
        df_sprintz_bos_amo.loc[k,"Encode"] = df_sprintz_bos_amo.iloc[k,2] / df_sprintz_bos_amo.iloc[k,4]
    df_avg_sprintz_bos_amo = df_sprintz_bos_amo.groupby(by = df_sprintz_bos_amo['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_amo_df = df_avg_sprintz_bos_amo.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    for k in range(df_bws.shape[0]):
        df_bws.loc[k,"Encode"] = df_bws.iloc[k,2] / df_bws.iloc[k,4]
    df_avg_bws = df_bws.groupby(by = df_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bws_df = df_avg_bws.shape[0]

    dir_ratio_rle_bws = path_rle_bws_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bws = pd.read_csv(dir_ratio_rle_bws)
    for k in range(df_rle_bws.shape[0]):
        df_rle_bws.loc[k,"Encode"] = df_rle_bws.iloc[k,2] / df_rle_bws.iloc[k,4]
    df_avg_rle_bws = df_rle_bws.groupby(by = df_rle_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bws_df = df_avg_rle_bws.shape[0]

    dir_ratio_sprintz_bws = path_sprintz_bws_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bws = pd.read_csv(dir_ratio_sprintz_bws)
    for k in range(df_sprintz_bws.shape[0]):
        df_sprintz_bws.loc[k,"Encode"] = df_sprintz_bws.iloc[k,2] / df_sprintz_bws.iloc[k,4]
    df_avg_sprintz_bws = df_sprintz_bws.groupby(by = df_sprintz_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bws_df = df_avg_sprintz_bws.shape[0]

    dir_ratio_pruning_bos = path_pruning_bos_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_bos = pd.read_csv(dir_ratio_pruning_bos)
    for k in range(df_pruning_bos.shape[0]):
        df_pruning_bos.loc[k,"Encode"] = df_pruning_bos.iloc[k,2] / df_pruning_bos.iloc[k,4]    
    df_avg_pruning_bos = df_pruning_bos.groupby(by = df_pruning_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_bos_df = df_avg_pruning_bos.shape[0]

    dir_ratio_pruning_sprintz = path_pruning_sprintz_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_sprintz = pd.read_csv(dir_ratio_pruning_sprintz)
    for k in range(df_pruning_sprintz.shape[0]):
        df_pruning_sprintz.loc[k,"Encode"] = df_pruning_sprintz.iloc[k,2] / df_pruning_sprintz.iloc[k,4]    
    df_avg_pruning_sprintz = df_pruning_sprintz.groupby(by = df_pruning_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_sprintz_df = df_avg_pruning_sprintz.shape[0]

    dir_ratio_pruning_rle = path_pruning_rle_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_rle = pd.read_csv(dir_ratio_pruning_rle)
    for k in range(df_pruning_rle.shape[0]):
        df_pruning_rle.loc[k,"Encode"] = df_pruning_rle.iloc[k,2] / df_pruning_rle.iloc[k,4]    
    df_avg_pruning_rle = df_pruning_rle.groupby(by = df_pruning_rle['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_rle_df = df_avg_pruning_rle.shape[0]


    for i in range(len_6_df):
        cr = df_avg.iloc[i,-1]
        df_result.loc[result_count] = [df_avg.iloc[i,0],dir_r[j],cr]
        result_count += 1

    
    for i in range(len_rr_df):
        cr = df_avg_rr.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
        result_count += 1        

    for i in range(len_df_outlier):
        cr = df_avg_outlier.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_outlier.iloc[i,0],dir_r[j],cr]
        result_count += 1  
    
    for i in range(len_pfor_df):
        cr = df_avg_pfor.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pfor.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_sprintz_bos_df):
        cr = df_avg_sprintz_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bos_df):
        cr = df_avg_rle_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_amortization_bos_df):
        cr = df_avg_amortization_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_amortization_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bos_amo_df):
        cr = df_avg_rle_bos_amo.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bos_amo.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_bos_amo_df):
        cr = df_avg_sprintz_bos_amo.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bos_amo.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_bws_df):
        cr = df_avg_bws.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_bws.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bws_df):
        cr = df_avg_rle_bws.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bws.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_bws_df):
        cr = df_avg_sprintz_bws.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bws.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_pruning_bos_df):
        cr = df_avg_pruning_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pruning_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1 

    for i in range(len_pruning_sprintz_df):
        cr = df_avg_pruning_sprintz.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pruning_sprintz.iloc[i,0],dir_r[j],cr]
        result_count += 1 

    for i in range(len_pruning_rle_df):
        cr = df_avg_pruning_rle.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pruning_rle.iloc[i,0],dir_r[j],cr]
        result_count += 1 


# print(df_result)
df_result.to_csv("./compression_ratio/encode_time.csv",index=False)

# path_datasets = './iotdb_datasets_lists'  # 文件目录
dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]
path_ratio = './compression_ratio/sota_ratio/'  # 文件目录
path_rr_ratio =  './compression_ratio/elf/'  # 文件目录
# path_ratio_outlier =  './compression_ratio/outlier/'  # 文件目录

df_result = pd.DataFrame(columns=['Encoding','Dataset','Decoding Time'])
result_i = 0
# for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
for j in range(len(dir_r)):

    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    df = pd.read_csv(dir_ratio)
    # df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('TS_2DIFF', 'FOR-DELTA')
    for k in range(df.shape[0]):
        df.loc[k,"Decode"] = df.iloc[k,5] / df.iloc[k,8]
    df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_6_df = df_avg.shape[0]
    # print(df_avg)


    dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
    df_rr = pd.read_csv(dir_ratio_rr)
    df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor32', 'Elf')
    for k in range(df_rr.shape[0]):
        df_rr.loc[k,"Decode"] = df_rr.iloc[k,5] / df_rr.iloc[k,8] 
    df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rr_df = df_avg_rr.shape[0]

    dir_ratio_outlier = path_ratio_outlier + dir_r[j] + "_ratio.csv"
    df_outlier = pd.read_csv(dir_ratio_outlier)
    # df_outlier['Encoding Algorithm'] = df_outlier['Encoding Algorithm'].replace('Outlier', "TS_2DIFF+BOS")
    for k in range(df_outlier.shape[0]):
        df_outlier.loc[k,"Encode"] = df_outlier.iloc[k,3] / df_outlier.iloc[k,4]
    df_avg_outlier = df_outlier.groupby(by = df_outlier['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_df_outlier = df_avg_outlier.shape[0]

    dir_ratio_pfor = path_pfor_ratio + dir_r[j] + "_ratio.csv"
    df_pfor = pd.read_csv(dir_ratio_pfor)
    for k in range(df_pfor.shape[0]):
        df_pfor.loc[k,"Encode"] = df_pfor.iloc[k,5] / df_pfor.iloc[k,8]

    df_avg_pfor = df_pfor.groupby(by = df_pfor['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pfor_df = df_avg_pfor.shape[0]

    dir_ratio_sprintz_bos = path_sprintz_bos_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos = pd.read_csv(dir_ratio_sprintz_bos)
    for k in range(df_sprintz_bos.shape[0]):
        df_sprintz_bos.loc[k,"Encode"] = df_sprintz_bos.iloc[k,3] / df_sprintz_bos.iloc[k,4]

    df_avg_sprintz_bos = df_sprintz_bos.groupby(by = df_sprintz_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_df = df_avg_sprintz_bos.shape[0]

    dir_ratio_rle_bos = path_rle_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos = pd.read_csv(dir_ratio_rle_bos)
    for k in range(df_rle_bos.shape[0]):
        df_rle_bos.loc[k,"Encode"] = df_rle_bos.iloc[k,3] / df_rle_bos.iloc[k,4]
    df_avg_rle_bos = df_rle_bos.groupby(by = df_rle_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_df = df_avg_rle_bos.shape[0]

    dir_ratio_amortization_bos = path_amortization_bos_ratio + dir_r[j] + "_ratio.csv"
    df_amortization_bos = pd.read_csv(dir_ratio_amortization_bos)
    for k in range(df_amortization_bos.shape[0]):
        df_amortization_bos.loc[k,"Encode"] = df_amortization_bos.iloc[k,3] / df_amortization_bos.iloc[k,4]
    df_avg_amortization_bos = df_amortization_bos.groupby(by = df_amortization_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_amortization_bos_df = df_avg_amortization_bos.shape[0]

    dir_ratio_rle_bos_amo = path_rle_bos_amo_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos_amo = pd.read_csv(dir_ratio_rle_bos_amo)
    for k in range(df_rle_bos_amo.shape[0]):
        df_rle_bos_amo.loc[k,"Encode"] = df_rle_bos_amo.iloc[k,3] / df_rle_bos_amo.iloc[k,4]
    df_avg_rle_bos_amo = df_rle_bos_amo.groupby(by = df_rle_bos_amo['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_amo_df = df_avg_rle_bos_amo.shape[0]

    dir_ratio_sprintz_bos_amo = path_sprintz_bos_amo_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos_amo = pd.read_csv(dir_ratio_sprintz_bos_amo)
    for k in range(df_sprintz_bos_amo.shape[0]):
        df_sprintz_bos_amo.loc[k,"Encode"] = df_sprintz_bos_amo.iloc[k,3] / df_sprintz_bos_amo.iloc[k,4]
    df_avg_sprintz_bos_amo = df_sprintz_bos_amo.groupby(by = df_sprintz_bos_amo['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_amo_df = df_avg_sprintz_bos_amo.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    for k in range(df_bws.shape[0]):
        df_bws.loc[k,"Encode"] = df_bws.iloc[k,3] / df_bws.iloc[k,4]
    df_avg_bws = df_bws.groupby(by = df_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bws_df = df_avg_bws.shape[0]

    dir_ratio_rle_bws = path_rle_bws_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bws = pd.read_csv(dir_ratio_rle_bws)
    for k in range(df_rle_bws.shape[0]):
        df_rle_bws.loc[k,"Encode"] = df_rle_bws.iloc[k,3] / df_rle_bws.iloc[k,4]
    df_avg_rle_bws = df_rle_bws.groupby(by = df_rle_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bws_df = df_avg_rle_bws.shape[0]

    dir_ratio_sprintz_bws = path_sprintz_bws_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bws = pd.read_csv(dir_ratio_sprintz_bws)
    for k in range(df_sprintz_bws.shape[0]):
        df_sprintz_bws.loc[k,"Encode"] = df_sprintz_bws.iloc[k,3] / df_sprintz_bws.iloc[k,4]
    df_avg_sprintz_bws = df_sprintz_bws.groupby(by = df_sprintz_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bws_df = df_avg_sprintz_bws.shape[0]

    dir_ratio_pruning_bos = path_pruning_bos_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_bos = pd.read_csv(dir_ratio_pruning_bos)
    for k in range(df_pruning_bos.shape[0]):
        df_pruning_bos.loc[k,"Encode"] = df_pruning_bos.iloc[k,3] / df_pruning_bos.iloc[k,4]    
    df_avg_pruning_bos = df_pruning_bos.groupby(by = df_pruning_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_bos_df = df_avg_pruning_bos.shape[0]

    dir_ratio_pruning_sprintz = path_pruning_sprintz_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_sprintz = pd.read_csv(dir_ratio_pruning_sprintz)
    for k in range(df_pruning_sprintz.shape[0]):
        df_pruning_sprintz.loc[k,"Encode"] = df_pruning_sprintz.iloc[k,3] / df_pruning_sprintz.iloc[k,4]    
    df_avg_pruning_sprintz = df_pruning_sprintz.groupby(by = df_pruning_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_sprintz_df = df_avg_pruning_sprintz.shape[0]

    dir_ratio_pruning_rle = path_pruning_rle_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_rle = pd.read_csv(dir_ratio_pruning_rle)
    for k in range(df_pruning_rle.shape[0]):
        df_pruning_rle.loc[k,"Encode"] = df_pruning_rle.iloc[k,3] / df_pruning_rle.iloc[k,4]    
    df_avg_pruning_rle = df_pruning_rle.groupby(by = df_pruning_rle['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_rle_df = df_avg_pruning_rle.shape[0]

    for i in range(len_6_df):
        cr = df_avg.iloc[i,-1]
        df_result.loc[result_i] = [df_avg.iloc[i,0],dir_r[j],cr]
        result_i += 1
    

    for i in range(len_rr_df):
        cr = df_avg_rr.iloc[i,-1]
        df_result.loc[result_i] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
        result_i += 1

    for i in range(len_df_outlier):
        cr = df_avg_outlier.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_outlier.iloc[i,0],dir_r[j],cr]
        result_count += 1  
    
    for i in range(len_pfor_df):
        cr = df_avg_pfor.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pfor.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_sprintz_bos_df):
        cr = df_avg_sprintz_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bos_df):
        cr = df_avg_rle_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_amortization_bos_df):
        cr = df_avg_amortization_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_amortization_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bos_amo_df):
        cr = df_avg_rle_bos_amo.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bos_amo.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_sprintz_bos_amo_df):
        cr = df_avg_sprintz_bos_amo.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bos_amo.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_bws_df):
        cr = df_avg_bws.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_bws.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bws_df):
        cr = df_avg_rle_bws.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bws.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_bws_df):
        cr = df_avg_sprintz_bws.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bws.iloc[i,0],dir_r[j],cr]
        result_count += 1
    for i in range(len_pruning_bos_df):
        cr = df_avg_pruning_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pruning_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1 

    for i in range(len_pruning_sprintz_df):
        cr = df_avg_pruning_sprintz.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pruning_sprintz.iloc[i,0],dir_r[j],cr]
        result_count += 1 

    for i in range(len_pruning_rle_df):
        cr = df_avg_pruning_rle.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pruning_rle.iloc[i,0],dir_r[j],cr]
        result_count += 1 

# print(df_result)
df_result.to_csv("./compression_ratio/decode_time.csv",index=False)