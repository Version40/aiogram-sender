from aiogram.fsm.state import State, StatesGroup


class StepsWeather(StatesGroup):
    GET_LOCATION = State()
