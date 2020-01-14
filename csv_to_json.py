import csv


def convert_csv_to_json():
    with open('A_Threat_Actor_Encyclopedia.csv') as csv_file:
        in_name_section = False
        csv_reader = csv.reader(csv_file, delimiter=',')
        names = []
        for row in csv_reader:
            if in_name_section:
                if row[0] == 'Country' or row[1] == 'Country':
                    in_name_section = False
                else:
                    if row[1] != "":
                        names.append(row[1])
            elif row[0] == 'Names':
                if row[1] != "":
                    names.append(row[1])
                    in_name_section = True
            # elif row[0].startswith('Names') or row[1].startswith('Names'):
            #     in_name_section = True
            #     continue
        print(names)

if __name__ == '__main__':
    convert_csv_to_json()
