from forgemaster import Forgemaster
from db import DatabaseConnection
from binance import Binance
import asyncio


async def main():
    db = DatabaseConnection()
    api_key, api_secret = db.fetch_binance_keys()

    if api_key and api_secret:
        binance = Binance(api_key, api_secret)
        forgemaster = Forgemaster(db, binance)
        await forgemaster.alchemy()  # Note the 'await' here
    else:
        print("Could not initialize Forgemaster due to missing Binance keys.")

if __name__ == "__main__":
    asyncio.run(main())  # This will run the 'main' coroutine and manage the event loop
