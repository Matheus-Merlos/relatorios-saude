from pony.orm import db_session, select, core, set_sql_debug
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from models import db
import models
import utils
import csv
import os


def converter_data(data):
    return datetime.strptime(data, "%d/%m/%Y").date()


def converter_horario(horario):
    return datetime.strptime(horario, "%H:%M:%S").time()


def converter_time(time):
    return datetime.strptime(time, "%d/%m/%Y %H:%M:%S").time()


if __name__ == '__main__':
    # pega todos os CSV's do diretório atual, e depois pega o último csv
    files = [file for file in Path(__file__).parent.iterdir(
    ) if file.is_file() and str(file).endswith('.csv')]
    latest_csv = max(files, key=lambda file: file.stat().st_mtime)

    utils.connect_to_database()

    with open(latest_csv, 'r', encoding='utf-8') as file:
        file_as_csv = csv.reader(file, delimiter=';')
        [next(file_as_csv) for _ in range(3)]  # pula as 3 primeiras linhas

        for row in file_as_csv:
            ficha_de_atendimento = {
                'id': f'{str(row[6])}/{str(row[9])}',
                'unidadeid': row[0],
                'unidade': row[1],
                'profissional': row[2],
                'especialidade': row[3],
                'motivo_consulta': row[4],
                'data_consulta': converter_data(row[5]),
                'data_nascimento': converter_data(row[7]),
                'sexo': row[8][0],
                'horario': converter_horario(row[10]),
                'hora_aten1': converter_time(row[11]) if row[11] else None,
                'hora_aten2': converter_time(row[12]) if row[12] else None
            }

            try:
                with db_session:
                    models.FichaDeAtendimento(**ficha_de_atendimento)
            except core.TransactionIntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    print(f'Ficha de atendimento {
                          ficha_de_atendimento["id"]} já existe na base de dados, skippando')
                continue

    print('Importação de dados concluída com sucesso!')
