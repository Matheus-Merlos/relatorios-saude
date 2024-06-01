from pony.orm import select, db_session
from dotenv import load_dotenv
from utils import save_to_file
from typing import Callable
from typing import Any
from models import db
import models
import os

def save_to_csv(query: Any, file_name: str) -> None:
    csv_as_str = ''
    for line in query:
        string = ','.join(str(element) for element in line)
        string += '\n'
        csv_as_str += string
        
    with open(f'output/{file_name}.csv', 'w', encoding='utf-8') as file:
        file.write(csv_as_str)
        
    

if __name__ == '__main__':
    load_dotenv()
    
    credentials = {
        'user': os.getenv('USER'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'database': os.getenv('DATABASE')
    }
    if None in credentials.values():
        raise KeyError('Não foram encontradas as credenciais para conectar ao banco')
    
    db.bind(provider='postgres', **credentials)
    db.generate_mapping(create_tables=True)

    select((ficha.unidade, ficha.profissional, ficha.data_consulta) for ficha in models.FichaDeAtendimento if 'FISIOTERAPIA' in ficha.unidade)[:]
