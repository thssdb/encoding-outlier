import numpy as np
import pandas as pd

std_devs = [100,1000,10000,100000,1000000]

n = 10240
for scale in std_devs:
    data = np.random.exponential(scale, n)

    data = data + (scale*(3-np.log(2)))
    int_data = np.round(data).astype(int)
    clipped_data = np.clip(int_data, 1, scale*6)



    df = pd.DataFrame({
        'Time': range(n), 
        'Value': int_data 
    })


    csv_path = '/Users/zihanguo/Downloads/R/outlier/outliier_code/encoding-outlier/trans_data/Synthetic_Exp_'+ str(scale) +'/data.csv' 
    df.to_csv(csv_path, index=False) 

    print(f"Data has been saved to {csv_path}")

for std_dev in std_devs:

    data = np.random.normal(3*std_dev, std_dev, n)
    int_data = np.round(data).astype(int)
    clipped_data = np.clip(int_data, 1, 6*std_dev)

    df = pd.DataFrame({
        'Time': range(n),  
        'Value': int_data 
    })


    csv_path = '/Users/zihanguo/Downloads/R/outlier/outliier_code/encoding-outlier/trans_data/Synthetic_Normal_'+ str(std_dev) +'/data.csv'  
    df.to_csv(csv_path, index=False)  

    print(f"Data has been saved to {csv_path}")
