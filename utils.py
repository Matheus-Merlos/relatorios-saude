from dotenv import load_dotenv
from pony.orm import db_session, dbapiprovider, set_sql_debug
from models import db
import os

def connect_to_database():
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
    
    with db_session:
        with open('views.sql', 'r', encoding='utf-8') as file:
            file_as_str = file.read()
        db.execute(file_as_str)
    
    db.generate_mapping()