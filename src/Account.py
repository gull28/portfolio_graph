class Account:
    def __init__(self, account):
        self.blocked = account['blocked']
        self.free = account['free']
        self.invested = account['invested']
        self.pieCash = account['pie_cash']
        self.result = account['result']
        self.total = account['total']
    