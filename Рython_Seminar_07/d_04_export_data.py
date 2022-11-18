# 4) экспорт данных
# - csv
# - json

export_file = 'export_data.txt'

def export_data(data):
    with open(export_file, 'a', encoding='utf-8') as f:
        f.write(str(data))
        f.write('\n')

if __name__ == "__main__":
    pass
