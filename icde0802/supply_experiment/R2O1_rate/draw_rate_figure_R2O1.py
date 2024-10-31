import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Font and style settings
fontsize = 11
matplotlib.rcParams.update({
    'font.size': fontsize,
    'axes.labelsize': fontsize,
    'axes.titlesize': fontsize,
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'legend.fontsize': fontsize
})

# Paths to data
df = pd.read_csv("./rate.csv")
# dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"]

dir_r = ["EPM-Education","Metro-Traffic","Vehicle-Charge","CS-Sensors","TH-Climate","TY-Transport","YZ-Electricity","GW-Magnetic","USGS-Earthquakes","Cyber-Vehicle","TY-Fuel",'Nifty-Stocks']

# df = df.drop(columns=['Dataset'])

# Calculate averages by label
# df = df.groupby('Encoding').mean().reset_index()


# Create a new DataFrame for easier plotting
# original_encodings = [ 'BOS-B','BOS-M']
# improved_encodings = [ 'BOS-B-Improve','BOS-M-Improve']

df['Lower'] = df['Lower'] * 100
df['Upper'] = df['Upper'] * 100


plot_data = {
    'Label': dir_r,
    'Lower Outliers': df[df['Dataset'].isin(dir_r)].set_index('Dataset').loc[dir_r, 'Lower'].values,
    'Upper Outliers': df[df['Dataset'].isin(dir_r)].set_index('Dataset').loc[dir_r, 'Upper'].values,
}
plot_df = pd.DataFrame(plot_data)

# Plotting
fig, axs = plt.subplots(1,1,figsize=(6, 2))
colors = ['#ff7f00', '#e31a1c', "#1178b4"]

# Plot bars for comparison
plot_df.plot.bar(x='Label', y=['Lower Outliers', 'Upper Outliers'], ax=axs, color=colors[:2], alpha=0.7)
# axs[0].set_title('(a) Compression Time')
axs.set_ylabel('Percentage (%)')
axs.set_xlabel('Dataset')
axs.set_xticklabels(axs.get_xticklabels(), rotation=30, ha="right")

# Remove legend from ax to create a unified one later
axs.get_legend().remove()

# plot_df.plot.bar(x='Label', y=['Improved Ratio', 'Improved Ratio'], ax=axs[1], color=colors[:2], alpha=0.7)
# axs[1].set_title('(b) Compression Ratio')
# axs[1].set_ylabel('Compression Ratio')
# axs[1].set_xlabel('Compression')
# axs[1].set_xticklabels(axs[0].get_xticklabels(), rotation=00, ha="center")

# # Remove legend from ax to create a unified one later
# axs[1].get_legend().remove()

lines, labels = axs.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 1.1), loc='upper center', fontsize=fontsize, labelspacing=0.2, handletextpad=0.2, columnspacing=0.8, ncol=2)

# Save the figure
fig.savefig("./fig/rate_outlier.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./fig/rate_outlier.png", dpi=400, bbox_inches='tight')

