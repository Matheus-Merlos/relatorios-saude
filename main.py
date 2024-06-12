from pathlib import Path
from database import PostgresConnection, DataInserter, Procedures
from insert import DataImporter
import logging
import csv

logger = logging.getLogger(__name__)

ROOT = Path(__file__).parent

logging.basicConfig(level=logging.INFO)

def main() -> None:
    ficha_de_atendimento = DataImporter('ficha', Procedures.INSERT_FICHA, '.env')

if __name__ == '__main__':
    main()
