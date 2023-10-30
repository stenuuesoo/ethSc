import hashlib
import uuid
import mysql.connector

class DatabaseConnection:
    def __init__(self, host="localhost", port="3306", user="root1", password="root1", database="ethSq_sandbox"):
        #host="host.docker.internal"
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            #print("Connection successful.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            #print("Connection closed.")

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            #print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def fetch_data(self, query, data=None):
        cursor = self.connection.cursor()
        result = None
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def test_database_connection(self):
        self.connect()
        self.disconnect()

    def fetch_binance_keys(self):
        self.connect()
        query = "SELECT name, api_key, api_secret FROM api_keys_table"
        result = self.fetch_data(query)
        self.disconnect()
        if result:
            for row in result:
                if row[0] == 'binance':  # 0 is the index for 'name'
                    return row[1], row[2]  # 1 and 2 are the indices for 'api_key' and 'api_secret'
            print("No Binance API keys found.")
            return None, None
        else:
            print("No API keys found.")
            return None, None

    def save_trade_to_db(self, trade_data):
        """
        Save trade data into the 'trades' table.

        Parameters:
            connection (mysql.connector.connection_cext.CMySQLConnection): The database connection.
            trade_data (dict): A dictionary containing the trade data.

        Returns:
            int: The trade_id of the inserted trade.
        """
        self.connect()
        cursor = self.connection.cursor()

        # SQL query to insert data into the 'trades' table
        sql_query = """
        INSERT INTO trades (trade_id, symbol, entry_price, exit_price, quantity, status, entry_timestamp, exit_timestamp, profit_or_loss, sentiment_score, leverage)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data_to_insert = (
            trade_data.get('trade_id'),  # Include the UUID
            trade_data.get('symbol'),
            trade_data.get('entry_price'),
            trade_data.get('exit_price'),
            trade_data.get('quantity'),
            trade_data.get('status'),
            trade_data.get('entry_timestamp'),
            trade_data.get('exit_timestamp'),
            trade_data.get('profit_or_loss'),
            trade_data.get('sentiment_score'),
            trade_data.get('leverage')
        )

        # Execute the query and commit the transaction
        cursor.execute(sql_query, data_to_insert)
        self.connection.commit()

        # Close the cursor
        cursor.close()
        # Close the database connection
        self.disconnect()
        print("Trade saved to database:", trade_data.get('trade_id'))

    def retrieve_trade_from_db(self, trade_id):

        """
        Retrieve a specific trade record from the 'trades' table using its trade_id.

        Parameters:
            trade_id (str): The UUID of the trade to be retrieved.

        Returns:
            dict: A dictionary containing the trade data, or None if the trade is not found.
        """
        self.connect()
        cursor = self.connection.cursor()
        trade = None

        # SQL query to fetch data from the 'trades' table for a specific trade_id
        sql_query = "SELECT trade_id, symbol, entry_price, exit_price, quantity, status, entry_timestamp, exit_timestamp, profit_or_loss, sentiment_score, leverage FROM trades WHERE trade_id = %s"

        try:
            cursor.execute(sql_query, (trade_id,))
            result = cursor.fetchone()

            if result:
                trade = {
                    'trade_id': result[0],
                    'symbol': result[1],
                    'entry_price': result[2],
                    'exit_price': result[3],
                    'quantity': result[4],
                    'status': result[5],
                    'entry_timestamp': result[6],
                    'exit_timestamp': result[7],
                    'profit_or_loss': result[8],
                    'sentiment_score': result[9],
                    'leverage': result[10]
                }

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()

        print("Trade retrieved from database:", trade.get('trade_id'))
        self.disconnect()

    def add_new_user(self, username, password):
        self.connect()
        user_id = str(uuid.uuid4())
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = "INSERT INTO users (user_id, username, hashed_password) VALUES (%s, %s, %s)"
        self.execute_query(query, (user_id, username, password))
        self.disconnect()
        return user_id



    def generate_and_store_api_key(self, user_id):
        self.connect()
        # Generate a unique API key
        api_key = str(uuid.uuid4())

        # Hash the API key
        hashed_api_key = hashlib.sha256(api_key.encode()).hexdigest()

        # Store hashed API key in the database
        query = "UPDATE users SET api_key = %s WHERE user_id = %s"
        self.execute_query(query, (hashed_api_key, user_id))
        self.disconnect()
        # Return the original (non-hashed) API key to the user
        return api_key

    def get_username(self, user_id):
        self.connect()
        cursor = self.connection.cursor()
        username = None

        # Correct the SQL query and parameter placeholder
        query = "SELECT username FROM users WHERE user_id = %s"

        try:
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()  # Fetch the first row

            if result:
                username = result[0]  # Get the first column (username) from the first row
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()
            self.disconnect()

        return username

