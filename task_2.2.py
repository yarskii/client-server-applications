"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4, ensure_ascii=False)


with open('orders.json', 'w', encoding='utf-8') as f_in:
    json.dump({'orders': []}, f_in, indent=4)

write_order_to_json('t-shirt', '10', '100', 'Ivanov', '01.01.2000')
write_order_to_json('socks', '18', '12', 'Smirnov', '01.01.2001')
write_order_to_json('clock', '5', '19999', 'Petrov', '07.02.2002')
write_order_to_json('book', '7', '250', 'Kuragov', '14.10.2005')
write_order_to_json('notebook', '2', '14239', 'Filimonov', '13.09.2017')
