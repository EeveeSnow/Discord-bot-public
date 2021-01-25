import discord


from discord.ext import commands
from mcstatus import MinecraftServer

from automatic import st
from servername import name
from config import settings


serverip = name["name"]
bot = commands.Bot(command_prefix = settings['prefix'])
def server_check(serverip):
    try:
        serverip = name["name"]
        nowserver = MinecraftServer.lookup(serverip)
        status = nowserver.status()
        serveronline = 1
    except:
        serveronline = 0
    if serveronline == 1:
        status = nowserver.status()
        pingnow = status.latency
        if len(status.raw['players']) >= 3:
            usersConnected = [user['name'] for user in status.raw['players']['sample']]
        else:
            usersConnected = []
    return (serveronline, usersConnected, status, pingnow)

@bot.command()
async def Connected(ctx):
    serveronline = st["line"]
    if serveronline == 1:
        usersConnected = st["usersConnected"]
        embed1 = discord.Embed(color = 0x00e600, title = 'Connected players')
        embed1.add_field(name=f"connected player - {len(usersConnected)}:", value="****", inline=False)
        for i in range(len(usersConnected)):
            embed1.add_field(name=f"`{usersConnected[i]}`", value="****", inline=True)
        await ctx.send(embed = embed1)
    else:
         embed1 = discord.Embed(color = 0xff0000, title = 'Connected players')
         embed1.add_field(name="server now offline:x:", value="****", inline=False)
         await ctx.send(embed = embed1) 
@bot.command()
async def full(ctx):
    serveronline = st["line"]
    if serveronline == 1:
        pingnow = st["pingnow"]
        usersConnected = st["usersConnected"]
        embed2 = discord.Embed(color = 0x00e600, title = 'Server Info')
        embed2.add_field(name="Status: online :white_check_mark:", value="****", inline=False)
        embed2.add_field(name=f"Ip: {serverip}", value="****", inline=False)
        embed2.add_field(name=f"Ping: {pingnow}", value="****", inline=False)
        embed2.add_field(name=f"Players: {len(usersConnected)}", value="****", inline=False)
        for i in range(len(usersConnected)):
            embed2.add_field(name=f"`{usersConnected[i]}`", value="** **", inline=True)
        await ctx.send(embed = embed2)
    else:
         embed2 = discord.Embed(color = 0xff0000, title = 'Server Info')
         embed2.add_field(name="server now offline:x:", value="** **", inline=False)
         await ctx.send(embed = embed2)
@bot.command()
async def snow(ctx):
    await ctx.send("\u2603\u2603\u2603")
@bot.command()    
async def snow2(ctx):
    await ctx.send("`\u2603\u2603\u2603`")
bot.run(settings['token'])