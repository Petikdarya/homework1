"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def count_sales(sales):
    total_sales = 0
    total_len = 0
    for items_sold in sales:
        phone_sales = sum(items_sold['items_sold'])
        total_sales += phone_sales
        phone_len = len(items_sold['items_sold'])
        total_len += phone_len 
        z = phone_sales/phone_len
        print('Продажи ' + str(items_sold['product']) + ' равны ' + str(phone_sales))
        print('Средние продажи по ' + str(items_sold['product']) + ' равны ' + str(z))
    q = total_sales/total_len
    print(f'Общие продажи составили {total_sales}')
    print(f'Общие средние продажи составили {q}')
    
# def avg_sales(sales):
#   for avg in sales:
#     avg_sale = count_sales(sales) / len(sales['item_sold'])

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    count_sales(sales)
    
      

if __name__ == "__main__":
    main()