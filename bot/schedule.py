import datetime as dt
from datetime import timedelta
import requests
from dataclasses import dataclass
import json
from constans import PARITY_NAME,NAME_WEEKDAY_CHOICES,TYPE_CHOICES
class Weekday:
  def __init__( self, dict ):
      vars(self).update( dict )
    


def date(tommorow):
    """определяет четная или нечетная неделя. при нечет возвращает - 1, чет - 0 """
    now = dt.date.today()
    weekday = dt.date.today().weekday()
    if tommorow == 1:
        now = now + timedelta(days=1)
        weekday = weekday + 1
        if weekday > 6:
            weekday = 0
    begin = dt.date(2023,2,6)
    delta = (now - begin).days
    parity =  (delta // 7) % 2 
    return weekday, parity


# def get_shedule(day):
#     if day == 0:
#         weekday, parity = date(day)
#         parity_name = PARITY_NAME[parity]
#         shedule = SHEDULE[parity][weekday]
#         shedule_name = shedule['weekday']
#         if weekday == 4 or weekday == 5 or weekday == 6:
#             text = (f'{shedule_name}.')
#         else:
#             text = f'Сегодня {parity_name}ая неделя. {shedule_name}.'
#         return shedule['img'], text
#     elif day == 1:
#         weekday, parity = date(day)
#         parity_name = PARITY_NAME[parity]

#         shedule = SHEDULE[parity][weekday]
#         parity_name = PARITY_NAME[parity]
#         shedule_name = shedule['weekday']
#         if weekday == 4 or weekday == 5 or weekday == 6:
#             text = (f'Завтра {shedule_name}')
#         else:
#             text = f'Завтра {shedule_name} {parity_name}ой недели '
#         return shedule['img'], text

#aditionally: 0 -tommorow, 1 - понедельник, 2 -вторник и т.д
def apis(day, parity, additionally):
    asd = ' '
    if additionally == 0: 
        day, parity = date(1)
        asd = 'Завтра'
    if additionally == 1: 
        day, parity = date(0)
        asd = 'Сегодня'
    response = requests.get(f'http://127.0.0.1:8000/api/v1/weekday/?name={day}&parity={parity}')
    weekday = json.loads(response.text[1:-1], object_hook=Weekday)
    text = (f'{asd} {NAME_WEEKDAY_CHOICES[day]} {PARITY_NAME[parity]} неделя'
            f'\n\n 1 - {TYPE_CHOICES[int(weekday.first_lesson[0].type)]} {weekday.first_lesson[0].name}, преподаватель {weekday.first_lesson[0].teacher}, {weekday.first_lesson[0].place}'
            f'\n\n 2 - {TYPE_CHOICES[int(weekday.second_lesson[0].type)]} {weekday.second_lesson[0].name}, преподаватель {weekday.second_lesson[0].teacher}, {weekday.second_lesson[0].place}'
            f'\n\n 3 - {TYPE_CHOICES[int(weekday.third_lesson[0].type)]} {weekday.third_lesson[0].name}, преподаватель {weekday.third_lesson[0].teacher}, {weekday.third_lesson[0].place}'
            f'\n\n 4 - {TYPE_CHOICES[int(weekday.fourth_lesson[0].type)]} {weekday.fourth_lesson[0].name}, преподаватель {weekday.fourth_lesson[0].teacher}, {weekday.fourth_lesson[0].place}'
            f'\n\n 5 - {TYPE_CHOICES[int(weekday.fifth_lesson[0].type)]} {weekday.fifth_lesson[0].name}, преподаватель {weekday.fifth_lesson[0].teacher}, {weekday.fifth_lesson[0].place}')
    return text




