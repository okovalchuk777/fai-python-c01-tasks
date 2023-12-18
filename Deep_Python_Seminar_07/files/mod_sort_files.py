# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с нексколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path


def sort_files(dir_in: str, dir_out: str) -> None:
    # кортежи с расширениями
    video_extensions_tuple = (
        'webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'rrc', 'gifv', 'mng', 'mov', 'avi', 'qt', 'wmv', 'yuv', 'rm',
        'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'm4v', 'svi', '3gp', '3g2', 'mxf',
        'roq', 'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b', 'mod')
    music_extensions_tuple = ('aif', 'cda', 'mid', 'midi', 'mp3', 'wav', 'wma', 'ogg', 'flac', 'ape', 'm4a')
    photo_extensions_tuple = (
        'jpg', 'jpeg', 'jpe', 'jif', 'jfif', 'jfi', 'png', 'gif', 'webp', 'tiff', 'tif', 'psd', 'raw', 'arw', 'cr2',
        'nrw',
        'k25', 'bmp', 'dib', 'heif', 'heic', 'ind', 'indd', 'indt', 'jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2', 'svg',
        'svgz',
        'ai', 'eps', 'pdf')
    text_extensions_tuple = (
        'txt', 'rtf', 'log', 'docx', 'doc', 'html', 'htm', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx')

    # входная директория (из которой нужно отсортировать файлы)
    path_in = Path(dir_in)

    # выходная директория (в которую перемещаем файлы и сортируем по папкам)
    path_out = Path(dir_out)

    # получаем список файлов и подпапок в основной директории
    entities_gen = (p for p in path_in.rglob("*"))

    # папки для сортировки
    folder_name_tuple = ('VIDEO', 'MUSIC', 'PHOTO', 'TEXT')

    # пути к новым папкам (пригодятся при перемещении файлов)
    new_dir_video = Path.joinpath(path_out, "VIDEO")
    new_dir_music = Path.joinpath(path_out, "MUSIC")
    new_dir_photo = Path.joinpath(path_out, "PHOTO")
    new_dir_text = Path.joinpath(path_out, "TEXT")

    # кортеж с новыми папками (пригодится при удалении пустых папок)
    # path_out должен проверяться последним
    new_dirs_tuple = (new_dir_video, new_dir_music, new_dir_photo, new_dir_text, path_out)

    # создаём новые папки
    for folder_name in folder_name_tuple:
        Path.joinpath(path_out, folder_name).mkdir(parents=True, exist_ok=True)

    # сортировка файлов по папкам
    for entity in entities_gen:
        if entity.is_file():
            if entity.suffix[1:].lower() in video_extensions_tuple:
                new_name = f'cat_{entity.stem}{entity.suffix}'  # or directly: f'cat_{entity.name}'
                Path(entity).rename(new_dir_video / new_name)

            elif entity.suffix[1:].lower() in music_extensions_tuple:
                new_name = f'cat_{entity.stem}{entity.suffix}'  # or directly: f'cat_{entity.name}'
                Path(entity).rename(new_dir_music / new_name)

            elif entity.suffix[1:].lower() in photo_extensions_tuple:
                new_name = f'cat_{entity.stem}{entity.suffix}'  # or directly: f'cat_{entity.name}'
                Path(entity).rename(new_dir_photo / new_name)

            elif entity.suffix[1:].lower() in text_extensions_tuple:
                new_name = f'cat_{entity.stem}{entity.suffix}'  # or directly: f'cat_{entity.name}'
                Path(entity).rename(new_dir_text / new_name)

    for new_dir in new_dirs_tuple:
        try:
            new_dir.rmdir()
        except FileNotFoundError:
            print(f'Error: cannot find the "{new_dir}" directory.')
        except NotADirectoryError:
            print(f'Error: "{new_dir}" is not a directory.')
        except OSError:
            print(f"Error: the '{new_dir}' directory isn't empty or there's a path issue.")
        else:
            print(f'Successfully removed the "{new_dir}" directory.')


if __name__ == '__main__':
    sort_files('D:\\29. Погружение в Python. Часть 1 (семинары)\\07\\NOT_Sorting_Dir',
               'D:\\29. Погружение в Python. Часть 1 (семинары)\\07\\SORTING_Dir')

