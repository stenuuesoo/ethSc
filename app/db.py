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
            print("Connection successful.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
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
        query = "SELECT name, api_key, api_secret FROM api_keys_table"
        result = self.fetch_data(query)
        if result:
            for row in result:
                if row[0] == 'binance':  # 0 is the index for 'name'
                    return row[1], row[2]  # 1 and 2 are the indices for 'api_key' and 'api_secret'
            print("No Binance API keys found.")
            return None, None
        else:
            print("No API keys found.")
            return None, None