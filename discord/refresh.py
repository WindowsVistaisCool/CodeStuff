import discord

token = input("Token: ")
status = input("Status: ")
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=status))
    print("ready")

try:
    client.run(token)
except:
    print("token error")
