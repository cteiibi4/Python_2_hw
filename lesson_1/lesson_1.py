import subprocess
import chardet

# Задание 1
print(f'Задание №1')
words = ['разработка', 'сокет', 'декоратор']
uni_words = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
             '\u0441\u043e\u043a\u0435\u0442',
             '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
             ]
for i in words:
    print(f'Тип: {type(i)}, Содержание: {i}')
for i in uni_words:
    print(f'Тип: {type(i)}, Содержание: {i}')


# Задание 2
print(f'Задание №2')
words_l_2 = [b'class', b'function', b'method']
for i in words_l_2:
    print(f'Тип: {type(i)}, Содержание: {i}, Длинна: {len(i)}')

# Задание 3
print(f'Задание №3')
words_l_3 = ['attribute', 'класс', 'функция', 'type']
for element in words_l_3:
    try:
        obj = f"b'{element}'"
        exec(obj)
    except SyntaxError:
        print(f'{element} не может быть bytes')

# Задание 4
print(f'Задание №4')
words_l_4 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words_l_4:
    bytes_str = i.encode('utf-8')
    reverse_str = bytes_str.decode()
    print(f'Строка в байтах: {bytes_str}\nДекодированная строка: {reverse_str}')

# Задание 5
print(f'Задание №5')
ping = 'ping'
adress = ['yandex.ru', 'youtube.com']
args_ping = []
for i in adress:    # Данный участок нужно упростить
    arg = [ping, i]
    args_ping.append(arg)
for arg in args_ping:
    ping_process = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in ping_process.stdout:
        code = chardet.detect(line)
        line = line.decode(code['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

# Задание 6
print(f'Задание №6')
words_for_file = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as f:
    for i in words_for_file:
        f.write(f'{i}\n')
    # print(f)

with open('test_file.txt', 'rb') as f:
    content = f.read()
    encoding = chardet.detect(content)['encoding']

with open('test_file.txt', encoding=encoding) as f:
    content = f.read()
print(content)