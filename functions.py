import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Token import token, access_token
import requests, os.path, json
from random import randrange

session_vk = vk_api.VkApi(token=token)
longpoll_vk = VkLongPoll(session_vk)
#user_info_dct = {'bdate': '6.4', 'city': 61, 'sex': 2, 'first_name': 'Александр'}
user_info_dct = {}
check_info_lst = []

def mssg_send(user_id, message):
    session_vk.method("messages.send", {
         "user_id" : user_id,
        "message" : message,
        "random_id" : randrange(10**7)})

def mssg_send_foto(user_id, photo_id):
    URL = f"https://vk.com/{user_id}?z=photo{user_id}_{photo_id}%2Fphotos{user_id}"
    session_vk.method("messages.send", {
        "user_id" : user_id,
        "attachment" : URL,
        "random_id": randrange (10 ** 7)})

def user_get_info(user_id):
    response = session_vk.method("users.get", {
        "user_id" : user_id,
        "v" : 5.131,
        "fields" : "bdate, city, first_name"
        })
    if response:
        for key, value in response[0].items():
            if key == "bdate":
                user_info_dct["bdate"] = response[0]["bdate"]
            elif key == "sex":
                user_info_dct["sex"] = response[0]["sex"]
            elif key == "first_name":
                user_info_dct["first_name"] = response[0]["first_name"]
            elif key == "city":
                user_info_dct["city"] = response[0]["city"]["id"]
    else:
        mssg_send(user_id, "Ошибка сбора информиции о пользователе!")
        return False
    return user_info_dct

#user_get_info(993117)

def check_user_info(user_id, user_info_dct):
    for key in ['bdate', 'city', 'sex']:
        if not user_info_dct.get(key):
            check_info_lst.append(key)
    if user_info_dct.get('bdate'):
        if len(user_info_dct["bdate"].split(".")) !=3:
            check_info_lst.append("bdate")
    if len(check_info_lst) > 0:
       mssg_send(user_id, f"Недостаточно информации, введите команду (ввод)!")
       #enter_information(user_id, check_info_lst)
    return check_info_lst
"""    print(f"Ваше имя: {user_info_dct['first_name']},\n"
          f" пол: {user_info_dct['sex']},\n"
          f"день рождения: {user_info_dct['bdate']},\n"
          f" город в котором будет произведён поиск пары: {user_info_dct['city']}")"""

#check_user_info(993117, user_info_dct)

#check_info_lst = ['bdate', 'city', 'sex']

def enter_information(user_id, check_info_lst):
    print(check_info_lst)
    for event in longpoll_vk.listen ():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message = event.text.lower ()
            if check_info_lst.count("bdate") > 0:
                mssg_send(user_id, "Введите дату рождения: формат --> дд.мм.гггг")
                if len(message.split(".")) == 3:
                    user_info_dct["bdate"] = message
                    check_info_lst.remove("bdate")
                    print(check_info_lst)
            elif check_info_lst.count("sex") > 0:
                mssg_send(user_id, "Введите информацию о вашем поле:\n"
                                   "женский --->  1\n"
                                   "мужской ---> 2")
                if message ==  2:
                    user_info_dct["sex"] = message
                    check_info_lst.remove ("sex")
                    break


"""def enter_information(user_id, check_info_lst):
    for info_key in check_info_lst:
        if info_key == "sex":
            mssg_send(user_id, "В данных нехватает информации о Вашем поле,\n"
                               "ответьте в сообщении:\n"
                               "Женский пол -- > 'sex-1'\n"
                               "Мужской пол -- > 'sex-2'")
        elif info_key == "bdate":
            mssg_send(user_id, "Информация о Вашем дне рождении отсутствует или она не полная.\n"
                               "Прошу написать в сообщении день рождения,\n"
                               "в следующем формате: --> {'bdate' : дд.мм.гггг}")"""





