import json
import os

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

# from Apidogs import prepare_img
from schedule import apis 
from text_command import COMMANDS
from constans import NAME_WEEKDAY_CHOICES, PARITY_NAME
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

vk_session = vk_api.VkApi(token=VK_TOKEN)
api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ID)


def get_but(text):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": "positive"
            }


def get_keyboard(text):
    return {
        'one_time' : True,
        'buttons' : [
            [get_but(text)]
        ]
    }


def json_keyboard(text):
    key = get_keyboard(text)
    keyboard = json.dumps(key, ensure_ascii = False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))  
    return keyboard


def send_mes(id, text, img):
    if img is not True:
        api.messages.send(chat_id = id, message = text, random_id = 0, )


# def send_video(id, text, vid):
#     api.messages.send(chat_id = id, message = text, random_id = 0, attachment = vid)


# weekday - показатель дня недели; '1' - завтра, '0' - сегодня
# def send_shedule(id, weekday):
#     shedule, text = get_shedule(weekday)
#     api.messages.send(chat_id = id, message = text, random_id = 0, attachment = shedule)


def send_text(id, text):
    api.messages.send(chat_id = id, message = text, random_id = 0)


def off_button(id, but_text):
    api.messages.send(chat_id = id, message = 'Нажмите, на кнопку "Вырубить кнопку", чтобы отключить старую кнопку.', keyboard = json_keyboard(but_text), random_id = 0)


def distir_schedule(msg, id):
    word = msg.split()
    # print(word[-1])
    if 'завтра' in word:
        pretext = apis(0,0,0) 
        send_text(id=id, text=pretext)
    elif 'сегодня' in word:
        pretext = apis(0,0,1)
        send_text(id=id, text=pretext)
    else:
        day_word = str(word[-1])
        day = int(str({i for i in NAME_WEEKDAY_CHOICES if NAME_WEEKDAY_CHOICES[i]==day_word})[1:-1])
        parity_word = word[-2]
        print(parity_word)
        parity = int(str({i for i in PARITY_NAME if PARITY_NAME[i]==parity_word})[1:-1])
        print(day, parity)
        pretext = apis(day,parity,1)
        send_text(id=id,text=pretext)
        
        

def distributor(msg, id):
        if msg == 'привет':
            send_text(id=id, text=COMMANDS['send_hi'])
        elif msg == 'выключить кнопку':
            off_button(id=id, but_text = 'Вырубить кнопку.')
        elif msg=='что умеешь?' or msg=='что умеешь.' or msg=='что умеешь':
            send_text(id=id, text=COMMANDS['send_help'])
        else:
            send_text(id=id, text=COMMANDS['send_error'])


def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            msg = event.object['message']['text'].lower()
            # print(event)
            id = event.chat_id
            try:
                name,msg = msg.split(',')
                name = name.strip(' ')
                msg = msg.strip(' ')
                if name == 'бот' and 'расписание' in msg:
                    distir_schedule(msg,id)
                elif name == 'бот':
                    distributor(msg,id)

            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()

