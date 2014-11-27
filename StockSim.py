# Automated Stock Market Trading Simulator
# http://code.activestate.com/recipes/578881-automated-stock-market-trading-simulation/?in=lang-python
import random

initialMoneyOwned = 1000.0
initalStockOwned = 0.1
initialStockPrice = 1000.0
tradingDays = 1000
tp = 5.0 #buy/sell percentage threshold of the investor
maxVolatilityPercent = 5.0 # of the stock
numTrails = 1000

initialInvestment = initialMoneyOwned + initalStockOwned * initialStockPrice

def SimulateTrading(moneyOwned, stockOwned, stockPrice, days):
    stockBuySellPrice = stockPrice
    
    for day in range(days):
        volatility = random.random () * stockPrice * maxVolatilityPercent / 100.0
        stockPrice += (random.random() * 2.0 - 1.0) * volatility
        
        #trading
        if stockOwned > 0.0:
            if stockPrice >= stockBuySellPrice * (100.0 + tp) / 100.0:
                #sell
                moneyOwned += stockOwned * stockPrice
                stockOwned = 0.0
                stockBuySellPrice = stockPrice
                
            if moneyOwned > 0.0:
                if stockPrice <= stockBuySellPrice * (100.0 - tp) / 100.0:
                    #buy
                    stockOwned += moneyOwned / stockPrice
                    moneyOwned = 0.0
                    stockBuySellPrice = stockPrice

    return (moneyOwned, stockOwned, stockPrice)
 
numWins = 0
numLosses = 0
totalWins = 0.0
totalLosses = 0.0
for i in range(numTrails):
    (moneyOwned, stockOwned, stockPrice) = \
    SimulateTrading(initialMoneyOwned, initalStockOwned, initialStockPrice, tradingDays)
    
    finalReturn = moneyOwned + stockOwned * stockPrice - initialInvestment
    
    if finalReturn > 0.0:
        numWins += 1
        totalWins += finalReturn
    elif finalReturn < 0.0:
        numLosses += 1
        totalLosses += finalReturn
        
print "Inital Investment  = " + str(initialInvestment)
print "Trading Days       = " + str(tradingDays)
print "Number of Trials   = " + str(numTrails)
print "Number of Wins     = " + str(numWins)
print "Average Win Amount = " + str(totalWins / numWins)
print "Number of Losses   = " + str(numLosses)
print "Average Loss Amount= " + str (abs(totalLosses / numLosses))
