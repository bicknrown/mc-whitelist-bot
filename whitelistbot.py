import asyncio
import re
import configparser

from disnake.ext import commands
from aiomcrcon import Client

# Mutex for locking shared resource calls
lock = asyncio.Lock()

config = configparser.ConfigParser()
config.read('config.ini')

# Discord config section.
TOKEN = config.get("Discord", "TOKEN", fallback="No token found!")
BOTPREFIX = config.get("Discord", "COMMAND_PREFIX", fallback="?")
BOTDESCRIPTION = config.get("Discord", "BOT_DESCRIPTION", fallback="A bot to whitelist your Minecraft in-game name!")
WHITELISTDESCRIPTION = config.get("Discord", "WHITELIST_DESCRIPTION", fallback="A command to whitelist your Minecraft in-game name!")
LISTDESCRIPTION = config.get("Discord", "LIST_DESCRIPTION", fallback="A command to list in-game players on discord!") 

# Remote minecraft config section.

HOST = config.get("Minecraft", "HOST", fallback="127.0.0.1")
PORT = int(config.get("Minecraft", "PORT", fallback="25575"))
PASSWORD = config.get("Minecraft", "PASSWORD", fallback="password")

# Internal config.
mcNameReMatch = r"^\w{3,16}$"
invalidMcName = "Invalid Username!"
whitelistCommand = "whitelist add "
listCommand = "list"

bot = commands.Bot(command_prefix=BOTPREFIX, description=BOTDESCRIPTION)

@bot.event
async def on_ready():
    print("logged in!")
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="for /whitelist"))

@bot.slash_command(description=WHITELISTDESCRIPTION)
async def whitelist(ctx, ign: str):
    reMatch = re.match(mcNameReMatch,ign)
    if reMatch != None:
        client = Client(HOST,PORT,PASSWORD)
        await client.connect()
        async with lock:
            response = await client.send_cmd(str(str(whitelistCommand) + str(ign)))
        await client.close()
        async with lock:
            await ctx.send(response[0])
    else:
        await ctx.send(invalidMcName)

@bot.slash_command(name=listCommand, description=LISTDESCRIPTION)
async def listCommand(ctx):
    client = Client(HOST,PORT,PASSWORD)
    await client.connect()
    async with lock:
        response = await client.send_cmd("list")
    await client.close()
    async with lock:
        await ctx.send(response[0])

bot.run(TOKEN)
