import json
import csv
from pathlib import Path


def convert(file: str | Path) -> None:
    my_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            my_dict[name.title()] = float(number)
    with open(f'{file.stem}.json', 'w', encoding='utf-8') as f_write:
        json.dump(my_dict, f_write, indent=2, ensure_ascii=False)


def json_to_csv(file: str | Path) -> None:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

    list_rows = []
    for level, id_name_dict in data.items():
        for id, name in id_name_dict.items():
            list_rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_rows)

    def csv_to_json(csv_file: str | Path, json_file: str | Path) -> None:
        json_list = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as f_read:
            csv_read = csv.reader(f_read, dialect='excel-tab')
            for i, line in enumerate(csv_read):
                json_dict = {}
                if i != 0:
                    level, id, name = line
                    json_dict['level'] = int(level)
                    json_dict['id'] = f'{int(id):010}'
                    json_dict['name'] = name.title()
                    json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                    json_list.append(json_dict)

        with open(json_file, 'w', encoding='utf-8') as f_write:
            json.dump(json_list, f_write, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    convert(Path('results.txt'))
    json_to_csv(Path('users.json'))
