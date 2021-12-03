import index as b

s = b.backtest(training_period, shape, 30, .01)
stratReturns = s*rdiff 
strat = priceFromReturns(stratReturns)
plt.plot(strat)
plt.plot(cdiff, 'r')
plt.legend(['sd', 'nbuy and hold'])
sharpeRatio(stratReturns)