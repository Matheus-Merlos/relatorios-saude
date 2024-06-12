from pathlib import Path
from database import Procedures
from insert import import_data

ROOT = Path(__file__).parent


def main() -> None:
    import_data('ficha', Procedures.INSERT_FICHA, '.env')


if __name__ == '__main__':
    main()
