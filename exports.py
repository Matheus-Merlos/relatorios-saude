from pony.orm import select, db_session
from datetime import time, timedelta, date
import models
import utils
import csv


@db_session
def view_to_csv(view, csv_name: str) -> None:
    with open(f'output/{csv_name}.csv', 'w', encoding='utf-8', newline='') as file:
        query = select(ficha for ficha in view)[:]

        writer = None
        for element in query:
            element_as_dict = element.to_dict()
            del element_as_dict['id']
            for k, v in element_as_dict.items():
                if isinstance(v, (time, timedelta, date)):
                    element_as_dict[k] = str(v)

            if writer is None:
                writer = csv.DictWriter(
                    file, fieldnames=element_as_dict.keys())
                writer.writeheader()

            writer.writerow(element_as_dict)


if __name__ == '__main__':
    utils.connect_to_database()

    view_to_csv(models.FichasGeral, 'fichas-geral')
    view_to_csv(models.FichasUnidades, 'fichas-medico')
    view_to_csv(models.FichasCSCN, 'fichas-cscn')
    view_to_csv(models.FichasFisioterapia, 'fichas-fisioterapia')
    view_to_csv(models.FichasEnfermagem, 'fichas-enfermagem')
