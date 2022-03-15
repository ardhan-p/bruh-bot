import discord

client = discord.Client()

# dictionary which contains usernames and corresponding amount of bruh moments
userDict = {}

def printLog(message):
    print("User:", message.author)
    print("Message:", message.content)
    print()

def addBruhMoment(message):
    username = message.author.name + "#" + message.author.discriminator

    if username in userDict:
        counter = userDict.get(username) + 1
        userDict[username] = counter
    else:
        userDict[username] = 1

@client.event
async def on_ready():
    print("Bot ready...")

@client.event
async def on_message(message): 
    username = message.author.name + "#" + message.author.discriminator

    if message.author == client.user:
        return

    if "!bruhmoments" in message.content.lower():
        await message.channel.send("list of users' bruh moments")
        await message.channel.send(userDict)
        return

    if "bruh" in message.content.lower():
        printLog(message)
        addBruhMoment(message)
        await message.channel.send("bruh moment")
        await message.channel.send(username + " has " + str(userDict.get(username)) + " bruh moments so far lol")

client.run("token")