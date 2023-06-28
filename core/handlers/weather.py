import json
import requests
import datetime
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsWeather
from core.settings import settings


async def get_location(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}! Напиши назву міста!')
    await state.set_state(StepsWeather.GET_LOCATION)


async def get_weather(message: Message, state: FSMContext):
    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Хмарно \U00002601',
        'Rain': 'Дощ \U00002614',
        'Drizzle': 'Дощ \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Сніг \U0001F328',
        'Mist': 'Туман \U0001F32B',
    }
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.bots.weather_api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Подивись у вікно, не розумію, що там відбувається.'

        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        await message.answer(
            f'Місто: <b>{data["name"]}</b> '
            f'\nТемпература: {cur_weather}°С {wd}'
            f'\nТемпература(відчувається): {data["main"]["feels_like"]}°С'
            f'\nВологість: {humidity}% '
            f'\nТиск: {pressure} мм.рт.ст.'
            f'\nВітер: {wind} м\с '
            f'\nСхід сонця: {sunrise_timestamp}'
            f'\nЗахід сонця: {sunset_timestamp}'
            f'\nТривалість дня: {lenght_of_the_day}'
            f'\nГарного Вам дня!'
        )
        await state.clear()
    else:
        await message.reply(f'Місто вказане не вірно!')