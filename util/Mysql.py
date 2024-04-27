import mysql.connector


class Mysql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                print("Connected to the database")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")
            self.connection = None

    def execute_query(self, query, params=None):
        if not self.connection:
            print("Not connected to the database")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()


def getDb():
    return Mysql("localhost", "root", "Lx284190056", "tju")


def query(sql):
    db = getDb()
    db.connect()
    result = db.execute_query(sql)
    db.disconnect()
    return result
