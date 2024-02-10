import discord
import env
import aws

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

userDict = {}

# terminal logs
def printLog(message):
    print("Username:", message.author)
    print("Message:", message.content)
    print()

# add a bruh moment into dictionary
def addBruhMoment(message):
    username = message.author.name

    if username in userDict:
        counter = userDict.get(username) + 1
        userDict[username] = counter
    else:
        userDict[username] = 1

# bot initialised
@client.event
async def on_ready():
    print("Bot ready...")

@client.event
async def on_message(message): 
    username = message.author.name

    if message.author == client.user:
        return

    if "!mybruhmoments" in message.content.lower():
        response = aws.checkUser(message)
        print(response)
        await message.channel.send("you have " + str(userDict.get(username)) + " bruh moments")
        await message.channel.send("yikes!")
        return

    if "bruh" in message.content.lower():
        printLog(message)
        addBruhMoment(message)
        await message.channel.send("bruh moment")
        await message.channel.send(username + " has " + str(userDict.get(username)) + " bruh moments so far lol")

client.run(env.DISCORD_TOKEN)