import discord
import json
from random import randint

def get_keys(filename="keys.json"):
    parsed = None
    with open(filename) as keyfile:
        raw = keyfile.read()
        parsed = json.loads(raw)
    return parsed

def get_quote():
    data = None
    with open('quotes.json') as f:
        data = f.read()
    parsed_data = json.loads(data)
    index = randint(0,25)
    return parsed_data[index]['quote']

keys = get_keys()
token = keys['discord_token']
client = discord.Client()
@client.event
async def on_message(message):
    recv = message.content
    channel = message.channel
    if message.author == client.user:
        pass
    if recv.startswith('!thanos'):
        msg = get_quote()
        state = not (recv[8:] is '')
        await client.send_message(channel, content=msg, tts=state)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

while True:
    try:
        client.run(token)
    except Exception as e:
        if "Event loop" in str(e):
            print("\nStopping bot....")
            break
        else:
            print(e)
            continue