import subprocess

print('Task_1', '\n')

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

lst = ['разработка', 'сокет', 'декоратор']

for line in lst:
    print(f'Переменная - {line}, тип переменной - {type(line)}, длина переменной - {len(line)}')

print('-' * 10)

lst_1 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
         '\u0441\u043e\u043a\u0435\u0442',
         '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for line in lst_1:
    print(f'Переменная - {line}, тип переменной - {type(line)}, длина переменной - {len(line)}')

print('-' * 10, '\n', 'Task_2', '\n')

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
# в последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

lst_2 = ['class', 'function', 'method']

for line in lst_2:
    print(f'Начальная переменная - {line}, тип переменной - {type(line)}')
    new_line = f"b'{line}'"

    eval(new_line)
    print(f'Переменная - {new_line},'
          f' тип переменной - {type(eval(new_line))},'
          f' длина переменной - {len(new_line)}')

print('-' * 10, '\n', 'Task_3', '\n')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

lst_3 = ['attribute', 'класс', 'функция', 'type']

for line in lst_3:
    print(f'Начальная переменная - {line}, тип переменной - {type(line)}')
    try:
        new_line = f"b'{line}'"
        eval(new_line)
        print(f'Переменная - {new_line},'
              f' тип переменной - {type(eval(new_line))},'
              f' длина переменной - {len(new_line)}')
    except SyntaxError:
        print(f'"{line}" невозможно записать в байтовом типе')

print('-' * 10, '\n', 'Task_4', '\n')

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

lst_4 = ['разработка', 'администрирование', 'protocol', 'standart']

for line in lst_4:
    print(f'Переменная - {line}, тип переменной - {type(line)}')
    enc_line = str.encode(line, encoding='utf-8')
    print(f'Закодированная переменная - {enc_line}, тип переменной - {type(enc_line)}')
    dec_line = enc_line.decode('utf-8')
    print(f'Раскодированная переменная - {dec_line}, тип переменной - {type(dec_line)}')

print('-' * 10, '\n', 'Task_5', '\n')

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

args_1 = ['ping', '-c 5', 'yandex.ru']
args_2 = ['ping', '-c 5', 'youtube.com']

subproc_ping_1 = subprocess.Popen(args_1, stdout=subprocess.PIPE)

for line_1 in subproc_ping_1.stdout:
    print(line_1.decode('utf-8'))

subproc_ping_2 = subprocess.Popen(args_2, stdout=subprocess.PIPE)

for line_2 in subproc_ping_2.stdout:
    print(line_2.decode('utf-8'))

print('-' * 10, '\n', 'Task_6', '\n')

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

with open('test_file.txt', 'w') as text:
    text.write('сетевое программирование' + '\n' +
               'сокет' + '\n' +
               'декоратор' + '\n')

print(text)

with open('test_file.txt', 'r', encoding='utf-8') as text:
    for i in text:
        print(i)

