import os

import ccxt
import json


class Binance:
    def __init__(self, api_key, api_secret):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret,
            'options': {'defaultType': 'spot'},
            'enableRateLimit': True
        })
        self.exchange.set_sandbox_mode(True)

    def fetch_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)

    def fetch_balance(self):
        return self.exchange.fetch_balance()

    def print_balance(self):
        print(self.exchange.fetch_balance())

    def print_eth_balance(self):
        balance_info = self.exchange.fetch_balance()
        eth_balance = balance_info['info']['balances']

        for asset_info in eth_balance:
            if asset_info['asset'] == 'ETH':
                print(f"Free ETH: {asset_info['free']}")
                print(f"Locked ETH: {asset_info['locked']}")
                break

