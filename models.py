from pony.orm import Database, Required, Optional, PrimaryKey
from datetime import date, time, timedelta

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


class FichasGeral(db.Entity):
    _table_ = 'fichasgeral'
    id = PrimaryKey(str)
    unidade = Required(str)
    profissional = Optional(str)
    especialidade = Optional(str)
    data_consulta = Required(date)
    sexo = Required(str)
    horario = Required(time)
    tempo_atendido = Optional(timedelta)


class FichasUnidades(db.Entity):
    _table_ = 'fichasunidades'
    id = PrimaryKey(str)
    unidade = Required(str)
    profissional = Optional(str)
    especialidade = Optional(str)
    sexo = Required(str)
    data_consulta = Required(date)
    horario = Required(time)
    tempo_atendido = Optional(timedelta)
    turno = Required(str)


class FichasCSCN(db.Entity):
    _table_ = 'fichascscn'
    id = PrimaryKey(str)
    unidade = Required(str)
    profissional = Optional(str)
    especialidade = Optional(str)
    data_consulta = Required(date)
    horario = Required(time)
    tempo_atendido = Optional(timedelta)
    turno = Required(str)


class FichasFisioterapia(db.Entity):
    _table_ = 'fichasfisioterapia'
    id = PrimaryKey(str)
    unidade = Required(str)
    profissional = Optional(str)
    data_consulta = Required(date)


class FichasEnfermagem(db.Entity):
    _table_ = 'fichasenfermagem'
    id = PrimaryKey(str)
    unidade = Required(str)
    profissional = Optional(str)
    especialidade = Optional(str)
    sexo = Required(str)
    data_consulta = Required(date)
    horario = Required(time)
    tempo_atendido = Optional(timedelta)
    turno = Required(str)
