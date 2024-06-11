class Position:
    def __init__(self, position):
        self.averagePrice = position['averagePrice']
        self.currentPrice = position['currentPrice']
        self.fillDate = position['initialFillDate']
        self.maxBuyPrice = position['maxBuy']
        self.maxSellPrice = position['maxSell']
        self.pieQuant = position['pieQuantity']
        self.quant = position['quantity']
        self.ticker = position['ticker']

    def getChange(self):
        return self.currentPrice - self.averagePrice