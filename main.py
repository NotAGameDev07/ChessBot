from base64 import b64decode
import discord

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	print(str(message.content))
	if str(message.content) == '!ping':
		await message.channel.send('pong')

client.run("MTA4MTY3MDk4MDUxMTk4OTc4MQ.Gjkbtz.WG0pNtTLFElpPgU1rBVXWY7Xa8TRK-nJMWWLDY")
