import requests
import json
from config import keys


class ConvertException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, sym: str, amount: str):
        if base == sym:
            raise ConvertException(f'Невозможно перевести одинаковые валюты')

        try:
            base_key = keys[base.lower()]
        except KeyError:
            raise ConvertException(f'Валюта {base} не найдена. Повторите попытку.')

        try:
            sym_key = keys[sym.lower()]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {sym}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"https://v6.exchangerate-api.com/v6/69bb5c837e1e9cc9dcbc6ff/latest/{base_key}")
        resp = json.loads(r.content)
        new_price = resp['conversion_rate'][sym_key]*float(amount)
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message