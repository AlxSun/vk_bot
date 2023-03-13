import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Token import token, access_token
import requests, os.path, json
from random import randrange

session_vk = vk_api.VkApi(token=token)
longpoll_vk = VkLongPoll(session_vk)
#user_info_dct = {'bdate': '6.4', 'city': 61, 'sex': 2, 'first_name': 'Александр'}
user_info_dct = {}

def mssg_send(user_id, message):
    session_vk.method("messages.send", {
         "user_id" : user_id,
        "message" : message,
        "random_id" : randrange(10**7)
    })

def mssg_send_foto(user_id, photo_id):
    URL = f"https://vk.com/{user_id}?z=photo{user_id}_{photo_id}%2Fphotos{user_id}"
    session_vk.method("messages.send", {
        "user_id" : user_id,
        "attachment" : URL,
        "random_id": randrange (10 ** 7)
    })

def user_get_info(user_id):
    response = session_vk.method("users.get", {
        "user_id" : user_id,
        "v" : 5.131,
        "fields" : "first_name, last_name, bdate, sex, city"
        })
    if response:
        user_info_dct["bdate"] = response[0]["bdate"]
        user_info_dct["city"] = response[0]["city"]["id"]
        user_info_dct["sex"] = response[0]["sex"]
        user_info_dct["first_name"] = response[0]["first_name"]
    else:
        mssg_send(user_id, "Ошибка")
        return False
    return user_info_dct

def check_user_info(user_id, user_info_dct):
    check_info = []
    for key in ['bdate', 'city', 'sex']:
        if not user_info_dct.get(key):
            check_info.append(key)
    if user_info_dct.get('bdate'):
        if len(user_info_dct["bdate"].split(".")) !=3:
            check_info.append("bdate")
    if len(check_info) > 0:
       mssg_send(user_id, f"Недостаточно информации, введите следующие данные: \n"
                          f"{check_info}")
"""           for event in longpoll_vk.listen ():
               if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                   message = event.text.lower ()"""




#check_user_info(993117, user_info_dct)