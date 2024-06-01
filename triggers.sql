CREATE OR REPLACE FUNCTION update_unidade()
RETURNS TRIGGER AS $$
BEGIN
    NEW.unidade := 
        CASE NEW.unidadeid
            WHEN 3 THEN 'UBS ALVORADA'
            WHEN 58 THEN 'UBS VILA NOVA'
            WHEN 377 THEN 'ESF NOVA CONCORDIA'
            WHEN 427 THEN 'CSCN'
            ELSE NEW.unidade
        END;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE TRIGGER update_unidade_trigger
BEFORE INSERT ON fichadeatendimento
FOR EACH STATEMENT
EXECUTE FUNCTION update_unidade();