from pathlib import Path
from database import Procedures
from insert import import_data


def main() -> None:
    import_data('ficha', Procedures.INSERT_FICHA)


if __name__ == '__main__':
    main()
