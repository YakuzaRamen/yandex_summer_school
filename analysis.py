'''
1) На вход дается
    а) 1 строка список товаров в формате json
    б) 5 строк в формате словаря
2) Необходимо отфильтровать список товаров
3) Вернуть подходящие товары в виде json обьекта
'''
import json
from datetime import datetime


def analysis(data: str, *args) -> json:
    data = json.loads(data)
    data_filter = {obj.split()[0]: obj.split()[1] for obj in args}
    result = {'result': {}}

    for product in data:
        # data for matching
        product_price = int(product['price'])
        filter_price_greater = int(data_filter['PRICE_GREATER_THAN'])
        filter_price_less = int(data_filter['PRICE_LESS_THAN'])
        product_date = datetime.strptime(product['date'], '%d.%m.%Y')
        filter_after_date = datetime.strptime(data_filter['DATE_AFTER'], '%d.%m.%Y')
        filter_before_date = datetime.strptime(data_filter['DATE_BEFORE'], '%d.%m.%Y')

        if data_filter['NAME_CONTAINS'] in product['name'] \
                and filter_price_greater < product_price < filter_price_less \
                and filter_after_date < product_date < filter_before_date:
            result['result'].update(product)

    return json.dumps(result, indent=4)
