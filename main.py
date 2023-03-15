import json
import os.path
from random import randrange
import requests
import vk_api
from functions import *
from vk_api.longpoll import VkLongPoll, VkEventType
from Token import token

session_vk = vk_api.VkApi(token=token) # авторизация, для применения метода пишем method
get_vk = session_vk.get_api() # позволяет обращаться к методам через точку
longpoll_vk = VkLongPoll(session_vk) #



for event in longpoll_vk.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id
        if message == "привет":
            mssg_send(user_id, "Я тут, привет! \n"
                               "Если Вы  хотите узнать о всех доступных функциях, \n"
                               "напечатайте в сообщении слово: -- > меню")
        elif message == "меню":
            mssg_send(user_id, "1 -- Сбор информации о Вас и уточнение данных для поиска пары!\n"
                               "2 -- Возрастной диапазон для поиска пары.\n"
                               "3 -- Мои данные")
        elif message == "1":
            user_get_info (user_id)
            check_user_info(user_id, user_info_dct)
        elif message == "ввод":
            pass
        elif message == "3":
            user_get_info(user_id)
            mssg_send(user_id, f"Вот инфа о тебе: {user_info_dct}")
        elif message == "фото":
            mssg_send(user_id, "Вот   фото!")
            mssg_send_foto(user_id, "457239119")
        else:
            mssg_send(user_id, f"Я пока знаю очень мало слов!!!")


