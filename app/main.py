from forgemaster import Forgemaster
from db import DatabaseConnection
from rules import Ruleset
from binance import Binance

if __name__ == "__main__":

    db = DatabaseConnection()
    rules = Ruleset()
    db.connect()
    api_key, api_secret = db.fetch_binance_keys()
    db.disconnect()

    if api_key and api_secret:
        binance = Binance(api_key, api_secret)
        forgemaster = Forgemaster(db, rules, binance)
        forgemaster.alchemy()
    else:
        print("Could not initialize Forgemaster due to missing Binance keys.")
