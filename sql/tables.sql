CREATE TABLE fichadeatendimento(
  id CHARACTER(15) PRIMARY KEY,
  unidadeid INTEGER,
  unidade VARCHAR(75),
  profissional VARCHAR(75),
  especialidade VARCHAR(75),
  motivo_consulta VARCHAR(50),
  data_consulta DATE,
  data_nascimento DATE,
  sexo CHAR(1),
  horario TIME,
  tempo_atendido INTEGER,
  turno VARCHAR(15)
);