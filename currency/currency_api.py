from fastapi import APIRouter,Depends
import requests

currency_router = APIRouter(prefix='/currency', tags=['Работа с Курсами Валют'])

# def chech_currency_rates_redis():
#     usd = redis_db.get('USD')
#     rub = redis_db.get('RUB')
#     eur = redis_db.get('EUR')
#
#     if usd and rub and eur:
#         return {
#                 "USD": usd.decode(),
#                 "RUB": rub.decode(),
#                 "EUR": eur.decode(),
#                 }
#     else:
#         return False

@currency_router.post('/get-rates')
async def get_currency_rates():
    nbu_url = 'https://nbu.uz/uz/exchange-rates/json/'
    usd = requests.get(nbu_url).json()[-1]
    rub = requests.get(nbu_url).json()[-6]
    eur = requests.get(nbu_url).json()[7]


    return {'USD': usd, 'RUB': rub, 'EUR': eur}