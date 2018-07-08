import csv
import sys

import fodselsnummer
from datetime import datetime

filename = "customer-values.csv"
with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
    cvs_reader = csv.DictReader(csvfile, delimiter=',')
    try:
        customer_list = list(cvs_reader)
        print("Read", len(customer_list), "customers from file")
        for customer in customer_list:
            offentlig_id = customer["offentlig_id"].replace("'", "").strip()
            if fodselsnummer.check_fnr(offentlig_id):
                # a valid customer
                if int(offentlig_id[4:6]) < 18:
                    pass  # skip people under age
                date_str = offentlig_id[0:4] + "19" + offentlig_id[4:6]

                try:
                    date = datetime.strptime(date_str, '%d%m%Y')
                    # a valid date
                    gender = "F" if int(offentlig_id[8]) % 2 == 0 else "M"

                    first_name = customer["fornavn"].replace("'", "").strip()
                    last_name = customer["etternavn"].replace("'", "").strip()
                    date_print = datetime.strftime(date, "%Y-%m-%d")

                    print(";{};{};{};{}".format(first_name, last_name, date_print, gender))

                except Exception as e:
                    pass

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, cvs_reader.line_num, e))
