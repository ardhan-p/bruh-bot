import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot initialised...")

@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    if "bruh" in message.content:
        await message.channel.send("bruh")

client.run("")