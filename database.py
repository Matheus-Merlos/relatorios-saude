import psycopg2
from dotenv import load_dotenv
from os import getenv


class PostgresConnection:
    def __init__(self, dotenv_path: str) -> None:
        load_dotenv(dotenv_path)
        self.__host: str | None = getenv('HOST')
        self.__database: str | None = getenv('DATABASE')
        self.__user: str | None = getenv('USER')
        self.__password: str | None = getenv('PASSWORD')
        self.__port: str | None = getenv('PORT')

        if self.__port is None:
            self.__port = '5432'

        self.__credentials = {
            'host': self.__host,
            'database': self.__database,
            'user': self.__user,
            'password': self.__password,
            'port': self.__port
        }

    def __enter__(self):
        self.__connection = psycopg2.connect(**self.__credentials)
        self.__cursor = self.__connection.cursor()

        return self

    def __exit__(self, class_exception, exception_, traceback_):
        self.__connection.commit()
        self.__cursor.close()
        self.__connection.close()

        if class_exception is not None:
            raise class_exception(*exception_.args).with_traceback(traceback_)

        return True

    def execute(self, sql_command: str) -> None:
        self.__cursor.execute(sql_command)

    def commit(self) -> None:
        self.__connection.commit()
