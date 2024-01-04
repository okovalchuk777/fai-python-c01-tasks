# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
# директорий.

import json
import csv
import pickle
from pathlib import Path


def dir_info(path_in: str | Path, path_log: str | Path) -> None:
    # входная директория с файлами
    path_in = Path(path_in)

    with (open(Path(path_log, 'dir_info.json'), 'w', encoding='utf-8') as f_json_write,
          open(Path(path_log, 'dir_info.csv'), 'w', encoding='utf-8') as f_csv_write,
          open(Path(path_log, 'dir_info.pickle'), 'wb') as f_pickle_write):

        dir_info_dict = {f'{path_in}': {}}

        # параметры корневой директории
        parents_root_dir = path_in.parents[0]
        dir_info_dict[f'{path_in}']['root directory'] = f'{parents_root_dir}'
        structure_root_dir = 'Directory'
        dir_info_dict[f'{path_in}']['structure'] = structure_root_dir
        size_root_dir = 0
        entities_gen_root_dir = (p for p in path_in.rglob("*"))
        for entity_root_dir in entities_gen_root_dir:
            if entity_root_dir.is_file():
                size_root_dir += Path(entity_root_dir).stat().st_size
        dir_info_dict[f'{path_in}']['size in bytes'] = size_root_dir

        dir_info_list = [{"full_path": f'{path_in}', "root_dir": f'{parents_root_dir}', "structure":
            structure_root_dir, "size": size_root_dir}]

        # получаем список файлов и подпапок в основной директории (без учёта параметров корневой директории)
        entities_gen = (p for p in path_in.rglob("*"))

        for entity in entities_gen:
            dir_info_dict[f'{entity}'] = {}
            parents = Path(entity).parents[0]
            dir_info_dict[f'{entity}']['root directory'] = f'{parents}'
            if entity.is_file():
                structure = 'file'
                dir_info_dict[f'{entity}']['structure'] = structure
                # To get the file size in Python
                size = Path(entity).stat().st_size
                dir_info_dict[f'{entity}']['size in bytes'] = size
                dir_info_list.append({"full_path": f'{entity}', "root_dir": f'{parents}', "structure":
                    structure, "size": size})
            elif entity.is_dir():
                structure = 'Directory'
                dir_info_dict[f'{entity}']['structure'] = structure
                size_dir = 0
                entities_gen_dir = (p for p in Path(entity).rglob("*"))
                for entity_dir in entities_gen_dir:
                    if entity_dir.is_file():
                        size_dir += Path(entity_dir).stat().st_size
                dir_info_dict[f'{entity}']['size in bytes'] = size
                dir_info_list.append({"full_path": f'{entity}', "root_dir": f'{parents}', "structure":
                    structure, "size": size})

        json.dump(dir_info_dict, f_json_write, indent=2, ensure_ascii=False)

        csv_write = csv.DictWriter(f_csv_write, fieldnames=["full_path", "root_dir", "structure", "size"],
                                   dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(dir_info_list)

        pickle.dump(dir_info_dict, f_pickle_write)


if __name__ == '__main__':
    dir_info('D:\\29. Погружение в Python. Часть 1 (семинары)\\08\\DIR_for_TEST',
             'D:\\29. Погружение в Python. Часть 1 (семинары)\\08')
