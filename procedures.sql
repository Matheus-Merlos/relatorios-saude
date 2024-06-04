CREATE OR REPLACE FUNCTION time_to_seconds(time_in TIME)
RETURNS INTEGER OR NULL AS $$
DECLARE
    total_seconds INTEGER;
BEGIN
    IF total_seconds IS NULL THEN 
        RETURN NULL;
    END IF;

    total_seconds := EXTRACT(HOUR FROM time_in) * 3600 +
                    EXTRACT(MINUTE FROM time_in) * 60 +
                    EXTRACT(SECOND FROM time_in)
    
    RETURN total_seconds;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE PROCEDURE insert_ficha(
    unidadeid INTEGER,
    unidade VARCHAR, 
    profissional VARCHAR, 
    especialidade VARCHAR, 
    motivo_consulta VARCHAR, 
    data_consulta DATE,
    usuario INTEGER,
    data_nascimento DATE, 
    sexo CHAR,
    codigo_consulta INTEGER,
    horario TIME, 
    hora_aten1 TIME, 
    hora_aten2 TIME
)
AS $$
DECLARE
    id VARCHAR := usuario || '/' || codigo_consulta;
    tempo_atendido INTEGER;
BEGIN
    tempo_atendido := time_to_seconds(hora_aten2) - time_to_seconds(hora_aten1);

    INSERT INTO fichadeatendimento
    (id, unidadeid, unidade, profissional, especialidade, motivo_consulta, 
    data_consulta, data_nascimento, sexo, tempo_atendido)
    VALUES
    (id, unidadeid, unidade, profissional, especialidade, motivo_consulta, 
    data_consulta, data_nascimento, sexo, tempo_atendido);
END;
$$ LANGUAGE plpgsql;

CALL insert_ficha()