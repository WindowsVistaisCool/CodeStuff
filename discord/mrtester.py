import discord
import requests
from discord.ext import commands
from discord_slash import SlashCommand, utils
from discord_slash.model import SlashContext
from os import system
from random import randint

client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
client.remove_command('help')
slash = SlashCommand(client)
token = "NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg"

@client.event
async def on_ready():
    print("ready")
    # await utils.manage_commands.add_slash_command(client.user.id, "NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg", 777553249388462093, "kick", "idk man dnt ask", None)

@slash.slash(name="blep")
async def _blep(ctx: SlashContext, animal, only_smol=False):
    await ctx.send(content=f"you chose {animal} and {only_smol}")

@client.command()
async def help(ctx, page=None):
    if page == "2":
        await ctx.send(content="no u")
    else:
        e = discord.Embed(title="sometimes i dont like writing code")
        await ctx.send(content=None, embeds=[e])

@slash.slash(name='help')
async def _help(ctx: SlashContext, page=None):
    if page == "page_1":
        page = "1"
    elif page == "page_2":
        page = "2"
    await help.callback(ctx, page)

@slash.slash(name='gaymeter')
async def _gaymeter(ctx: SlashContext, member=None):
    if member is None:
        member = ctx.author
    else:
        oof = member.replace('<@!', '')
        oof = oof.replace('>', '')
        try:
            member = await ctx.guild.fetch_member(int(oof))
        except:
            await ctx.send(content="The member was not found, please @ping someone!", complete_hidden=True)
            return
    e = discord.Embed(title=f'GAYMETER for {member}', color=discord.Color.blurple(), description=f'{randint(1, 100)}% gay\nWOW!')
    await ctx.send(content=None, embeds=[e])

@client.command()
@commands.is_owner()
async def t(ctx, d):
    # e = await utils.manage_commands.remove_slash_command(client.user.id, "NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg", ctx.guild.id, cmd_id)
    # e = await utils.manage_commands.get_all_commands(client.user.id, token, ctx.guild.id)
    # e = requests.get("https://discord.com/api/v8/applications/713461668667195553/commands", headers={"Authorization": "NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg"})
    url = "https://discord.com/api/v8/applications/713461668667195553/guilds/777553249388462093/commands"

    json = {
        "name": "gaymeter",
        "description": "GAYMETER WHAHAHAHAAHTT?????",
        "options": [
            {
                "name": "member",
                "description": "Mention a Member",
                "type": 3,
                "required": False,
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
            }
            # {
            #     "name": "only_smol",
            #     "description": "Whether to show only baby animals",
            #     "type": 5,
            #     "required": False
            # }
        ]
    }

    headers = {
        "Authorization": "Bot NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg"
    }

    # e = requests.post("https://discord.com/api/v8/applications/713461668667195553/guilds/777553249388462093/commands", headers={"Authorization": "Bot NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg"}, json=json)
    r = requests.delete(url + f"/{d}", headers=headers)
    e = requests.get(url, headers=headers)
    try:
        await ctx.send(e.text)
        await ctx.send(r)
    except:
        pass


@client.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send("restart")
    await client.close()
    system("python3 mrtester.py")

client.run("NzEzNDYxNjY4NjY3MTk1NTUz.Xsgc9Q.i_P0GsSFK_yRBfjvaNabQ9-6Jfg")
