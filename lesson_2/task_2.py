import json
import os

def write_order_to_json(path_to_json, product, quantity, price, buyer, date):
    dict_to_json = {
        'Товар': product,
        'Количество' : quantity,
        'Цена': price,
        'Покупатель': buyer,
        'Дата': date,
        }
    path = os.path.abspath(path_to_json)
    if os.path.splitext(path)[1] == '.json':
        with open(path) as f:
            f_content = f.read()
            objs = json.loads(f_content)
            values = objs.get('orders')
        values.append(dict_to_json)
        objs.update({'orders': values})
        with open(path, 'w') as f:
            json.dump(objs, f, indent=4)
    else:
        print(f'Файл {os.path.split(path)[1]} неверного формата.')

if __name__ == '__main__':
    write_order_to_json('stuff/orders.json', 'Рамирези', 5, 120, 'Степка', '9.05.2020')