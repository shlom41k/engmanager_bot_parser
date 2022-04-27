# English Manager Bot Parser
***A simple Telegram bot for parsing results of games at http://engmanager.ru/.***

The bot allows you to receive data with the results of matches from the site http://engmanager.ru/.
Access to the bot is limited. To gain access, the administrator must add your chattid to the allowed list.
<hr>

## Bot Commands
### Users commands:
- ```/start``` - start chat;
- ```/ligas``` - get list of ligas;
- ```/all_stat``` - get list of all games results;

### Admins commands:
- ```/blacklist``` - get list of unauthorized users;
- ```/whitelist``` - get list of authorized users (added to whitelist);
- ```/admins``` - get list of admins commands and their descriptions;
- ```/adduser <user_chatID>``` - add some user with chatID <user_chatID> to whitelist;
- ```/deluser <user_chatID>``` - delete some user with chatID <user_chatID> from whitelist;
- ```/clear``` - delete all users from blacklist.

## Main tools:
```
- Python 3.10.2
- PyTelegramBotAPI 4.2.2
- Beautifullsoup4 4.10.0
- Aiohttp 3.8.1
```

## Projects setup
All settings are in the config file [settings.json](https://github.com/shlom41k/engmanager_bot_parser/blob/main/src/scripts/settings.json). Insert your bot token into ```"token": ""``` field in this file.

Running application:
- ```pip install -r requirements.txt```
- ```python .\main.py ```
<hr>

## Some screenshots:
> ### Bot
<p align="center">
  <img src="https://github.com/shlom41k/engmanager_bot_parser/blob/main/src/img/start.jpg" width="30%">
  <img src="https://github.com/shlom41k/engmanager_bot_parser/blob/main/src/img/ligas.jpg" width="30%">
  <img src="https://github.com/shlom41k/engmanager_bot_parser/blob/main/src/img/all_stat.jpg" width="30%">
  <img src="https://github.com/shlom41k/engmanager_bot_parser/blob/main/src/img/admin_commands.jpg" width="30%">
</p>

> ### Site
<p align="center">
  <img src="https://github.com/shlom41k/engmanager_bot_parser/blob/main/src/img/manager.PNG">
</p>
