import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

discord_token = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("WE HAVE LOGGED IN AS {0.user}".format(client))


@client.event
async def on_message(message):
    # message.author is the user who send a message while client.user is the bot
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!teamup'):
        team1 = []
        team2 = []
        msg_content_no_cmd = msg.split("!teamup ")[1]
        if "," in msg: 
            split_names = msg_content_no_cmd.split(", ")
        else: 
            split_names = msg_content_no_cmd.split(" ")
        for name in split_names:
            if(random.randint(0, 1)):
                team1.append(name)
            else:
                team2.append(name)
        for teammate in team1: 
            if(len(team1) > len(team2) + 1): 
                random_pop = random.randint(0, len(team1) - 1)
                team2.append(team1[random_pop])
                team1.pop(random_pop)
            elif(len(team2) > len(team1) + 1): 
                random_pop = random.randint(0, len(team2) - 1)
                team1.append(team2[random_pop])
                team2.pop(random_pop)

        await message.channel.send(f"team 1: {team1}")
        await message.channel.send(f"team 2: {team2}")



client.run(discord_token)
