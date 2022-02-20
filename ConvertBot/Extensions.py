import json
import requests
from Config import exchanges



class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(base : str, quote : str, amount : str):
        
        if quote == base:
            raise ConvertionException(f'Cant convert similar currency: {base}')

        try:  
            quote_ticker = exchanges[quote]
        except KeyError:
            raise ConvertionException(f'Cant process: {quote}')
        
        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise ConvertionException(f'Cant process: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Cant process value: {amount}')

        r = requests.get(f'https://free.currconv.com/api/v7/convert?apiKey=ae3c94a1609a6889cd55&q={base_ticker}_{quote_ticker}&compact=ultra')
        cont = json.loads(r.content)
        
    
        asked_cont = cont[f'{base_ticker}_{quote_ticker}'] * amount
        asked_cont = round(asked_cont, 3)
        return asked_cont