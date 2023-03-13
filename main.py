import json
import os.path
from random import randrange
import requests
import vk_api
from functions import *
from vk_api.longpoll import VkLongPoll, VkEventType
from Token import token

#user_id ="993117"
#user_get_info(66206783)

session_vk = vk_api.VkApi(token=token) # авторизация, для применения метода пишем method
get_vk = session_vk.get_api() # позволяет обращаться к методам через точку
longpoll_vk = VkLongPoll(session_vk) #


for event in longpoll_vk.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id
        user_get_info(user_id)
        if message == "привет":
            mssg_send(user_id, f"Я тут {user_info_dct['first_name']}, привет! \n"
                               f"Если Вы {user_info_dct['first_name']} хотите узнать о всех доступных функциях, \n"
                               f"напечатайте в сообщении слово: -- > меню")
        elif message == "меню":
            mssg_send(user_id, f"1 -- Сбор информации о Вас и уточнение данных для поиска пары!\n"
                               f"2 -- Возрастной диапазон для поиска пары.\n"
                               f"3 -- ")
        elif message == "1":
            check_user_info(user_id, user_info_dct)
            #mssg_send (user_id, f"Вот твои данные {user_info_dct}")
        elif message == "фото":
            mssg_send(user_id, f"Вот тебе {user_info_dct['first_name']}, фото!")
            mssg_send_foto(user_id, "457239119")
        else:
            mssg_send(user_id, f"Я пока знаю очеь мало слов!!!, {user_info_dct['first_name']} научи меня.")


