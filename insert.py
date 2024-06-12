import logging
from typing import Callable
from pathlib import Path
import os
from database import Procedures, PostgresConnection, DataInserter
import csv

ROOT: Path = Path(__file__).parent

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def search_latest_csv(filter_func: Callable[[Path | str], bool]) -> Path:
    logger.info('Searching latest CSV...')
    files: list[Path] = [file for file in ROOT.iterdir() if file.is_file()]

    latest_filtered_csv: Path = max(
        filter(filter_func, files),
        key=lambda file:
            file.stat().st_mtime
    )
    logger.info(f'Latest csv found: {latest_filtered_csv.name}')
    return latest_filtered_csv


def import_data(file_name_filter: str, procedure_insert: Procedures, dotenv_filename: str = '.env', refresh_procedure: str | None = None) -> None:
    latest_file = search_latest_csv(
        lambda filename:
            file_name_filter in str(filename).lower()
    )

    with open(latest_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for _ in range(3):
            next(csv_reader)

        data = [line for line in csv_reader]

    logger.info('Connecting to database....')
    with PostgresConnection(dotenv_filename) as connection:
        inserter = DataInserter(connection)
        logger.info('Importing data')
        assert data
        for line in data:
            inserter.insert_with_procedure(procedure_insert, *line)

        if refresh_procedure:
            logger.info('Refreshing views')
            connection.execute(f'CALL {refresh_procedure};')

    logger.info('Data import finished with sucess!')
