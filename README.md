# BOS: Bit-packing with Outlier Separation

In our paper **BOS: Bit-packing with Outlier Separation**, we show some examples and performance about BOS.

To enable reproductivity, we share all datasets, algorithms and codes in the repository of encoding-outlier, and this readme guides will help you reproduce the results of the experiment and figures in the paper.

## 1. Directory Structure

    ├── README.md           // Help Document
    
    ├── icde0802             // Codes and datasets
    
    │   ├── compression_ratio       // Results of the experiments
    
    │   ├── figs      // Figures of the experiments

    │   ├── supply_experiment // Codes and results of the supply experiments
    
    │       ├── R1O2_block_size_time       // Codes and results of R1O2
    
    │       ├── R1O2_bos_b_improve       // Codes and results of R1O2

    │       ├── R1O4_decode_time       // Codes and results of R1O4

    |       ├── R2O1_rate         // Codes and results of R2O1

    |       ├── R2O2_query_processing         // Codes and results of R2O2

    |       ├── R2O3_lower_outlier_compare        // Codes and results of R2O3
    
    │       └── R3O4_vary_part    // Codes and results of R3O4
    
    │   └── other .py       // codes of drawing results

    ├── trans_data   // datasets


## 2. Environment Requirement

- IoTDB: download from branch [GitHub - apache/iotdb at research/encoding-outlier](https://github.com/apache/iotdb/tree/research/encoding-outlier)
- python: 3.8+
- modules needed: seaborn 0.11.1+, numpy, pandas

## 3. Code Execution

- Get results of compression ratio and time

```
java  xxx.java
```

- The algorithm corresponding to the java code is as follows

| algorithms                         | java code                                                                        |
| ---------------------------------- |----------------------------------------------------------------------------------|
| TSDIFF+BOS-V        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\TSDIFFBOSVImproveDecodeTest.java    |
| TSDIFF+BOS-B        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\TSDIFFBOSBImproveTest.java          |
| TSDIFF+BOS-M        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\TSDIFFBOSMImproveTest.java          |
| SPRINTZ+BOS-V        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\SPRINTZBOSVTest.java               |
| SPRINTZ+BOS-B        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\SPRINTZOSBTest.java                |
| SPRINTZ+BOS-M        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\SPRINTZBOSMTest.java               |
| RLE+BOS-V        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RLEBOSVTest.java                       |
| RLE+BOS-B        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RLEBOSBImproveTest.java                |
| RLE+BOS-M        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RLEBOSMTest.java                       |

- Get figures about xxx.py

```
python xxx.py
```

- The figures corresponding to the python code are as follows

| Figures   | python code                                                                     |
| --------- | -----------------------------------------------------------------------------   |
| Figure 8  | icde0802/draw_data.py                                                           |
| Figure 9  | icde0802/supply_experiment/R2O1_rate/draw_rate_figure_R2O1.py                   |
| Figure 10a| icde0802/table_ratio.py                                                         |
| Figure 10b| icde0802/draw_cr_vs_time.py                                                     |
| Figure 10c| icde0802/table_time.py                                                          |
| Figure 11 | icde0802/supply_experiment/R2O2_query_processing/new_compare_query_time_R2O2.py       |
| Figure 12 | icde0802/supply_experiment/R2O3_lower_outlier_compare/new_compare_figure_R2O3.py      |
| Figure 13 | icde0802/supply_experiment/R3O1_compare_compression/new_draw_figures_compres_R3O2.py  |
| Figure 14 | icde0802/supply_experiment/R3O4_vary_part/new_vary_part_figure_R3O4.py                |
| Figure 15 | icde0802/supply_experiment/R1O2_block_size_time/new_draw_block_size_time.py           |


- 
