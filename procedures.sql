CREATE OR REPLACE FUNCTION time_to_seconds(time_in TIME)
RETURNS INTEGER AS $$
DECLARE
    total_seconds INTEGER;
BEGIN
    total_seconds := NULL;

    total_seconds := EXTRACT(HOUR FROM time_in) * 3600 +
                    EXTRACT(MINUTE FROM time_in) * 60 +
                    EXTRACT(SECOND FROM time_in);
    
    RETURN total_seconds;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_ficha(
    unidadeid_in INTEGER,
    unidade_in VARCHAR, 
    profissional_in VARCHAR, 
    especialidade_in VARCHAR, 
    motivo_consulta_in VARCHAR, 
    data_consulta_in DATE,
    usuario_in INTEGER,
    data_nascimento_in DATE, 
    sexo_in CHAR,
    codigo_consulta_in INTEGER,
    horario_in TIME, 
    hora_aten1_in VARCHAR, 
    hora_aten2_in VARCHAR
)
AS $$
DECLARE
    id VARCHAR;
    tempo_atendido INTEGER;
    hora_in TIME;
    hora_out TIME;
BEGIN
    --Caso não sejam especificados os horários de entrada ou saida, ele vai deixar como NULL o horario de entrada e o de saída
    --Caso contrário, ele vai calcular o total de segundos que a pessoa ficou na consulta em si, e colocar na tabela de tempo_atendido
    IF hora_aten1_in = '' THEN
        hora_in := NULL;
    END IF;
    IF hora_aten2_in = '' THEN
        hora_out := NULL;
    ELSE
        hora_in := hora_aten1_in::TIME;
        hora_out := hora_aten2_in::TIME;
        IF hora_in IS NOT NULL AND hora_out IS NOT NULL THEN
            tempo_atendido := time_to_seconds(hora_out) - time_to_seconds(hora_in);
        ELSE
            tempo_atendido := NULL;
        END IF;
    END IF;


    id := usuario_in || '/' || codigo_consulta_in;


    INSERT INTO fichadeatendimento
    (id, unidadeid, unidade, profissional, especialidade, motivo_consulta, 
    data_consulta, data_nascimento, sexo, horario, tempo_atendido)
    VALUES
    (id, unidadeid_in, unidade_in, profissional_in, especialidade_in, motivo_consulta_in, 
    data_consulta_in, data_nascimento_in, sexo_in, horario_in, tempo_atendido);
END;
$$ LANGUAGE plpgsql;
