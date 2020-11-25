from mcstatus import MinecraftServer
from servername import name
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
st = {
    "line": serveronline,
    "usersConnected": usersConnected,
    "pingnow": pingnow
}