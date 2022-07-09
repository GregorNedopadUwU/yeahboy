#IMPORT
import discord
from discord.ext import commands
import asyncio
import os
import random
import urllib
import json
import time
from discord import Client, Intents, Embed
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import psutil
import asyncio
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from discord.ext.commands import check
import traceback
import sys
from discord.ext import commands
import platform
import subprocess

client = commands.Bot(command_prefix="-")
client.remove_command('help')
def myping(host):
    response = os.system("ping -c 1 " + host)
    
    if response == 0:
        return True
    else:
        return False
#ZPRAVA ON READY

    
@client.event
async def on_ready():
    print("Online")
    client.statuses = cycle(['/add-server', f'DisHub'])
    change_status.start()
@tasks.loop(seconds=30)
async def change_status():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(client.statuses)))  

@client.command()
async def ping(ctx):
  embed = discord.Embed(title="DisHub Ping", description=myping("dishub.fun"))
  await ctx.send(embed=embed)

my_secret = os.environ['nottokenlol']

    

client.run(os.environ['nottokenlol'])





