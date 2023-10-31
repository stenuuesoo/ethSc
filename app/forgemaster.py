from community import Minion
from trade import Trade


class Forgemaster:
    def __init__(self, db, rules, binance):
        self.db = db
        self.rules = rules
        self.binance = binance

    def alchemy(self):

        self.rules.print_daily_trade_limit()
        self.binance.print_eth_balance()

        minion = Minion(self.db)
        minion_id = minion.create_minion()

        trade = Trade(self.db)
        trade_id = trade.create_trade(minion_id)





