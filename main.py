import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('Bot Encendido')
  
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.send(f'{amount} messages cleared.')
  await ctx.channel.purge(limit=amount)

client.run('token de tu bot')
