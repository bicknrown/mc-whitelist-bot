import re
import os
import configparser
import discord
from discord.ext import commands
from aiomcrcon import Client

config = configparser.ConfigParser()
config.read('config.ini')

# Discord config section.
TOKEN = config.get("Discord", "TOKEN", fallback="No token found!")
BOTPREFIX = config.get("Discord", "COMMAND_PREFIX", fallback="*")
BOTDESCRIPTION = config.get("Discord", "BOT_DESCTIPTION", fallback="A bot to whitelist your Minecraft in-game name!")
WHITELISTDESCRIPTION = config.get("Discord", "WHITELIST_DESCTIPTION", fallback="A command to whitelist your Minecraft in-game name!")

# Remote minecraft config section.

HOST = config.get("Minecraft", "HOST", fallback="127.0.0.1")
PORT = int(config.get("Minecraft", "PORT", fallback="25566"))
PASSWORD = config.get("Minecraft", "PASSWORD", fallback="password")

# Internal config.
mcNameReMatch = r"^\w{3,16}$"
success = "You have been added to the whitelist!"
invalidMcName = "Invalid Username!"
nameAlreadyAdded = "This username has already been added!"
nameDNE = "This Username does not exist!"
whitelistCommand = "whitelist add "

botIntents = discord.Intents.default()
botIntents.members = True

bot = commands.Bot(command_prefix=BOTPREFIX, description=BOTDESCRIPTION, intents=botIntents)

@bot.event
async def on_ready():
    print("logged in!")

@bot.command(description=WHITELISTDESCRIPTION)
async def whitelist(ctx, ign: str):
    reMatch = re.match(mcNameReMatch,ign)
    match reMatch:
        case None:
            ctx.respond(invalidMcName)
        case _:
            client = Client(HOST,PORT,PASSWORD)
            await client.connect()
            response = await client.send_cmd(whitelistCommand + ign)
            await client.close()
            print(response)
            ctx.respond(success)




bot.run(TOKEN)
