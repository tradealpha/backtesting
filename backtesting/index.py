def backtest(training_period, shape, params):
    """
        - training_period: rows that are ignored because they are used as training
        - shape: dataframe shape (used to calculate the size of the output array)
        - params: different input params

        returns: an array with information about the signal
    """
    out_size = shape[0] - training_period

    # init array for output
    # col 1: position: 0: out, 1: long and (-1: short)
    out = np.zeros(( out_size, 2))

    buy_level = float("nan")

    rsi_threshold = params['rsi_threshold']
    exitposition_threshold = params['exitposition_threshold']
    riskRewardRatio = params['riskRewardRatio']

    exitposition_threshold_gain = 1 + exitposition_threshold
    exitposition_threshold_loss = 1 - exitposition_threshold*riskRewardRatio

    # go through step by step
    for index, row in df.iterrows():
        i = index - training_period

        if (i < 0):
            continue

        # get previous position value
        prev = out[i-1,0] if i > 0 else 0
        # get signal
        # psignal = 1 if row['ema2'] > row['ema1'] else 0
        psignal = 1 if row['rsi'] < rsi_threshold else 0

        if prev == 1: # and psignal == 0:
            if row['close']> exitposition_threshold_gain*buy_level or row['close'] < exitposition_threshold_loss*buy_level:
                signal = 0
                buy_level = float("nan")

        else:
            signal = psignal

        if signal == 1:
            buy_level = row['close']

        # end of signal creation, putting all together
        
        # get pnl
        pnl = signal * row['rdiff']

        out[i,0] = signal
        out[i,1] = 0

    # take signal out
    # and remove last data, we predict for a data point that we don't have
    ## first index: all but last entry,
    ## second index: first array dimension (the signal)
    s = out[:-1,0]  
    return s