import discord
import time
from discord.ext import commands
from config import settings
from mcstatus import MinecraftServer

serveronline = 0
status = []
serverip = "Your server"
bot = commands.Bot(command_prefix = settings['prefix'])
nowserver = MinecraftServer.lookup(serverip)

try:
    status = nowserver.status()
    serveronline = 1
except:
    serveronline = 0

if serveronline == 1 and status != 0:
    status = nowserver.status()
    pingnow = status.latency
    print(status.raw['players'])
    if len(status.raw['players']) >= 3:
        usersConnected = [user['name'] for user in status.raw['players']['sample']]
    else:
        usersConnected = []
@bot.command()
async def Connected(ctx):
    if serveronline == 1:
        embed1 = discord.Embed(color = 0x00e600, title = 'Connected players')
        embed1.add_field(name=f"connected player - {len(usersConnected)}:", value="** **", inline=False)
        for i in range(len(usersConnected)):
            embed1.add_field(name=f"`{usersConnected[i]}`", value="** **", inline=True)
        await ctx.send(embed = embed1)
    else:
         embed1 = discord.Embed(color = 0xff0000, title = 'Connected players')
         embed1.add_field(name="server now offline:x:", value="** **", inline=False)
         await ctx.send(embed = embed1) 
@bot.command()
async def full(ctx):
    if serveronline == 1:
        embed2 = discord.Embed(color = 0x00e600, title = 'Server Info')
        embed2.add_field(name="Status: online :white_check_mark:", value="** **", inline=False)
        embed2.add_field(name=f"Ip: {serverip}", value="** **", inline=False)
        embed2.add_field(name=f"Ping: {pingnow}", value="** **", inline=False)
        embed2.add_field(name=f"Players: {len(usersConnected)}", value="** **", inline=False)
        for i in range(len(usersConnected)):
            embed2.add_field(name=f"`{usersConnected[i]}`", value="** **", inline=True)
        await ctx.send(embed = embed2)
    else:
         embed1 = discord.Embed(color = 0xff0000, title = 'Server Info')
         embed1.add_field(name="server now offline:x:", value="** **", inline=False)
         await ctx.send(embed = embed1)
@bot.command()
async def snow(ctx):
    await ctx.send("\u2603\u2603\u2603")
@bot.command()    
async def snow2(ctx):
    await ctx.send("`\u2603\u2603\u2603`")
bot.run(settings['token'])