# NAV
# take signal starting after training period + 1 (!) to account for training period
rdiff = df.iloc[training_period+1:]['rdiff']
cdiff = priceFromReturns(rdiff) 
sharpeCum = sharpeRatio(rdiff)

#print('{} and {}'.format(sharpeCum, sharpeStrat))
print('{} and {}'.format(len(rdiff), sharpeStrat))