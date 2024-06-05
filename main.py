from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import psycopg2
import csv
import os


if __name__ == '__main__':
    # pega todos os CSV's do diretório atual, e depois pega o último csv
    files = [file for file in Path(__file__).parent.iterdir(
    ) if file.is_file() and str(file).endswith('.csv')]
    latest_csv = max(files, key=lambda file: file.stat().st_mtime)

    load_dotenv()

    credentials = {
        'user': os.getenv('USER'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'database': os.getenv('DATABASE')
    }
    with open(latest_csv, 'r', encoding='utf-8') as file:
        file_as_csv = csv.reader(file, delimiter=';')
        [next(file_as_csv) for _ in range(3)]  # pula as 3 primeiras linhas

        connection = psycopg2.connect(**credentials)
        cursor = connection.cursor()

        for row in file_as_csv:
            try:
                cursor.execute(f"""CALL insert_ficha(
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
            except (psycopg2.errors.UniqueViolation, psycopg2.errors.InFailedSqlTransaction):
                print(f"""Ficha com o id {
                      row[6]}/{row[9]} já existe no sistema, skippando""")
                continue

        connection.commit()

        cursor.execute("CALL refresh_views()")

        connection.commit()
        cursor.close()
        connection.close()

    print('Importação de dados concluída com sucesso!')
