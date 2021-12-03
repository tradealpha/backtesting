ra = range(30, 45)
exitposition_thresholds = [.005, .01, .015, .02, .025,.03]
rrr = [3/4, 2/3, 1/2, 1/3, 1/4]
heatmap_data = np.zeros((len(rrr),  len(exitposition_thresholds), len(ra)))
#heatmap_data = np.zeros((len(rrr), len(exitposition_thresholds)))

print(heatmap_data.shape)

#rsi_threshold=36
#riskRewardRatio = 1/2


for idx, riskRewardRatio in enumerate(rrr):
    for idx2, exitposition_threshold in enumerate(exitposition_thresholds):
        for idx3, rsi_threshold in enumerate(ra):
            s = backtest(training_period, shape, rsi_threshold, exitposition_threshold, riskRewardRatio)
            stratReturns = s*rdiff 
            sharpeStrat = sharpeRatio(stratReturns)
            heatmap_data[idx, idx2, idx3] = sharpeStrat

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

ax = sns.heatmap(heatmap_data[:,:,0], linewidth=0.5, xticklabels=exitposition_thresholds, yticklabels=ra)
plt.show()