class Forgemaster:
    def __init__(self, db, rules, binance):
        self.db = db
        self.rules = rules
        self.binance = binance

    def alchemy(self):
        self.rules.print_daily_trade_limit()
        self.binance.print_eth_balance()
