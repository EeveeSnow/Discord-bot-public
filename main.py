import discord
from discord.ext import commands
from config import settings
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix = settings['prefix'])
nowserver = MinecraftServer.lookup("Your server")

status = nowserver.status()

    pingnow = status.latency
    if len(status.raw['players']) >= 3:
        usersConnected = [user['name'] for user in status.raw['players']['sample']]
    else:
        usersConnected = []
@bot.command()
async def Connected(ctx):
    embed1 = discord.Embed(color = 0x00e600, title = 'Connected players')
    embed1.add_field(name=f"connected player - {len(usersConnected)}:", value="** **", inline=False)
    for i in range(len(usersConnected)):
        embed1.add_field(name=f"`{usersConnected[i]}`", value="** **", inline=True)
    await ctx.send(embed = embed1)
@bot.command()
async def full(ctx):
    embed2 = discord.Embed(color = 0x00e600, title = 'Server Info')
    embed2.add_field(name="Status: online :white_check_mark:", value="** **", inline=False)
    embed2.add_field(name=f"Ip: {nowserver}", value="** **", inline=False)
    embed2.add_field(name=f"Ping: {pingnow}", value="** **", inline=False)
    embed2.add_field(name=f"Players: {len(usersConnected)}", value="** **", inline=False)
    for i in range(len(usersConnected)):
        embed2.add_field(name=f"`{usersConnected[i]}`", value="** **", inline=True)
    await ctx.send(embed = embed2)
@bot.command()
async def snow(ctx):
    await ctx.send("\u2603\u2603\u2603")
@bot.command()    
async def snow2(ctx):
    await ctx.send("`\u2603\u2603\u2603`")
bot.run(settings['token'])