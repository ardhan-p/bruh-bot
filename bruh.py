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
        print(message.author)
        print(message)
        await message.channel.send("bruh")

client.run("Insert bot token here")