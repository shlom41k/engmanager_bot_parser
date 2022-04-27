# -*- coding: utf-8 -*-

# shlom41k

import json
import asyncio
import time
import telebot
import random
from datetime import datetime

from settings import SETTINGS_JSON, SHLOM41k, save_settings, load_settings, get_settings
from stickers import STIC_PRESS_F, FLAGS, COMMANDS, ADMIN_COMMANDS
from parser import get_ligas, get_stat
from logger import Logger

# Load settings and data
PRESETS = load_settings(SETTINGS_JSON)
token, url, log_file, admins, white_users, black_users = get_settings(PRESETS)
bl = black_users

# Create logger
log = Logger(log_file)

# Create BOT
bot = telebot.TeleBot(token)

# Create keyboard
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/all_stat', '/ligas')


def is_main_admin(user_id: int) -> bool:
    """
    Check if user is main admin
    """
    return True if user_id == SHLOM41k else False


def is_user_admin(user_id: int) -> bool:
    """
    Check if user is admin
    """
    return True if str(user_id) in admins.keys() else False


def is_user_allowed(foo):
    """
    Check if user is allowed to use bot
    """
    def wrapper(message):

        user_id = message.from_user.id
        username, firstname, lastname = message.from_user.username, message.from_user.first_name, message.from_user.last_name

        # print(f"{datetime.now()}: USER REQUEST <- [{username}] {firstname} {lastname}: '{message.text}'")
        log.add(f"{datetime.now()}: USER REQUEST <- [{username}] {firstname} {lastname}: '{message.text}'")

        # Check if user is allowed to use bot
        if str(user_id) in white_users.keys():
            foo(message)
            # print(f"{datetime.now()}: BOT RESPONSE -> [{username}] {firstname} {lastname}")
            log.add(f"{datetime.now()}: BOT RESPONSE -> [{username}] {firstname} {lastname}")

        elif str(user_id) not in black_users.keys():
            black_users[str(user_id)] = [username, firstname, lastname]
            save_settings(PRESETS, SETTINGS_JSON)
            # print(f"Unauthorized user: id={user_id} | {username} | {firstname} | {lastname}. No response")
            log.add(f"Unauthorized user: id={user_id} | {username} | {firstname} | {lastname}. No response")

    return wrapper


@bot.message_handler(commands=['start'])
def start_message(message):
    """
    Start message
    """
    # print(f"{datetime.now()}: USER REQUEST <- [{message.from_user.username}] {message.from_user.first_name} {message.from_user.last_name}: '{message.text}'")
    log.add(f"{datetime.now()}: USER REQUEST <- [{message.from_user.username}] {message.from_user.first_name} {message.from_user.last_name}: '{message.text}'")

    ans = bot.send_sticker(message.chat.id, random.choice(STIC_PRESS_F), reply_markup=keyboard1)

    # print(f"{datetime.now()}: BOT RESPONSE -> [{message.from_user.username}] {message.from_user.first_name} {message.from_user.last_name}")
    log.add(f"{datetime.now()}: BOT RESPONSE -> [{message.from_user.username}] {message.from_user.first_name} {message.from_user.last_name}")


@bot.message_handler(commands=['all_stat'])
@is_user_allowed
def command_all_stat(message):
    """
    All stat command
    """
    ans = bot.send_message(message.chat.id, f"Request is in progress...")
    log.add(f"{datetime.now()}: INFO: Request to -> '{url}'")

    try:
        stat = get_stat(url)
        log.add(f"{datetime.now()}: INFO: Response from <- '{url}'")
    # print(stat)
    except:
        ans = bot.send_message(message.chat.id, f"ERROR: No response from {url}")
        log.add(f"{datetime.now()}: ERROR: No response from '{url}'")
        return

    for liga, value in stat.items():
        ans = ""
        try:
            description, matches = value
            games = "\n".join([f"{result}" for result, link in matches.items()])
            liga_name = FLAGS.get(liga, FLAGS['default'])[0] + "  " + FLAGS.get(liga, FLAGS['default'])[1].decode()

            ans = f"{liga_name}  {description}:\n\n{games}\n\n"
            # print(ans)
            ans = bot.send_message(message.chat.id, ans, parse_mode="html")
        except:
            ans = bot.send_message(message.chat.id, f"No data about '{liga}'")
            log.add(f"{datetime.now()}: ERROR: No data from '{url}' about league '{liga}'")

    ans = bot.send_message(message.chat.id, f"Statistic end")


@bot.message_handler(commands=['ligas'])
@is_user_allowed
def command_ligas(message):
    """
    Ligas command
    """
    log.add(f"{datetime.now()}: INFO: Response from <- '{url}'")

    try:
        ligas = get_ligas(url)
        log.add(f"{datetime.now()}: INFO: Response from <- '{url}'")
    except:
        ans = bot.send_message(message.chat.id, f"ERROR: No response from {url}")
        log.add(f"{datetime.now()}: ERROR: No response from '{url}'")
        return

    ans = bot.send_message(message.chat.id,
                           "\n".join([f"/{FLAGS.get(liga, FLAGS['default'])[0]} "
                                      f"{FLAGS.get(liga, FLAGS['default'])[1].decode()}" for liga in ligas]))


@bot.message_handler(commands=COMMANDS[:-1])
@is_user_allowed
def command_commands(message):
    """
    Commands
    """

    for liga_name, description in FLAGS.items():
        if description[0] in message.text:

            log.add(f"{datetime.now()}: INFO: Response from <- '{url}'")

            try:
                stat = get_stat(url, liga_name)
                log.add(f"{datetime.now()}: INFO: Response from <- '{url}'")

                for liga, value in stat.items():
                    ans = ""

                    description, matches = value
                    games = "\n".join([f"{result}" for result, link in matches.items()])
                    # games = "\n".join([f"{result}\n{link}" for result, link in matches.items()])
                    # games = "\n".join([f"<a href='{link}'>{result}</a>" for result, link in matches.items()])
                    liga_name = FLAGS.get(liga, FLAGS['default'])[0] + "  " + FLAGS.get(liga, FLAGS['default'])[1].decode()

                    ans = f"{liga_name}  {description}:\n\n{games}\n\n"
                    ans = bot.send_message(message.chat.id, ans, parse_mode="html")
                    # "<a href='http://engmanager.ru/web/manager/match/view/?id=15447'>Прямая связь</a>"
            except:
                ans = bot.send_message(message.chat.id, f"ERROR: No response from {url}")
                log.add(f"{datetime.now()}: ERROR: No response from '{url}'")


@bot.message_handler(commands=['blacklist'])
@is_user_allowed
def command_blacklist(message):
    """
    Blacklist command
    """
    if is_user_admin(message.from_user.id):
        # print(black_users)
        ans = bot.send_message(message.chat.id, "\n".join([f"{key}: {value}" for key, value in black_users.items()]))


@bot.message_handler(commands=['whitelist'])
@is_user_allowed
def command_whitelist(message):
    """
    Whitelist command
    """
    if is_user_admin(message.from_user.id):
        # print(black_users)
        ans = bot.send_message(message.chat.id, "\n".join([f"{key}: {value}" for key, value in white_users.items()]))


@bot.message_handler(commands=['admins'])
@is_user_allowed
def command_admins(message):
    """
    Admins command
    """
    if is_user_admin(message.from_user.id):
        # print(black_users)
        ans = bot.send_message(message.chat.id, b"\xF0\x9F\x91\xA4".decode() + " Administrators:\n" + "\n".join([f"{key}: {value}" for key, value in admins.items()]))
        ans = bot.send_message(message.chat.id, b"\xF0\x9F\x93\x84".decode() + " Administrators commands:\n" + "\n".join([f"{key}: {value}" for key, value in ADMIN_COMMANDS.items()]), parse_mode="html")


@bot.message_handler(content_types=["text"])
@is_user_allowed
def command_test(message):

    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am StasyanBot!", parse_mode="html")

    elif message.text.startswith("/adduser"):
        # Adding some user to whitelist
        if is_user_admin(message.from_user.id):
            try:
                _, user_id = message.text.split()

                user_data = black_users.pop(user_id, None)

                if user_data is None:
                    bot.send_message(message.from_user.id, "ERROR! Unknown user!")
                else:
                    white_users[user_id] = user_data
                    save_settings(PRESETS, SETTINGS_JSON)
                    bot.send_message(message.from_user.id, f"User id={user_id}: {user_data} added to whitelist")
                    log.add(f"{datetime.now()}: INFO: id={message.from_user.id} '[{message.from_user.username}] "
                            f"{message.from_user.first_name} {message.from_user.last_name}' "
                            f"add user id={user_id} {user_data} to whitelist")
            except:
                bot.send_message(message.from_user.id, "ERROR! Try again")
        else:
            bot.send_message(message.from_user.id, "You do not have administrator rights :(")
            log.add(f"{datetime.now()}: INFO: id={message.from_user.id} '[{message.from_user.username}] "
                    f"{message.from_user.first_name} {message.from_user.last_name}' try '{message.text}'")

    elif message.text.startswith("/addadmin"):
        # Adding some user to admins
        if is_main_admin(message.from_user.id):
            try:
                _, user_id = message.text.split()
                user_data = white_users.get(user_id, None)

                if user_data is None:
                    bot.send_message(message.from_user.id, "ERROR! Unknown user!")
                else:
                    admins[user_id] = user_data
                    save_settings(PRESETS, SETTINGS_JSON)
                    bot.send_message(message.from_user.id, f"User id={user_id}: {user_data} added to administrators")
                    log.add(f"{datetime.now()}: INFO: id={message.from_user.id} '[{message.from_user.username}] "
                            f"{message.from_user.first_name} {message.from_user.last_name}' "
                            f"add user id={user_id} {user_data} to administrators")
            except:
                bot.send_message(message.from_user.id, "ERROR! Try again")
        else:
            bot.send_message(message.from_user.id, "You do not have superuser rights :(")
            log.add(f"{datetime.now()}: INFO: id={message.from_user.id} '[{message.from_user.username}] "
                    f"{message.from_user.first_name} {message.from_user.last_name}' try '{message.text}'")

    elif message.text == "/clear blacklist":
        # Clear blacklist
        black_users.clear()
        black_users["chat_id"] = ["username", "firstname", "lastname"]
        save_settings(PRESETS, SETTINGS_JSON)
        ans = bot.send_message(message.chat.id, "\n".join([f"{key}: {value}" for key, value in black_users.items()]))
        log.add(f"{datetime.now()}: INFO: id={message.from_user.id} '[{message.from_user.username}] "
                f"{message.from_user.first_name} {message.from_user.last_name}' clear blacklist")


@bot.message_handler(content_types=['document', 'audio'])
@is_user_allowed
def handle_document_audio(message):
    bot.send_message(message.from_user.id, "Thanks :)")


@bot.message_handler(content_types=['sticker'])
@is_user_allowed
def sticker_id(message):
    """
    Sticker command
    """
    ans = bot.send_sticker(message.chat.id, random.choice(STIC_PRESS_F))


if __name__ == '__main__':
    def main():
        while True:
            try:
                log.add(f"{datetime.now()}: INFO: Telebot [token='{token}'] started")
                print("Bot started ...")
                bot.polling(none_stop=True, interval=1)
            except Exception as e:
                log.add(f"{datetime.now()}: ERROR: message='{e}'")
                # print(e)
                time.sleep(5)

    async def foo():
        while True:
            print("Hello")
            time.sleep(1)

    main()


    # loop = asyncio.get_event_loop()
    # loop.create_task(main())
    # loop.create_task(foo())
    # loop.run_forever()
