from random import randrange

import requests
from openai import OpenAI
import json

import os

import discord
from discord import Member
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, MissingPermissions, Context
from discord import Intents

from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']

intents=discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)

def getUrlFromJson(Number):
  with open('img.json') as f:
      data = json.load(f)

  if str(Number) in data:
      data = str(Number)

@bot.event
async def on_ready():
  print("Meow Meow!")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.mention}!")

@bot.event
async def on_member_remove(member):
    await member.send(f"{member.username} Has left us")

@bot.command()
async def kill1(ctx, arg):
  num = randrange(1,2)
  error_state = randrange(1,2)
  if arg == "<@1213580421925699645>":
    await ctx.send("You can't kill me, Time to vaporize you!")
  elif arg == "<@1114659960656248902>":
    if error_state == 1:
      await ctx.send("You can't kill him, Time to send you to {dimension}")
      await ctx.send("Alert! 'dimension' is undifined. Error has been found, Correcting")
      await ctx.send("You can't kill him, Time to send you to VOID")
    elif error_state == 2:
      await ctx.send("You can't kill him, Time to send you to VOID")
    await ctx.send(f"You killed {arg}!")
  elif num == 2:
    await ctx.send(f"You failed to kill {arg}!")


@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, arg):
  await member.kick(reason=arg)
  await ctx.send(f'Kicked {member}')

@kick.error
async def kick_error(ctx, error):
 if isinstance(error, commands.MissingPermissions):
   await ctx.send("You don't have permission to kick people! ")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, arg):
  await member.ban(reason=arg)
  await ctx.send(f'Kicked {member}')

@ban.error
async def ban_error(ctx, error):
 if isinstance(error, commands.MissingPermissions):
   await ctx.send("You don't have permission to Ban people! ")

@bot.command()
async def sync(ctx):
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
     print(e)
     ctx.send(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message("Hello World!")

@bot.tree.command(name="cat")
async def cat(interaction: discord.Interaction):
  data = requests.get("https://api.thecatapi.com/v1/images/search")
  data = data.json()
  get = data[0]
  result = get["url"]

  embed = discord.Embed(title="Cat", description="Here is a free cat picture!", url=result, color=discord.Color.random())
  embed.set_author(name="TheCatAPI", url="https://thecatapi.com/", icon_url="https://FloppaGcdn.github.io/images/thecatapi-cat.74a07522.png") 
  embed.set_image(url=result)
  await interaction.response.send_message(embed=embed)
  

@bot.tree.command(name="credits")
async def credits(interaction: discord.Interaction):
  embed = discord.Embed(title="Credits", description="The credits of FloppaBOT 2", color=discord.Color.random())
  
  embed.add_field(name="Developers", value="@floppa_god1000")
  embed.add_field(name="Software", value="TheCatAPI \n PixaBay \n Discord.PY")
  
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ping", description="Shows the bots latency")
async def ping(interaction: discord.Interaction):
      latency = round(bot.latency * 1000)  # convert to milliseconds
      await interaction.response.send_message(f"Pong! Latency: {latency}ms")

@bot.tree.command(name="kill", description="Kills a user")
@app_commands.describe(arg="The user to kill")
async def kill(interaction: discord.Interaction, arg: str):
  
  num = randrange(1,2)
  error_state = randrange(1,2)
  if arg == "<@1213580421925699645>":
    await interaction.response.send_message("You can't kill me, Time to vaporize you!")
  elif arg == "<@1114659960656248902>":
    if error_state == 1:
      await interaction.response.send_message("You can't kill him, Time to send you to {dimension}")
      await interaction.response.send_message("Alert! 'dimension' is undifined. Error has been found, Correcting")
      await interaction.response.send_message("You can't kill him, Time to send you to VOID")
    elif error_state == 2:
      await interaction.response.send_message("You can't kill him, Time to send you to VOID")
    await interaction.response.send_message(f"You killed {arg}!")
  elif num == 2:
    await interaction.response.send_message(f"You failed to kill {arg}!")

@bot.tree.command(name="dog", description="Shows a random Dog picture")
async def dog(interaction: discord.Interaction):
  with open('img.json') as f:
    data = json.load(f)

  category_data = data['dogs']
  number = randrange(1, 15)
  number = str(number)

  result = category_data[number]

  embed = discord.Embed(title="Dog", description="Here is a free lake picture ig."+"Cat better lol", url=result, color=discord.Color.random())
  embed.set_author(name="Pixabay", url="https://pixabay.com", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Pixabay-logo-new.svg/400px-Pixabay-logo-new.svg.png") 
  embed.set_image(url=result)
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="nature", description="Shows a random Nature picture")
async def nature(interaction: discord.Interaction):
  with open('img.json') as f:
    data = json.load(f)

  category_data = data['nature']
  number = randrange(1, 15)
  number = str(number)

  result = category_data[number]

  embed = discord.Embed(title="Nature", description="Here is a free nature picture or go outside.", url=result, color=discord.Color.random())
  embed.set_author(name="Pixabay", url="https://pixabay.com", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Pixabay-logo-new.svg/400px-Pixabay-logo-new.svg.png") 
  embed.set_image(url=result)
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="flower", description="Shows a random Flower picture")
async def flower(interaction: discord.Interaction):
  with open('img.json') as f:
    data = json.load(f)

  category_data = data['flower']
  number = randrange(1, 15)
  number = str(number)

  result = category_data[number]

  embed = discord.Embed(title="Flower", description="Here is a free flower picture!", url=result, color=discord.Color.random())
  embed.set_author(name="Pixabay", url="https://pixabay.com", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Pixabay-logo-new.svg/400px-Pixabay-logo-new.svg.png") 
  embed.set_image(url=result)
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="lake", description="Shows a random lake picture")
async def lake(interaction: discord.Interaction):
  with open('img.json') as f:
    data = json.load(f)

  category_data = data['lake']
  number = randrange(1, 15)
  number = str(number)

  result = category_data[number]
  
  embed = discord.Embed(title="Lake", description="Here is a free lake picture!", url=result, color=discord.Color.random())
  embed.set_author(name="Pixabay", url="https://pixabay.com", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Pixabay-logo-new.svg/400px-Pixabay-logo-new.svg.png") 
  embed.set_image(url=result)
  await interaction.response.send_message(embed=embed)

bot.run(TOKEN)
