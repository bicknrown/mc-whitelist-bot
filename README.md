# Minecraft server whitelist Discord companion bot
Long winded name, but at least its specific.

## purpose
This bot is setup for the very specific purpose of allowing users in the discord server this bot is added in to remotely add themselves to the whitelist of the specified minecraft server.

## limitations
There are many limitations, including but not limited to:
* lack of multi (minecraft)server support
* lack of ability to remove names from whitelist remotely[^1]
* it does only one thing.

## setup
This project is a wrapper for using the Minecraft RCON protocol;
Due to many factors, I settled on using [py-cord](https://github.com/Pycord-Development/pycord) and [Aio-MC-RCON](https://github.com/Iapetus-11/aio-mc-rcon) to accomplish this task.

### configuration
This bot expects at bare minimum, a configuration file, named `config.ini`, in the same directory as the bot script, containing *AT LEAST*:
```ini
[Discord]
# Discord bot token
TOKEN=CHANGEME
[Minecraft]
# Minecraft RCON password
PASSWORD=CHANGEME
```
There are other optional settings to configure, outlined in [config.ini.default](https://github.com/bicknrown/mc-whitelist-bot/blob/master/config.ini.default), but those are the bare minimum.

## contributions
Pull requests and issues for fixes or improvements are welcome, though this project is **designed to do a single thing**, so take that as you will.

[^1]: this may be a feature, depending on your users.
