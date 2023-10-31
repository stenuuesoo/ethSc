import uuid


class Trade:
    def __init__(self, db):
        self.db = db

    def create_trade(self, minion_id):
        self.sample_trade = {
            'trade_id': str(uuid.uuid4()),  # Generate a unique UUID
            'minion_id': minion_id,
            'symbol': 'ETH/USD',
            'entry_price': 2000.00,
            'exit_price': 2100,
            'quantity': 1.0,
            'status': 'OPEN',
            'entry_timestamp': None,
            'exit_timestamp': None,
            'profit_or_loss': 100,
            'sentiment_score': 0.75,
            'leverage': 2.0
        }
        self.db.save_trade_to_db(self.sample_trade)
        self.db.retrieve_trade_from_db(self.sample_trade['trade_id'])
