from discord.ext.commands import Bot
import random
import requests
import json

BOTPREFIX = ("?", "!")
TOKEN = "NTEwMzQ2MDE0MDk2NjIxNTg5.DsbA6w.mlLwpxVQ3_RgZ2ZKbgEqHrBBR7Q"

client = Bot(command_prefix=BOTPREFIX)


@client.command(name="insult", pass_context = True)
async def insults(context):
    possibleInsults = [
        "You are dumb",
        "You suck",
        "Youre terrible at this game"
    ]

    await client.say(str(context.message) + ", " + random.choice(possibleInsults))


@client.command(name="gif", pass_context = True)
async def gif(context):
    message = context.message.content
    messageToPass = message[4:]

    apikey = "NQAQHOC74ITL"  # test value
    lmt = 25

    # load the user's anonymous ID from cookies or some other disk storage
    # anon_id = <from db/cookies>

    # ELSE - first time user, grab and store their the anonymous ID
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

    if r.status_code == 200:
        anon_id = json.loads(r.content)["anon_id"]
        # store in db/cookies for re-use later
    else:
        anon_id = ""

    # our test search

    # get random results using default locale of EN_US
    r = requests.get(
        "https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s&anon_id=%s" % (messageToPass, apikey, lmt, anon_id))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        print(gifs['results'][0]['url'])
    else:
        gifs = None

    await client.say(gifs['results'][0]['url'])


client.run(TOKEN)