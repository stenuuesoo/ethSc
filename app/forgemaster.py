from community import Minion
import time
import logging
import asyncio

#logging.basicConfig(level=logging.INFO)


class Forgemaster:
    def __init__(self, db, binance):
        self.db = db
        self.binance = binance
        self.max_active_minions = 10
        self.current_recruitment = 0

    async def alchemy(self):
        tasks = []
        while True:
            if self.current_recruitment < self.max_active_minions:
                self.current_recruitment += 1
                minion = Minion(self.db)
                minion_id = minion.create_minion()
                task = asyncio.ensure_future(self.manage_minion(minion, minion_id))
                tasks.append(task)
            await asyncio.sleep(5)  # Sleep for 1 second

    async def manage_minion(self, minion, minion_id):
        while True:
            achievement = minion.explore(minion_id)
            if achievement < 0:
                self.current_recruitment -= 1
                print(f"{self.db.get_username(minion_id)} tucks in for the rainy night and tries again tommorrow...")
                break  # Stop this minion from exploring
            await asyncio.sleep(5)  # Sleep for 1 second








