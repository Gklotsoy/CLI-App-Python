import psycopg2


class Dbh:

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.db_config = {
            "dbname": "tls_employee",
            "user": "postgres",
            "password": "pass123",
            "host": "localhost",
            "port": "5432"
        }

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_config)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print("Error while connecting to PostgreSQL", e)

    def disconnect(self):
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # def fetch(self):
    #     return self.cursor.fetchall()
    #
    # def fetch_one(self):
    #     return self.cursor.fetchone()
