import random


class GoldenMinion:

    def __init__(self, db):
        self.nouns = ["dog", "cat", "fish", "bird"]
        self.adjectives = ["happy", "sad", "angry", "excited"]
        self.verbs = ["run", "jump", "fly", "swim"]

        self.db = db

    def community(self):
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

        self.db.generate_and_store_api_key(user_id)

        return user_id

    def minion_says_hello(self, user_id):
        print(f"Say hello, {self.db.get_username(user_id)}. Heyyy!")
