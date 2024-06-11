from pathlib import Path
from database import PostgresConnection, DataInserter, Procedures
import logging
import csv

logger = logging.getLogger(__name__)

CURRENT_PATH = Path(__file__).parent

logging.basicConfig(level=logging.INFO)

def main() -> None:
    # pega todos os CSV's do diretório atual, e depois pega o último csv
    logger.info('Searching latest .csv...')

    files = [file for file in CURRENT_PATH.iterdir() if str(file).endswith('.csv') and 'ficha' in str(file).lower()]
    
    latest_csv = max(files, key=lambda file: file.stat().st_mtime)
    
    logger.info(f'Latest CSV found: {latest_csv.name}')

    logger.info('Connecting to database...')
    with PostgresConnection('.env') as connection:

        logger.info('Importing data...')
        with open(latest_csv, 'r', encoding='utf-8') as file:
            file_as_csv = csv.reader(file, delimiter=';')
            [next(file_as_csv) for _ in range(3)]  # pula as 3 primeiras linhas

            inserter = DataInserter(connection)

            for row in file_as_csv:
                inserter.insert_with_procedure(
                    Procedures.INSERT_FICHA,
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8][0], row[9], row[10], row[11], row[12]
                )

            connection.commit()

            connection.execute('CALL refresh_views()')

    logger.info('Data import finished with sucess!')


if __name__ == '__main__':
    main()
