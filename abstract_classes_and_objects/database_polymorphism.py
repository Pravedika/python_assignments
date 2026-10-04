from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL.")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL.")

class SQLiteDatabase(Database):
    def connect(self):
        print("Connected to SQLite.")

databases = [MySQLDatabase(), PostgreSQLDatabase(), SQLiteDatabase()]

for database in databases:
    database.connect()
