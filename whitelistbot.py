import re
import os
import subprocess
import interactions

TOKEN = os.getenv("TOKEN")

bot = interactions.Client(token=TOKEN)

@bot.event
async def on_ready():
    print("logged in!")

@bot.command(
        name="whitelist",
        description="add a username to the whitelist",
        options=[interactions.Option(
            type=interactions.OptionType.STRING,
            name="ingamename",
            description="your in-game name",
            required=True,
            )]
        )
async def whitelist(ctx,ingamename: str):
    valid = re.match(r"^\w{3,16}$",ingamename)
    if valid == None:
        await ctx.send("Invalid Username!")
    else:
        subprocess.run(["screen", "-S", "mc", "-X","eval", 'stuff "whitelist add {0}\015"'.format(ingamename)])
        await ctx.send("You have been added to the whitelist!")

bot.start()
