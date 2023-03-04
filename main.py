from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = input("Token: ")
session_vk = vk_api.VkApi(token=token)
#longpoll_vk = VkLongPoll(session_vk)

def reply_msg(user_id, message):
    session_vk.method("messages.send", {
        "user_id" : user_id,
        "message" : message,
        "random_id" : randrange(100)})

for event in VkLongPoll(session_vk).listen():
    if event.type == VkEventType.MESSAGE_NEW:
