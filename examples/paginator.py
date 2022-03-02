import discord
from discord.ext import commands
from discord.ext import pages
from discord import Embed

import pycordSuperUtils

client = commands.Bot(command_prefix="-")

embedc = discord.Color(0, 208, 255)


@client.event
async def on_ready():
    print("Page manager is ready.", bot.user)

     

# The old buttonpaginator was removed from PSU! Here's a example for the official py-cord paginator
    
@client.command()
async def paginator(ctx):
    await ctx.defer()
    prefix = "/"
    invite = "https://discord.com/api/oauth2/authorize?client_id=828902907084537867&permissions=8&scope=bot%20applications.commands"
    page1 = Embed(
        color=embedc,
        title="**🤖 Help Menu**",
        timestamp=datetime.datetime.utcnow()
    )
    page1.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
    page1.set_thumbnail(url=client.user.avatar.url)
    page1.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    page1.add_field(name="**🌐Features**", value="> Moderation \n> Information\n> Fun\n> Helpful Setups like applications, join2create and much more!", inline=False)
    page1.add_field(name="**📊 Stats**", value=f"```py\nGuilds: {len(client.guilds)}\nUsers: {len(client.users)}\nUptime: 5 minutes```", inline=False)
    page1.add_field(name="**🆘 Help & Links**", value=f"**Support Server**\n> [Join here](https://discord.gg/mQkydPS82f)\n**Developer**\n> Areo | 513786050271772673\n**Invite me**\n> [Invite now!]({invite})", inline=False)

    page2 = Embed(
        color=embedc,
        title="**🤖 Bot Help Menu**",
        description=f"**🔨 Moderation Commands**",
        timestamp=datetime.datetime.utcnow()
    )
    page2.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
    page2.set_thumbnail(url=client.user.avatar.url)

    page3 = Embed(
        color=embedc,
        title="**🤖 Bot Help Menu**",
        description=f"**ℹ Information Commands**",
        timestamp=datetime.datetime.utcnow()
    )

    page4 = Embed(
        color=embedc,
        title="**🤖 Bot Help Menu**",
        description=f"**🎭 Fun Commands**",
        timestamp=datetime.datetime.utcnow()
    )

    page5 = Embed(
        color=embedc,
        title="**🤖 Bot Help Menu**",
        description=f"**⚙ Setup Commands**",
        timestamp=datetime.datetime.utcnow()
    )
    page5.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
    page5.set_thumbnail(url=client.user.avatar.url)
    

    paginationList = [page1, page2, page3, page4, page5]

    # Creating buttons
    b1 = pages.PaginatorButton("next", label="▶️", style=discord.ButtonStyle.blurple)
    b2 = pages.PaginatorButton("first", label="⏪", style=discord.ButtonStyle.blurple)
    b4 = pages.PaginatorButton("last", label="⏩", style=discord.ButtonStyle.blurple)
    b3 = pages.PaginatorButton("prev", label="◀️", style=discord.ButtonStyle.blurple)
    button_list = [b1, b2, b3, b4]


    # initializing the paginator
    paginator = pages.Paginator(pages=paginationList,
                                show_disabled=True,
                                show_indicator=False,
                                use_default_buttons=False,
                                custom_buttons=button_list)


    # start paginating
    await paginator.respond(ctx.interaction, ephemeral=False)


bot.run("token")
