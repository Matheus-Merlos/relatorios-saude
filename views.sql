DROP MATERIALIZED VIEW fichasgeral;

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

CREATE OR REPLACE MATERIALIZED VIEW fichasunidades
AS SELECT
  id,
  unidade,
  profissional,
  especialidade,
  sexo,
  data_consulta,
  horario,
  tempo_atendido,
  CASE
    WHEN EXTRACT(HOUR FROM horario) IS NULL THEN NULL
    WHEN EXTRACT(HOUR FROM horario) >= 18 THEN 'FORA DE TURNO'
    WHEN EXTRACT(HOUR FROM horario) >= 13 THEN 'TARDE'
    WHEN EXTRACT(HOUR FROM horario) >= 7 THEN 'MANHÃ'
    ELSE 'FORA DE TURNO'
  END AS turno
FROM
  fichadeatendimento
WHERE (especialidade = 'MEDICO DA ESTRATÉGIA DE SAUDE DA FAMILIA' OR
especialidade = 'MEDICO CLINICO GERAL' OR
especialidade = 'MÉDICO CLÍNICO')
AND (unidade LIKE 'ESF%' OR unidade LIKE 'UBS%' OR unidade LIKE '%CANGO');



CREATE OR REPLACE MATERIALIZED VIEW fichascscn
AS SELECT
  id,
  unidade,
  profissional,
  especialidade,
  data_consulta,
  horario,
  tempo_atendido,
  CASE
    WHEN EXTRACT(HOUR FROM horario) IS NULL THEN NULL
    WHEN EXTRACT(HOUR FROM horario) >= 19 AND EXTRACT(HOUR FROM horario) <= 23 THEN 'NOITE'
    WHEN EXTRACT(HOUR FROM horario) >= 17 THEN 'DUPLO'
    WHEN EXTRACT(HOUR FROM horario) >= 13 THEN 'TARDE'
    WHEN EXTRACT(HOUR FROM horario) >= 7 THEN 'MANHÃ'
    ELSE 'FORA DE TURNO'
  END AS turno
FROM 
    fichadeatendimento
WHERE unidadeid = 427;



CREATE OR REPLACE MATERIALIZED VIEW fichasfisioterapia
AS SELECT
  id,
  unidade, 
  profissional, 
  data_consulta
FROM 
    fichadeatendimento
WHERE unidade LIKE '%FISIOTERAPIA%';



CREATE OR REPLACE MATERIALIZED VIEW fichasenfermagem 
AS SELECT
  id,
  unidade,
  profissional,
  especialidade,
  sexo,
  data_consulta,
  horario,
  tempo_atendido,
  CASE
    WHEN EXTRACT(HOUR FROM horario) IS NULL THEN NULL
    WHEN EXTRACT(HOUR FROM horario) >= 18 THEN 'FORA DE TURNO'
    WHEN EXTRACT(HOUR FROM horario) >= 13 THEN 'TARDE'
    WHEN EXTRACT(HOUR FROM horario) >= 7 THEN 'MANHÃ'
    ELSE 'FORA DE TURNO'
  END AS turno
FROM
  fichadeatendimento
WHERE (especialidade = 'ENFERMEIRO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA'
        OR especialidade = 'ENFERMEIRO'
        OR especialidade = 'ENFERMEIRO DA ESTRATEGIA DE AGENTE COMUNITARIO DE SAUDE'
        OR especialidade = 'ENFERMEIRO SAUDE DA FAMILIA')
AND (unidade LIKE 'ESF%' OR unidade LIKE 'UBS%' OR unidade LIKE '%CANGO');
