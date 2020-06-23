import csv
import os
import re

def get_data(path):
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    _path = os.path.abspath(path)
    file_list = os.listdir(_path)
    for name in file_list:
        if os.path.splitext(name)[1] == '.txt':
            file = os.path.abspath(f'{_path}/{name}')
            with open(file) as f:
                text = f.read()
                new_list = []
                pattern_creator = r'Изготовитель системы:\s+(\w*)'
                pattern_os_name = r'Название ОС:\s+([\w*\s*\b$?]+\.?[\w*\s*\b]+)\n'
                pattern_code_product = r'Код продукта:\s+(\w*-\w*-\w*-\w*)'
                pattern_type_system = r'Тип системы:\s+(\w*-\w*\s*\w*)'
                creator_system = re.findall(pattern_creator, text)
                os_name = re.findall(pattern_os_name, text)
                code_product = re.findall(pattern_code_product, text)
                type_system = re.findall(pattern_type_system, text)
                new_list.append(creator_system[0])
                new_list.append(os_name[0])
                new_list.append(code_product[0])
                new_list.append(type_system[0])
                main_data.append(new_list)
    print(main_data)
    return main_data

def write_to_csv(csv_file, path):
    main_data = get_data(path)
    norm_csv_file = os.path.normpath(csv_file)
    with open(norm_csv_file, 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            f_n_writer.writerow(row)
    with open(norm_csv_file) as f_n:
        print(f_n.read())


if __name__ == '__main__':
    write_to_csv('task_1.csv', 'stuff')
    # get_data('stuff')