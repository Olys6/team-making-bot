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

    if msg.startswith('!teamup') and (msg.split("!teamup")[1].startswith(" ") or msg.split("!teamup")[1].startswith("2")):
        team1 = []
        team2 = []
        if(msg.split("!teamup")[1].startswith(" ")):
            msg_content_no_cmd = msg.split("!teamup ")[1]
        elif(msg.split("!teamup")[1].startswith("2")):
            msg_content_no_cmd = msg.split("!teamup2 ")[1]
        if "," in msg: 
            split_names = msg_content_no_cmd.split(", ")
        else: 
            split_names = msg_content_no_cmd.split(" ")
        for name in split_names:
            if(random.randint(0, 1)):
                team1.append(name)
            else:
                team2.append(name)
        for teammate in split_names: 
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

    if msg.startswith('!teamup') and msg.split("!teamup")[1].startswith("3"):
        team1 = []
        team2 = []
        team3 = []
        msg_content_no_cmd = msg.split("!teamup3 ")[1]
        if "," in msg:
            split_names = msg_content_no_cmd.split(", ")
        else:
            split_names = msg_content_no_cmd.split(" ")
        for name in split_names:
            randomNum = random.randint(0, 2)
            if randomNum == 0:
                team1.append(name)
            elif randomNum == 1:
                team2.append(name)
            else:
                team3.append(name)
        for teammate in split_names:
            if(len(team1) > len(team2) + 1):
                random_pop = random.randint(0, len(team1) - 1)
                team2.append(team1[random_pop])
                team1.pop(random_pop)
            elif len(team1) > len(team3) + 1:
                random_pop = random.randint(0, len(team1) - 1)
                team3.append(team1[random_pop])
                team1.pop(random_pop)
            elif len(team2) > len(team3) +1:
                random_pop = random.randint(0, len(team3) - 1)
                team2.append(team3[random_pop])
                team3.pop(random_pop)
            elif(len(team2) > len(team1) + 1):
                random_pop = random.randint(0, len(team2) - 1)
                team1.append(team2[random_pop])
                team2.pop(random_pop)
            elif len(team3) > len(team1) + 1:
                random_pop = random.randint(0, len(team3) - 1)
                team1.append(team3[random_pop])
                team3.pop(random_pop)
            elif len(team3) > len(team2) + 1:
                random_pop = random.randint(0, len(team3) - 1)
                team2.append(team3[random_pop])
                team3.pop(random_pop)

        await message.channel.send(f"team 1: {team1}")
        await message.channel.send(f"team 2: {team2}")
        await message.channel.send(f"team 3: {team3}")



client.run(discord_token)
