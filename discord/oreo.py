import discord
import requests
from discord.ext import commands
from discord_slash import SlashCommand, utils
from discord_slash.model import SlashContext
from os import system
from asyncio import sleep

client = commands.Bot(command_prefix='\'', intents=discord.Intents.all())
client.remove_command('help')
slash = SlashCommand(client)
token = "Nzg5OTI1NTEwMDMzMDQ3NTgy.X95JdQ.FOoUUDFOhuWiUEgMqx-NnEkZnpM"

url = "https://discord.com/api/v8/applications/789925510033047582/commands"

@client.event
async def on_ready():
    print("ready")
    # await utils.manage_commands.add_slash_command(client.user.id, "Nzg5OTI1NTEwMDMzMDQ3NTgy.X95JdQ.FOoUUDFOhuWiUEgMqx-NnEkZnpM", 788525642168926219, "kick", "idk man dnt ask", None)

@slash.slash(name="nickname")
async def _nickname(ctx: SlashContext, nick):
    await ctx.author.edit(nick=nick)
    await ctx.send(content=f"Your nickname has been changed to {nick}", complete_hidden=True)

@slash.slash(name='restart')
async def _restart(ctx: SlashContext):
    if ctx.author.id == 392502213341216769:
        await ctx.send(content="Restarting bot...", complete_hidden=True)
        await client.close()
        system("python3 oreo.py")
    else:
        await ctx.send(content="You do not have permission!", hidden=True)

@slash.slash(name='stop')
async def _stop(ctx: SlashContext):
    if ctx.author.id == 392502213341216769:
        await ctx.send(content="Stopping bot...", complete_hidden=True)
        await client.close()
    else:
        await ctx.send(content="You do not have permission!", hidden=True)

@slash.slash(name='start')
async def _start(ctx: SlashContext):
    await ctx.send(content="Starting bot...")
    await sleep(2)
    await ctx.send(content="oh wait, im already started, you dumbass")

@client.command()
async def help(ctx):
    await ctx.send(content="no u")

@slash.slash(name='help')
async def _help(ctx: SlashContext, page):
    await help.callback(ctx)

@client.command()
@commands.is_owner()
async def t(ctx, d):
    # e = requests.get("https://discord.com/api/v8/applications/789925510033047582/commands", headers={"Authorization": "Nzg5OTI1NTEwMDMzMDQ3NTgy.X95JdQ.FOoUUDFOhuWiUEgMqx-NnEkZnpM"})
    url = "https://discord.com/api/v8/applications/788519667542261770/guilds/788525642168926219/commands"

    json = {
        "name": "start",
        "description": "Starts the bot"
        # "options": [
        #     {
        #         "name": "name",
        #         "description": "Your new name",
        #         "type": 3,
        #         "required": True,
                # "choices": [
                #     {
                #         "name": "1",
                #         "value": "page_1"
                #     },
                #     {
                #         "name": "2",
                #         "value": "page_2"
                #     }
                # ]
            # },
            # {
            #     "name": "only_smol",
            #     "description": "Whether to show only baby animals",
            #     "type": 5,
            #     "required": False
            # }
        # ]
    }
    # headers = {
    #     "Authorization": "Bot Nzg5OTI1NTEwMDMzMDQ3NTgy.X95JdQ.FOoUUDFOhuWiUEgMqx-NnEkZnpM"
    # }
    headers = {
        "Authorization": "Bot Nzg4NTE5NjY3NTQyMjYxNzcw.X9ksKg.s_Qy5tVERqGzn9qDVckJMc5-8uI"
    }

    # r = requests.post(url, headers=headers, json=json)
    r = requests.delete(url + f"/{d}", headers=headers)
    e = requests.get(url, headers=headers)
    try:
        await ctx.send(e.text)
        await ctx.send(r)
    except:
        pass

client.run("Nzg5OTI1NTEwMDMzMDQ3NTgy.X95JdQ.FOoUUDFOhuWiUEgMqx-NnEkZnpM")
