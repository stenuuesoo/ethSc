class Ruleset:
    def __init__(self):
        self._rules = {'active_trade_limit': 1, 'daily_trade_limit': 1, 'trade_time_window': "09:30-16:00",
                       'min_trade_size': 0.01, 'max_open_loss': -0.02}

    @property
    def active_trade_limit(self):
        return self._rules['active_trade_limit']

    @property
    def daily_trade_limit(self):
        return self._rules['daily_trade_limit']

    @property
    def trade_time_window(self):
        return self._rules['trade_time_window']

    @property
    def min_trade_size(self):
        return self._rules['min_trade_size']

    @property
    def max_open_loss(self):
        return self._rules['min_trade_size']

    def print_rules(self):
        print(self._rules)

    def print_active_trade_limit(self):
        print(f"Active Trade Limit: {self.active_trade_limit}")

    def print_daily_trade_limit(self):
        print(f"Daily Trade Limit: {self.daily_trade_limit}")

    def print_trade_time_window(self):
        print(f"Trade Time Window: {self.trade_time_window}")

    def print_min_trade_size(self):
        print(f"Minimum Trade Size: {self.min_trade_size}")

    def print_max_open_loss(self):
        print(f"Maximum Open Loss: {self.max_open_loss}")
