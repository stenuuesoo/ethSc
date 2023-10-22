import uuid


class Trade:
    def __init__(self):
        self.sample_trade = {
            'trade_id': str(uuid.uuid4()),  # Generate a unique UUID
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