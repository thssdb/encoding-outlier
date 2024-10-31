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
path_m_bos_ratio =  './compression_ratio/bos_m_improve/' 
path_rle_bos_m_ratio = './compression_ratio/rle_bos_m_improve/'
path_sprintz_bos_m_ratio = './compression_ratio/sprintz_bos_m_improve/'
path_bosb_ratio = './compression_ratio/bos_b_improve/'
path_rle_bosb_ratio = './compression_ratio/rle_bos_b_improve/'
path_sprintz_bosb_ratio = './compression_ratio/sprintz_bos_b_improve/'
path_tsdiff_ratio = './compression_ratio/tsdiff/'
path_sprintz_ratio = './compression_ratio/sprintz/'

# path_pruning_bos_ratio = './compression_ratio/pruning_bos/'
# path_pruning_sprintz_ratio = './compression_ratio/sprintz_pruning/'
# path_pruning_rle_ratio = './compression_ratio/rle_pruning/'
# path_test_ratio = './compression_ratio/test_2_point/'
path_test_beta_ratio = ['./compression_ratio/tsdiff/','./compression_ratio/rle/']

df_result = pd.DataFrame(columns=['Encoding','Dataset','Encoding Time'])
result_count = 0
# for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
for j in range(len(dir_r)):
    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    # print(dir_ratio)
    df = pd.read_csv(dir_ratio)
    df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('TS_2DIFF', 'OTHER')
    df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('SPRINTZ', 'OTHER')
    df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('RLE', 'OTHER')
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

    dir_ratio_m_bos = path_m_bos_ratio + dir_r[j] + "_ratio.csv"
    df_m_bos = pd.read_csv(dir_ratio_m_bos)
    for k in range(df_m_bos.shape[0]):
        df_m_bos.loc[k,"Encode"] = df_m_bos.iloc[k,2] / df_m_bos.iloc[k,4]
    df_avg_m_bos = df_m_bos.groupby(by = df_m_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_m_bos_df = df_avg_m_bos.shape[0]

    dir_ratio_rle_bos_m = path_rle_bos_m_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos_m = pd.read_csv(dir_ratio_rle_bos_m)
    for k in range(df_rle_bos_m.shape[0]):
        df_rle_bos_m.loc[k,"Encode"] = df_rle_bos_m.iloc[k,2] / df_rle_bos_m.iloc[k,4]
    df_avg_rle_bos_m = df_rle_bos_m.groupby(by = df_rle_bos_m['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_m_df = df_avg_rle_bos_m.shape[0]

    dir_ratio_sprintz_bos_m = path_sprintz_bos_m_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos_m = pd.read_csv(dir_ratio_sprintz_bos_m)
    for k in range(df_sprintz_bos_m.shape[0]):
        df_sprintz_bos_m.loc[k,"Encode"] = df_sprintz_bos_m.iloc[k,2] / df_sprintz_bos_m.iloc[k,4]
    df_avg_sprintz_bos_m = df_sprintz_bos_m.groupby(by = df_sprintz_bos_m['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_m_df = df_avg_sprintz_bos_m.shape[0]

    dir_ratio_bosb = path_bosb_ratio + dir_r[j] + "_ratio.csv"
    df_bosb = pd.read_csv(dir_ratio_bosb)
    for k in range(df_bosb.shape[0]):
        df_bosb.loc[k,"Encode"] = df_bosb.iloc[k,2] / df_bosb.iloc[k,4]
    df_avg_bosb = df_bosb.groupby(by = df_bosb['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bosb_df = df_avg_bosb.shape[0]

    dir_ratio_rle_bosb = path_rle_bosb_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bosb = pd.read_csv(dir_ratio_rle_bosb)
    for k in range(df_rle_bosb.shape[0]):
        df_rle_bosb.loc[k,"Encode"] = df_rle_bosb.iloc[k,2] / df_rle_bosb.iloc[k,4]
    df_avg_rle_bosb = df_rle_bosb.groupby(by = df_rle_bosb['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bosb_df = df_avg_rle_bosb.shape[0]

    dir_ratio_sprintz_bosb = path_sprintz_bosb_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bosb = pd.read_csv(dir_ratio_sprintz_bosb)
    for k in range(df_sprintz_bosb.shape[0]):
        df_sprintz_bosb.loc[k,"Encode"] = df_sprintz_bosb.iloc[k,2] / df_sprintz_bosb.iloc[k,4]
    df_avg_sprintz_bosb = df_sprintz_bosb.groupby(by = df_sprintz_bosb['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bosb_df = df_avg_sprintz_bosb.shape[0]

    dir_ratio_sprintz = path_sprintz_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz = pd.read_csv(dir_ratio_sprintz)
    for k in range(df_sprintz.shape[0]):
        df_sprintz.loc[k,"Encode"] = df_sprintz.iloc[k,2] / df_sprintz.iloc[k,4]
    df_avg_sprintz = df_sprintz.groupby(by = df_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_df = df_avg_sprintz.shape[0]

    for path_test_ratio in path_test_beta_ratio:
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Encode"] = df_test.iloc[k,2] / df_test.iloc[k,4]    
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            cr = df_avg_test.iloc[i,-1]
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],cr]
            result_count += 1 
    # dir_ratio_pruning_bos = path_tsdiff_ratio + dir_r[j] + "_ratio.csv"
    # df_pruning_bos = pd.read_csv(dir_ratio_pruning_bos)
    # for k in range(df_pruning_bos.shape[0]):
    #     df_pruning_bos.loc[k,"Encode"] = df_pruning_bos.iloc[k,2] / df_pruning_bos.iloc[k,4]    
    # df_avg_pruning_bos = df_pruning_bos.groupby(by = df_pruning_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_pruning_bos_df = df_avg_pruning_bos.shape[0]

    # dir_ratio_pruning_sprintz = path_pruning_sprintz_ratio + dir_r[j] + "_ratio.csv"
    # df_pruning_sprintz = pd.read_csv(dir_ratio_pruning_sprintz)
    # for k in range(df_pruning_sprintz.shape[0]):
    #     df_pruning_sprintz.loc[k,"Encode"] = df_pruning_sprintz.iloc[k,2] / df_pruning_sprintz.iloc[k,4]    
    # df_avg_pruning_sprintz = df_pruning_sprintz.groupby(by = df_pruning_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_pruning_sprintz_df = df_avg_pruning_sprintz.shape[0]

    # dir_ratio_pruning_rle = path_pruning_rle_ratio + dir_r[j] + "_ratio.csv"
    # df_pruning_rle = pd.read_csv(dir_ratio_pruning_rle)
    # for k in range(df_pruning_rle.shape[0]):
    #     df_pruning_rle.loc[k,"Encode"] = df_pruning_rle.iloc[k,2] / df_pruning_rle.iloc[k,4]    
    # df_avg_pruning_rle = df_pruning_rle.groupby(by = df_pruning_rle['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_pruning_rle_df = df_avg_pruning_rle.shape[0]



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

    for i in range(len_m_bos_df):
        cr = df_avg_m_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_m_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bos_m_df):
        cr = df_avg_rle_bos_m.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bos_m.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_bos_m_df):
        cr = df_avg_sprintz_bos_m.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bos_m.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_bosb_df):
        cr = df_avg_bosb.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_bosb.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bosb_df):
        cr = df_avg_rle_bosb.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bosb.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_bosb_df):
        cr = df_avg_sprintz_bosb.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bosb.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_df):
        cr = df_avg_sprintz.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz.iloc[i,0],dir_r[j],cr]
        result_count += 1
    # for i in range(len_pruning_bos_df):
    #     cr = df_avg_pruning_bos.iloc[i,-1]
    #     df_result.loc[result_count] = [df_avg_pruning_bos.iloc[i,0],dir_r[j],cr]
    #     result_count += 1 

    # for i in range(len_pruning_sprintz_df):
    #     cr = df_avg_pruning_sprintz.iloc[i,-1]
    #     df_result.loc[result_count] = [df_avg_pruning_sprintz.iloc[i,0],dir_r[j],cr]
    #     result_count += 1 

    # for i in range(len_pruning_rle_df):
    #     cr = df_avg_pruning_rle.iloc[i,-1]
    #     df_result.loc[result_count] = [df_avg_pruning_rle.iloc[i,0],dir_r[j],cr]
    #     result_count += 1 

    for path_test_ratio in path_test_beta_ratio:
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Encode"] = df_test.iloc[k,2] / df_test.iloc[k,4]    
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            cr = df_avg_test.iloc[i,-1]
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],cr]
            result_count += 1 


# print(df_result)
df_result.to_csv("./compression_ratio/encode_time_improve.csv",index=False)

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
    df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('SPRINTZ', 'OTHER')
    df['Encoding Algorithm'] = df['Encoding Algorithm'].replace('RLE', 'OTHER')
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

    dir_ratio_m_bos = path_m_bos_ratio + dir_r[j] + "_ratio.csv"
    df_m_bos = pd.read_csv(dir_ratio_m_bos)
    for k in range(df_m_bos.shape[0]):
        df_m_bos.loc[k,"Encode"] = df_m_bos.iloc[k,3] / df_m_bos.iloc[k,4]
    df_avg_m_bos = df_m_bos.groupby(by = df_m_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_m_bos_df = df_avg_m_bos.shape[0]

    dir_ratio_rle_bos_m = path_rle_bos_m_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bos_m = pd.read_csv(dir_ratio_rle_bos_m)
    for k in range(df_rle_bos_m.shape[0]):
        df_rle_bos_m.loc[k,"Encode"] = df_rle_bos_m.iloc[k,3] / df_rle_bos_m.iloc[k,4]
    df_avg_rle_bos_m = df_rle_bos_m.groupby(by = df_rle_bos_m['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bos_m_df = df_avg_rle_bos_m.shape[0]

    dir_ratio_sprintz_bos_m = path_sprintz_bos_m_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bos_m = pd.read_csv(dir_ratio_sprintz_bos_m)
    for k in range(df_sprintz_bos_m.shape[0]):
        df_sprintz_bos_m.loc[k,"Encode"] = df_sprintz_bos_m.iloc[k,3] / df_sprintz_bos_m.iloc[k,4]
    df_avg_sprintz_bos_m = df_sprintz_bos_m.groupby(by = df_sprintz_bos_m['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bos_m_df = df_avg_sprintz_bos_m.shape[0]

    dir_ratio_bosb = path_bosb_ratio + dir_r[j] + "_ratio.csv"
    df_bosb = pd.read_csv(dir_ratio_bosb)
    for k in range(df_bosb.shape[0]):
        df_bosb.loc[k,"Encode"] = df_bosb.iloc[k,3] / df_bosb.iloc[k,4]
    df_avg_bosb = df_bosb.groupby(by = df_bosb['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_bosb_df = df_avg_bosb.shape[0]

    dir_ratio_rle_bosb = path_rle_bosb_ratio + dir_r[j] + "_ratio.csv"
    df_rle_bosb = pd.read_csv(dir_ratio_rle_bosb)
    for k in range(df_rle_bosb.shape[0]):
        df_rle_bosb.loc[k,"Encode"] = df_rle_bosb.iloc[k,3] / df_rle_bosb.iloc[k,4]
    df_avg_rle_bosb = df_rle_bosb.groupby(by = df_rle_bosb['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rle_bosb_df = df_avg_rle_bosb.shape[0]

    dir_ratio_sprintz_bosb = path_sprintz_bosb_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz_bosb = pd.read_csv(dir_ratio_sprintz_bosb)
    for k in range(df_sprintz_bosb.shape[0]):
        df_sprintz_bosb.loc[k,"Encode"] = df_sprintz_bosb.iloc[k,3] / df_sprintz_bosb.iloc[k,4]
    df_avg_sprintz_bosb = df_sprintz_bosb.groupby(by = df_sprintz_bosb['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_bosb_df = df_avg_sprintz_bosb.shape[0]

    dir_ratio_sprintz = path_sprintz_ratio + dir_r[j] + "_ratio.csv"
    df_sprintz = pd.read_csv(dir_ratio_sprintz)
    for k in range(df_sprintz.shape[0]):
        df_sprintz.loc[k,"Encode"] = df_sprintz.iloc[k,3] / df_sprintz.iloc[k,4]
    df_avg_sprintz = df_sprintz.groupby(by = df_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_sprintz_df = df_avg_sprintz.shape[0]

    for path_test_ratio in path_test_beta_ratio:
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Encode"] = df_test.iloc[k,3] / df_test.iloc[k,4]    
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            cr = df_avg_test.iloc[i,-1]
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],cr]
            result_count += 1 
    # dir_ratio_pruning_bos = path_pruning_bos_ratio + dir_r[j] + "_ratio.csv"
    # df_pruning_bos = pd.read_csv(dir_ratio_pruning_bos)
    # for k in range(df_pruning_bos.shape[0]):
    #     df_pruning_bos.loc[k,"Encode"] = df_pruning_bos.iloc[k,3] / df_pruning_bos.iloc[k,4]    
    # df_avg_pruning_bos = df_pruning_bos.groupby(by = df_pruning_bos['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_pruning_bos_df = df_avg_pruning_bos.shape[0]

    # dir_ratio_pruning_sprintz = path_pruning_sprintz_ratio + dir_r[j] + "_ratio.csv"
    # df_pruning_sprintz = pd.read_csv(dir_ratio_pruning_sprintz)
    # for k in range(df_pruning_sprintz.shape[0]):
    #     df_pruning_sprintz.loc[k,"Encode"] = df_pruning_sprintz.iloc[k,3] / df_pruning_sprintz.iloc[k,4]    
    # df_avg_pruning_sprintz = df_pruning_sprintz.groupby(by = df_pruning_sprintz['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_pruning_sprintz_df = df_avg_pruning_sprintz.shape[0]

    # dir_ratio_pruning_rle = path_pruning_rle_ratio + dir_r[j] + "_ratio.csv"
    # df_pruning_rle = pd.read_csv(dir_ratio_pruning_rle)
    # for k in range(df_pruning_rle.shape[0]):
    #     df_pruning_rle.loc[k,"Encode"] = df_pruning_rle.iloc[k,3] / df_pruning_rle.iloc[k,4]    
    # df_avg_pruning_rle = df_pruning_rle.groupby(by = df_pruning_rle['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # len_pruning_rle_df = df_avg_pruning_rle.shape[0]

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

    for i in range(len_m_bos_df):
        cr = df_avg_m_bos.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_m_bos.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bos_m_df):
        cr = df_avg_rle_bos_m.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bos_m.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_sprintz_bos_m_df):
        cr = df_avg_sprintz_bos_m.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bos_m.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_bosb_df):
        cr = df_avg_bosb.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_bosb.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_rle_bosb_df):
        cr = df_avg_rle_bosb.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rle_bosb.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_bosb_df):
        cr = df_avg_sprintz_bosb.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz_bosb.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_sprintz_df):
        cr = df_avg_sprintz.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_sprintz.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for path_test_ratio in path_test_beta_ratio:
        dir_ratio_test = path_test_ratio + dir_r[j] + "_ratio.csv"
        df_test = pd.read_csv(dir_ratio_test)
        for k in range(df_test.shape[0]):
            df_test.loc[k,"Decode"] = df_test.iloc[k,3] / df_test.iloc[k,4]    
        df_avg_test = df_test.groupby(by = df_test['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_test_df = df_avg_test.shape[0]

        for i in range(len_test_df):
            cr = df_avg_test.iloc[i,-1]
            df_result.loc[result_count] = [df_avg_test.iloc[i,0],dir_r[j],cr]
            result_count += 1 
    # for i in range(len_pruning_bos_df):
    #     cr = df_avg_pruning_bos.iloc[i,-1]
    #     df_result.loc[result_count] = [df_avg_pruning_bos.iloc[i,0],dir_r[j],cr]
    #     result_count += 1 

    # for i in range(len_pruning_sprintz_df):
    #     cr = df_avg_pruning_sprintz.iloc[i,-1]
    #     df_result.loc[result_count] = [df_avg_pruning_sprintz.iloc[i,0],dir_r[j],cr]
    #     result_count += 1 

    # for i in range(len_pruning_rle_df):
    #     cr = df_avg_pruning_rle.iloc[i,-1]
    #     df_result.loc[result_count] = [df_avg_pruning_rle.iloc[i,0],dir_r[j],cr]
    #     result_count += 1 

# print(df_result)
df_result.to_csv("./compression_ratio/decode_time_improve.csv",index=False)