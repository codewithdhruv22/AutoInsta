# Autoinsta Part 4
#By CODE WITH DHRUV
from instabot import Bot
import os
import random
import time
from PIL import Image
import smtplib
from instabot.api.api_photo import compatible_aspect_ratio

cwd = os.getcwd()

bot = Bot()

bot.login(username="username", password="***************")


def send_email():
    email = "youremail@host.com"
    password = "*********************"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    s.sendmail(email, email, f"Less than 10 Images is available in Photos Storage")
    s.quit()


def post():
    files_name = os.listdir(f"{cwd}/photos")
    file = random.choice(files_name)
    split_file_name = str(file).split(".")
    ext = str(split_file_name[1])

    img = Image.open(f"{cwd}/photos/{file}")
    size = img.size

    if not compatible_aspect_ratio(size):
        print("RESIZING IMAGE")
        newsize = (1080, 1080)
        img = img.resize(newsize)
        img.save(f"{cwd}/photos/{file}")

    if ext == 'png':
        img = Image.open(f"{cwd}/photos/{file}")
        jpeg_img = img.convert('RGB')
        jpeg_img.save(f"{cwd}/photos/converted.jpeg")
        bot.upload_photo(f"{cwd}/photos/converted.jpeg", "caption")
        os.remove(f"{cwd}/photos/{file}.REMOVE_ME")
        os.remove(f"{cwd}/photos/converted.jpeg.REMOVE_ME")
    else:
        bot.upload_photo(f"{cwd}/photos/{file}", "caption")

        os.remove(f"{cwd}/photos/{file}.REMOVE_ME")

    if len(files_name) <= 10:
        send_email()


while True:
    # posting on 8:00AM everyday
    post()
    time.sleep(86400)  # = 24 hours
