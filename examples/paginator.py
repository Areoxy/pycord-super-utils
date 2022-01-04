import discord
from discord.ext import commands

import pycordSuperUtils

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    print("Page manager is ready.", bot.user)


@bot.command()
async def paginator(ctx):
    messages = [
        discord.Embed(title="Data (1/2)", description="Hello world"),
        discord.Embed(title="Data (2/2)", description="Hello world"),
    ]

    await pycordSuperUtils.ButtonsPageManager(ctx, messages).run()


bot.run("token")
