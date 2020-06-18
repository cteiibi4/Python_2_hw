import os
import yaml

for_dict_1 = ['лаб-да-бу-да', 'шфивтануться']
for_dict_2 = 12
for_dict_3 = {'12€': 45, '45€':85}
dict_for_yaml = {'key_1':for_dict_1,
                 'key_2':for_dict_2,
                 'key_3':for_dict_3
                 }
with open(os.path.abspath('stuff/data.yaml'), 'w') as f:
    yaml.dump(dict_for_yaml, f, default_flow_style=False, allow_unicode = True)

with open(os.path.abspath('stuff/data.yaml')) as f:
    print(f.read())
    if f.read() == dict_for_yaml:
        print('Совпадают')
    else:
        print('Не совпадают')