import logging
from typing import Callable
from pathlib import Path
import os
from database import Procedures, PostgresConnection, DataInserter
import csv

ROOT = Path(__file__).parent

def search_latest_csv(filter_func: Callable) -> Path:
    files: list = [file for file in ROOT.iterdir() if file.is_file()]
        
    latest_filtered_csv = max(filter(filter_func, files), key=lambda file: file.stat().st_mtime)
    return latest_filtered_csv
    

class DataImporter:
    def __init__(self, file_name_filter: str, procedure_insert: Procedures, dotenv_filename: str, refresh_procedure: str | None=None) -> None:
        self.__file_name_filter = file_name_filter
        self.__procedure = procedure_insert
        self.__dotenv = dotenv_filename
        self.__refresh_procedure = refresh_procedure
        
        self.__latest_file = search_latest_csv(lambda filename: self.__file_name_filter in str(filename).lower())
        self.__data: None | list = None
        
        self.read_csv()
        self.insert_data()
        
    def read_csv(self):
        with open(self.__latest_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            [next(csv_reader) for _ in range(3)]
            data = [line for line in csv_reader]
            self.__data = data
        
    def insert_data(self):
        with PostgresConnection(self.__dotenv) as connection:
            inserter = DataInserter(connection)
            assert self.__data
            for line in self.__data:
                inserter.insert_with_procedure(self.__procedure, *line)
            
            if self.__refresh_procedure:
                connection.execute(f'CALL {self.__procedure};')
            
    
            
            
            