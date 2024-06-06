from pathlib import Path
from database import PostgresConnection
import csv


if __name__ == '__main__':
    # pega todos os CSV's do diretório atual, e depois pega o último csv
    files = [file for file in Path(__file__).parent.iterdir(
    ) if file.is_file() and str(file).endswith('.csv')]
    latest_csv = max(files, key=lambda file: file.stat().st_mtime)

    with PostgresConnection('.env') as connection:

        with open(latest_csv, 'r', encoding='utf-8') as file:
            file_as_csv = csv.reader(file, delimiter=';')
            [next(file_as_csv) for _ in range(3)]  # pula as 3 primeiras linhas

            for row in file_as_csv:
                connection.execute(f"""CALL insert_ficha(
                                {row[0]},
                                '{row[1]}',
                                '{row[2]}',
                                '{row[3]}',
                                '{row[4]}',
                                '{row[5]}',
                                {row[6]},
                                '{row[7]}',
                                '{row[8][0]}',
                                {row[9]},
                                '{row[10]}',
                                '{row[11]}',
                                '{row[12]}');"""
                )

            connection.commit()

            connection.execute('CALL refresh_views()')

    print('Importação de dados concluída com sucesso!')
