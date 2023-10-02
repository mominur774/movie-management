import requests
import requests

# Bu yerda video api sini olish uchun so'rov yaratamiz
url = "https://api.vk.com/method/video.get"
params = {
    "owner_id": -202524996, # Bu yerda video egasi identifikatorini beramiz
    "videos": "-202524996_456239034", # Bu yerda video identifikatorini beramiz
    "access_token": "your_access_token", # Bu yerda video api ga kirish uchun token beramiz
    "v": "5.131" # Bu yerda video api versiyasini beramiz
}

# Bu yerda video api sini olish uchun so'rov yuboramiz
response = requests.get(url, params=params)

# Bu yerda video api dan kelgan javobni tekshiramiz
if response.status_code == 200:
    data = response.json() # Bu yerda javobni json formatida o'zgaruvchiga saqlaymiz
    if "response" in data: # Bu yerda response deyilgan kalitni tekshiramiz
        if data["response"]["count"] > 0:
            video = data["response"]["items"][0] # Bu yerda birinchi video ma'lumotlarini o'zgaruvchiga saqlaymiz
            print(video["player"]) # Bu yerda video manzilini konsolga chiqaramiz
        else:
            print("Video topilmadi") # Bu yerda video topilmaganligini konsolga chiqaramiz
    elif "error" in data: # Bu yerda error deyilgan kalitni tekshiramiz
        print("Video api ga murojaat qilishda xatolik: {}".format(data["error"]["error_msg"])) # Bu yerda xatolik haqidagi ma'lumotni konsolga chiqaramiz
else:
    print("Video api ga murojaat qilishda xatolik") # Bu yerda video api ga murojaat qilishda xatolik bo'lganligini konsolga chiqaramiz

#
# # Bu yerda video api sini olish uchun so'rov yaratamiz
# url = "https://api.vk.com/method/video.get"
# params = {
#     "owner_id": -202524996, # Bu yerda video egasi identifikatorini beramiz
#     "videos": "-202524996_456239034", # Bu yerda video identifikatorini beramiz
#     "access_token": "your_access_token", # Bu yerda video api ga kirish uchun token beramiz
#     "v": "5.131" # Bu yerda video api versiyasini beramiz
# }
#
# # Bu yerda video api sini olish uchun so'rov yuboramiz
# response = requests.get(url, params=params)
#
# # Bu yerda video api dan kelgan javobni tekshiramiz
# if response.status_code == 200:
#     data = response.json() # Bu yerda javobni json formatida o'zgaruvchiga saqlaymiz
#     if data["response"]["count"] > 0:
#         video = data["response"]["items"][0] # Bu yerda birinchi video ma'lumotlarini o'zgaruvchiga saqlaymiz
#         print(video["player"]) # Bu yerda video manzilini konsolga chiqaramiz
#     else:
#         print("Video topilmadi") # Bu yerda video topilmaganligini konsolga chiqaramiz
# else:
#     print("Video api ga murojaat qilishda xatolik") # Bu yerda video api ga murojaat qilishda xatolik bo'lganligini konsolga chiqaramiz
