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
df = pd.read_csv("./compression_ratio/decode_time.csv")


df = df.drop(columns=['Dataset'])

# Calculate averages by label
df = df.groupby('Encoding').mean().reset_index()


# Create a new DataFrame for easier plotting
original_encodings = ['BOS-V', 'BOS-B', 'BOS-M']
improved_encodings = ['BOS-V-Improve', 'BOS-B-Improve', 'BOS-M-Improve']

plot_data = {
    'Label': original_encodings,
    'Original': df[df['Encoding'].isin(original_encodings)].set_index('Encoding').loc[original_encodings, 'Decode Time'].values,
    'Improved': df[df['Encoding'].isin(improved_encodings)].set_index('Encoding').loc[improved_encodings, 'Decode Time'].values,
    'Original Ratio': df[df['Encoding'].isin(original_encodings)].set_index('Encoding').loc[original_encodings, 'Ratio'].values,
    'Improved Ratio': df[df['Encoding'].isin(improved_encodings)].set_index('Encoding').loc[improved_encodings, 'Ratio'].values

}
plot_df = pd.DataFrame(plot_data)

# Plotting
fig, axs = plt.subplots(1,2,figsize=(6, 2))
colors = ['#ff7f00', '#e31a1c', "#1178b4"]

# Plot bars for comparison
plot_df.plot.bar(x='Label', y=['Original', 'Improved'], ax=axs[0], color=colors[:2], alpha=0.7)
axs[0].set_title('(a) Decompression Time')
axs[0].set_ylabel('Decompression Time (ns/point)')
axs[0].set_xlabel('Compression')
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=00, ha="center")

# Remove legend from ax to create a unified one later
axs[0].get_legend().remove()

plot_df.plot.bar(x='Label', y=['Original Ratio', 'Improved Ratio'], ax=axs[1], color=colors[:2], alpha=0.7)
axs[1].set_title('(b) Compression Ratio')
axs[1].set_ylabel('Compression Ratio')
axs[1].set_xlabel('Compression')
axs[1].set_xticklabels(axs[0].get_xticklabels(), rotation=00, ha="center")

# Remove legend from ax to create a unified one later
axs[1].get_legend().remove()

lines, labels = axs[0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 1.16), loc='upper center', fontsize=fontsize, labelspacing=0.2, handletextpad=0.2, columnspacing=0.8, ncol=2)

# Save the figure
fig.savefig("./fig/decode_time_comparison.eps", format='eps', dpi=400, bbox_inches='tight')
fig.savefig("./fig/decode_time_comparison.png", dpi=400, bbox_inches='tight')

