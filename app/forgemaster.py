from community import GoldenMinion
from trade import Trade

class Forgemaster:
    def __init__(self, db, rules, binance):
        self.db = db
        self.rules = rules
        self.binance = binance


    def alchemy(self):

        self.rules.print_daily_trade_limit()
        self.binance.print_eth_balance()

        new_minion = GoldenMinion(self.db)
        minion_id = new_minion.community()
        new_minion.minion_says_hello(minion_id)

        new_trade = Trade()
        self.db.save_trade_to_db(new_trade.sample_trade)
        self.db.retrieve_trade_from_db(new_trade.sample_trade['trade_id'])






