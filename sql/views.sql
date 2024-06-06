CREATE MATERIALIZED VIEW IF NOT EXISTS fichasgeral
AS 
SELECT
  id,
  unidade,
  profissional,
  especialidade,
  data_consulta,
  sexo,
  horario,
  tempo_atendido
FROM fichadeatendimento
WHERE unidade NOT LIKE '%FISIOTERAPIA%';

CREATE MATERIALIZED VIEW fichasunidades
AS SELECT
  id,
  unidade,
  profissional,
  especialidade,
  sexo,
  data_consulta,
  horario,
  tempo_atendido,
  turno
FROM
  fichadeatendimento
WHERE (especialidade = 'MEDICO DA ESTRATÉGIA DE SAUDE DA FAMILIA' OR
especialidade = 'MEDICO CLINICO GERAL' OR
especialidade = 'MÉDICO CLÍNICO')
AND (unidade LIKE 'ESF%' OR unidade LIKE 'UBS%' OR unidade LIKE '%CANGO');

CREATE MATERIALIZED VIEW fichascscn
AS SELECT
  id,
  unidade,
  profissional,
  especialidade,
  data_consulta,
  horario,
  tempo_atendido,
  turno
FROM 
    fichadeatendimento
WHERE unidadeid = 427;



CREATE MATERIALIZED VIEW fichasfisioterapia
AS SELECT
  id,
  unidade, 
  profissional, 
  data_consulta
FROM 
    fichadeatendimento
WHERE unidade LIKE '%FISIOTERAPIA%';



CREATE MATERIALIZED VIEW fichasenfermagem 
AS SELECT
  id,
  unidade,
  profissional,
  especialidade,
  sexo,
  data_consulta,
  horario,
  tempo_atendido,
  turno
FROM
  fichadeatendimento
WHERE (especialidade = 'ENFERMEIRO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA'
        OR especialidade = 'ENFERMEIRO'
        OR especialidade = 'ENFERMEIRO DA ESTRATEGIA DE AGENTE COMUNITARIO DE SAUDE'
        OR especialidade = 'ENFERMEIRO SAUDE DA FAMILIA')
AND (unidade LIKE 'ESF%' OR unidade LIKE 'UBS%' OR unidade LIKE '%CANGO');
