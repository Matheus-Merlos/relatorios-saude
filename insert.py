import logging
from typing import Callable
from pathlib import Path
import os
from database import Procedures

ROOT = Path(__file__).parent

def search_latest_csv(filter_func: Callable) -> Path:
    files: list = [file for file in ROOT.iterdir() if file.is_file()]
    
    latest_filtered_csv: list = list(filter(filter_func, files))
    return latest_filtered_csv[0]
    

class DataImporter:
    def __init__(self, file_name_filter: str, procedure_insert: Procedures) -> None:
        self.__file_name_filter = file_name_filter
        self.__procedure_insert = procedure_insert
        
        self.__latest_file = search_latest_csv(lambda filename: filename.endswith('.csv'))
        
    def read_csv(self)