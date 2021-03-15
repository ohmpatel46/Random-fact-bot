import discord
import os
import requests
import json

client=discord.Client()

def get_quote():
  resp=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(resp.text)
  quote=json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def get_fact():
  resp=requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
  json_data=json.loads(resp.text)
  return(json_data["text"])

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author== client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Hello '+message.author.display_name+'!')
  
  if message.content.startswith('!inspire'):
    quote =get_quote()
    await message.channel.send(quote)

  if message.content.startswith('!fact'):
    fact=get_fact()
    await message.channel.send(fact)

client.run(os.getenv('TOKEN'))
