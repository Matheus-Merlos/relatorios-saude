from pony.orm import Database, Required, Optional, PrimaryKey
from datetime import date, time

db = Database()

class FichaDeAtendimento(db.Entity):
    id = PrimaryKey(str, max_len=15)
    unidadeid = Required(int)
    unidade = Required(str, max_len=75)
    profissional = Optional(str, max_len=75)
    especialidade = Optional(str, max_len=75)
    motivo_consulta = Optional(str, max_len=50)
    data_consulta = Required(date)
    data_nascimento = Required(date)
    sexo = Required(str, max_len=1)
    horario = Required(time)
    hora_aten1 = Optional(time)
    hora_aten2 = Optional(time)
