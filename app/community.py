import random
from trade import Trade
from rules import Ruleset

class Minion:

    def __init__(self, db):
        self.nouns = ["dog", "cat", "fish", "bird", "toad"]
        self.adjectives = ["happy", "joyius", "angry", "excited"]
        self.verbs = ["run", "jump", "fly", "swim"]
        self.rules = Ruleset()
        self.db = db


    def create_minion(self):

        #self.rules.print_daily_trade_limit()
        # Using predefined lists
        nouns = self.nouns
        adjectives = self.adjectives
        verbs = self.verbs

        random_noun = random.choice(nouns)
        random_adjective = random.choice(adjectives)
        random_verb = random.choice(verbs)
        random_number = random.randint(0, 10000)  # Generating a random number from 0 to 10000

        username = f"{random_adjective}_{random_noun}_{random_number}"
        password = f"{random_verb}_{random_noun}_{random_number}"

        user_id = self.db.add_new_user(username, password)
        #print(user_id)
        self.db.generate_and_store_api_key(user_id)
        self.minion_says_hello(user_id)
        return user_id

    def minion_says_hello(self, user_id):
        print(f"Heyy {self.db.get_username(user_id)} here: Ready to explore! {user_id}")

    def explore(self, user_id):

        print("Found some trees and stones but no sea in sight just yet...")

        # Generate a random number between 0 and 1
        rand_num = random.randint(0, 1)

        if rand_num == 1:
            print(f"I found sea and {self.db.get_username(user_id)} keeps collecting.")
            return 0
        else:
            print(f"{self.db.get_username(user_id)} only found a rubble of ash.")
            return -1
        # Fetch market data, analyze trends, etc.
        # Maybe use self.db and self.rules here

    def attack(self, minion_id):
        trade = Trade(self.db)
        trade_id = trade.create_trade(minion_id)
