import discord

client = discord.Client()

# dictionary which contains usernames and corresponding amount of bruh moments
userDict = {}

def printLog(message):
    print("User:", message.author)
    print("Message:", message.content)
    print()

# def printBotMessage(message):

def addBruhMoment(message):
    username = message.author.name + "#" + message.author.discriminator

    if username in userDict:
        counter = userDict.get(username) + 1
        userDict[username] = counter
    else:
        userDict[username] = 1

@client.event
async def on_ready():
    print("Bot initialised...")

@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    if "bruh" in message.content:
        printLog(message)
        addBruhMoment(message)
        print(userDict)
        await message.channel.send("bruh moment")
        await message.channel.send("lol")

client.run("token")