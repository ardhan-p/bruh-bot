import discord

client = discord.Client()

# dictionary which contains usernames and corresponding amount of bruh moments
userDict = {}

# terminal logs
def printLog(message):
    print("User:", message.author)
    print("Message:", message.content)
    print()

# add bruh moment into dictionary
def addBruhMoment(message):
    username = message.author.name + "#" + message.author.discriminator

    if username in userDict:
        counter = userDict.get(username) + 1
        userDict[username] = counter
    else:
        userDict[username] = 1

# ready message
@client.event
async def on_ready():
    print("Bot ready...")

# checks if user message contains the word "bruh"
# adds to user to dictionary if so
# user can do "!bruhmoments" to check server list of bruh moments
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