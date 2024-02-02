import os
import pandas as pd

# path_datasets = '../iotdb_test_small/'  
path_ratio = './compression_ratio/sota_ratio/'  
dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]


path_rd_ratio =  './compression_ratio/bos/' 
path_rr_ratio =  './compression_ratio/elf/' 
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


df_result = pd.DataFrame(columns=['Encoding','Dataset','Compression Ratio'])
res_index = 0
# for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
for j in range(len(dir_r)):
    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    df = pd.read_csv(dir_ratio)
    # if dir_r[j] == "GW-Magnetic":
    #     print(df)
    # df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('TS_2DIFF', 'FOR-DELTA')
    df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # if dir_r[j] == "GW-Magnetic":
    #     print(df_avg)
    len_6_df = df_avg.shape[0]

    dir_ratio_rd = path_rd_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    # df_rd['Encoding Algorithm'] = df_rd['Encoding Algorithm'].replace('Outlier', 'FOR-DELTA+BOS')
    df_avg_rd = df_rd.groupby(by = df_rd['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # for k in range(df_avg_rd.shape[0]):
    #     df_avg_rd.loc[k,"CR"] = df_avg_rd.iloc[k,4] / (8*df_avg_rd.iloc[k,3])        
    len_rd_df = df_avg_rd.shape[0]

    dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
    df_rr = pd.read_csv(dir_ratio_rr)
    # df_rr = df_rr[df_rr['Encoding Algorithm'] == "ElfCompressor"]
    df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor32', 'Elf')
    df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # print(df_avg_rr)
    len_rr_df = df_avg_rr.shape[0]

    dir_ratio_pfor = path_pfor_ratio + dir_r[j] + "_ratio.csv"
    df_pfor = pd.read_csv(dir_ratio_pfor)
    # df_rr = df_rr[df_rr['Encoding Algorithm'] == "ElfCompressor"]
    # df_btr['Encoding Algorithm'] = df_btr['Encoding Algorithm'].replace('ElfCompressor32', 'Elf')
    df_avg_pfor = df_pfor.groupby(by = df_pfor['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # print(df_avg_btr)
    len_pfor_df = df_avg_pfor.shape[0]

    dir_ratio_pruning_bos = path_pruning_bos_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_bos = pd.read_csv(dir_ratio_pruning_bos)
    df_avg_pruning_bos = df_pruning_bos.groupby(by = df_pruning_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_bos_df = df_avg_pruning_bos.shape[0]

    dir_ratio_sprintz_bos = path_sprintz_bos_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos = pd.read_csv(dir_ratio_sprintz_bos)
    df_avg_sprintz_bos = df_sprintz_bos.groupby(by = df_sprintz_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_df = df_avg_sprintz_bos.shape[0]

    dir_ratio_rle_bos = path_rle_bos_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos = pd.read_csv(dir_ratio_rle_bos)
    df_avg_rle_bos = df_rle_bos.groupby(by = df_rle_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_df = df_avg_rle_bos.shape[0]

    dir_ratio_amortization_bos = path_amortization_bos_ratio + dir_r[j] + "_ratio.csv"
    df_amortization_bos = pd.read_csv(dir_ratio_amortization_bos)
    df_avg_amortization_bos = df_amortization_bos.groupby(by = df_amortization_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_amortization_bos_df = df_avg_amortization_bos.shape[0]

    dir_ratio_rle_bos_amo = path_rle_bos_amo_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos_amo = pd.read_csv(dir_ratio_rle_bos_amo)
    df_avg_rle_bos_amo = df_rle_bos_amo.groupby(by = df_rle_bos_amo['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_amo_df = df_avg_rle_bos_amo.shape[0]

    dir_ratio_sprintz_bos_amo = path_sprintz_bos_amo_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos_amo = pd.read_csv(dir_ratio_sprintz_bos_amo)
    df_avg_sprintz_bos_amo = df_sprintz_bos_amo.groupby(by = df_sprintz_bos_amo['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_amo_df = df_avg_sprintz_bos_amo.shape[0]

    dir_ratio_bws = path_bws_ratio + dir_r[j] + "_ratio.csv"
    df_bws = pd.read_csv(dir_ratio_bws)
    df_avg_bws = df_bws.groupby(by = df_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bws_df = df_avg_bws.shape[0]

    dir_ratio_rle_bws = path_rle_bws_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bws = pd.read_csv(dir_ratio_rle_bws)
    df_avg_rle_bws = df_rle_bws.groupby(by = df_rle_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bws_df = df_avg_rle_bws.shape[0]

    dir_ratio_sprintz_bws = path_sprintz_bws_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bws = pd.read_csv(dir_ratio_sprintz_bws)
    df_avg_sprintz_bws = df_sprintz_bws.groupby(by = df_sprintz_bws['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bws_df = df_avg_sprintz_bws.shape[0]

    dir_ratio_pruning_sprintz = path_pruning_sprintz_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_sprintz = pd.read_csv(dir_ratio_pruning_sprintz)   
    df_avg_pruning_sprintz = df_pruning_sprintz.groupby(by = df_pruning_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_sprintz_df = df_avg_pruning_sprintz.shape[0]

    dir_ratio_pruning_rle = path_pruning_rle_ratio + dir_r[j] + "_ratio.csv"
    df_pruning_rle = pd.read_csv(dir_ratio_pruning_rle)  
    df_avg_pruning_rle = df_pruning_rle.groupby(by = df_pruning_rle['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pruning_rle_df = df_avg_pruning_rle.shape[0]

    for i in range(len_6_df):
        cr = 1/df_avg.iloc[i,-1]
        df_result.loc[res_index] = [df_avg.iloc[i,0],dir_r[j],cr]
        res_index += 1

    
    for i in range(len_rd_df):
        cr = 1/df_avg_rd.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_rd.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_rr_df):
        cr = 1/df_avg_rr.iloc[i,-2]
        df_result.loc[res_index] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_pfor_df):
        cr = 1/df_avg_pfor.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_pfor.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_sprintz_bos_df):
        cr = 1/df_avg_sprintz_bos.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_sprintz_bos.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_rle_bos_df):
        cr = 1/df_avg_rle_bos.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_rle_bos.iloc[i,0],dir_r[j],cr]
        res_index += 1
    
    for i in range(len_amortization_bos_df):
        cr = 1/df_avg_amortization_bos.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_amortization_bos.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_rle_bos_amo_df):
        cr = 1/df_avg_rle_bos_amo.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_rle_bos_amo.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_sprintz_bos_amo_df):
        cr = 1/df_avg_sprintz_bos_amo.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_sprintz_bos_amo.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_bws_df):
        cr = 1/df_avg_bws.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_bws.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_rle_bws_df):
        cr = 1/df_avg_rle_bws.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_rle_bws.iloc[i,0],dir_r[j],cr]
        res_index += 1
    
    for i in range(len_sprintz_bws_df):
        cr = 1/df_avg_sprintz_bws.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_sprintz_bws.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_pruning_bos_df):
        cr = 1/df_avg_pruning_bos.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_pruning_bos.iloc[i,0],dir_r[j],cr]
        res_index += 1       

    for i in range(len_pruning_sprintz_df):
        cr = 1/df_avg_pruning_sprintz.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_pruning_sprintz.iloc[i,0],dir_r[j],cr]
        res_index += 1 

    for i in range(len_pruning_rle_df):
        cr = 1/df_avg_pruning_rle.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_pruning_rle.iloc[i,0],dir_r[j],cr]
        res_index += 1 

# print(df_result)
df_result.to_csv("./compression_ratio/compression_ratio.csv",index=False)