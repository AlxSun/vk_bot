from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Token import token

#token = input("Token: ")
session_vk = vk_api.VkApi(token=token)
get_vk = session_vk.get_api()
longpoll_vk = VkLongPoll(session_vk)

def mssg_send(user_id, message):
    session_vk.method("messages.send", {
         "user_id" : user_id,
        "message" : message,
        "random_id" : randrange(10**7)
    })
user_info = {}
def user_get_info(user_id):
    response = session_vk.method("users.get", {
        "user_id" : user_id,
        "v" : 5.131,
        "fields" : "first_name, last_name, bdate, sex, city"
        })
    if response:
        user_info["bdate"] = response[0]["bdate"]
        user_info["city"] = response[0]["city"]["title"]
        user_info["sex"] = response[0]["sex"]
        user_info["first_name"] = response[0]["first_name"]
    else:
        mssg_send(user_id, "Ошибка")
        return False
    return user_info
#user_get_info(993117)
#user_get_info(66206783)

for event in longpoll_vk.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id
        user_get_info(user_id)
        if message == "привет":
            mssg_send(user_id, f"Я тут {user_info['first_name']}")
        elif message == "пока":
            mssg_send(user_id, "Пока!")
        else:
            mssg_send(user_id, "Я пока знаю очеь мало слов!!!")

#print(user_info)
