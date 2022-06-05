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

# ? TEAM MAKER CODE
    teamSeperator = "\n- "

# 2 TEAMS MAKER
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
            is_not_balanced = True
        while is_not_balanced:
            if ((len(team1) > len(team2) + 1) or (len(team2) > len(team1) + 1)) == False:
                is_not_balanced = False
            if(len(team1) > len(team2) + 1):
                random_pop = random.randint(0, len(team1) - 1)
                team2.append(team1[random_pop])
                team1.pop(random_pop)
            elif(len(team2) > len(team1) + 1):
                random_pop = random.randint(0, len(team2) - 1)
                team1.append(team2[random_pop])
                team2.pop(random_pop)

        team1 = teamSeperator.join(sorted(team1))
        team2 = teamSeperator.join(sorted(team2))

        await message.channel.send(f"----- team 1 ----- \n- {team1}\n\n----- team 2: ----- \n- {team2}".title())

# 3 TEAMS MAKER
    if msg.startswith('!teamup3'):
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
            is_not_balanced = True
        while is_not_balanced:
            if ((len(team1) > len(team2) + 1) or len(team1) > len(team3) + 1 or (len(team2) > len(team1) + 1) or (len(team3) > len(team1) + 1) or (len(team3) > len(team2) + 1)) == False:
                is_not_balanced = False
            if(len(team1) > len(team2) + 1):
                random_pop = random.randint(0, len(team1) - 1)
                team2.append(team1[random_pop])
                team1.pop(random_pop)
            elif len(team1) > len(team3) + 1:
                random_pop = random.randint(0, len(team1) - 1)
                team3.append(team1[random_pop])
                team1.pop(random_pop)
            elif len(team2) > len(team3) + 1:
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

        team1 = teamSeperator.join(sorted(team1))
        team2 = teamSeperator.join(sorted(team2))
        team3 = teamSeperator.join(sorted(team3))

        await message.channel.send(f"----- team 1 ----- \n- {team1}\n\n----- team 2 ----- \n- {team2}\n\n----- team 3 ----- \n- {team3}".title())

# 4 TEAMS MAKER
    if msg.startswith('!teamup') and msg.split("!teamup")[1].startswith("4"):
        team1 = []
        team2 = []
        team3 = []
        team4 = []
        msg_content_no_cmd = msg.split("!teamup4 ")[1]
        if "," in msg:
            split_names = msg_content_no_cmd.split(", ")
        else:
            split_names = msg_content_no_cmd.split(" ")
        for name in split_names:
            randomNum = random.randint(0, 3)
            if randomNum == 0:
                team1.append(name)
            elif randomNum == 1:
                team2.append(name)
            elif randomNum == 2:
                team3.append(name)
            elif randomNum == 3:
                team4.append(name)
            is_not_balanced = True
        while is_not_balanced:
            if ((len(team1) > len(team2) + 1) or (len(team1) > len(team3) + 1) or (len(team1) > len(team4) + 1) or (len(team2) > len(team3) + 1) or (len(team2) > len(team1) + 1) or (len(team2) > len(team4) + 1) or (len(team3) > len(team1) + 1) or (len(team3) > len(team2) + 1) or (len(team3) > len(team4) + 1)) == False:
                is_not_balanced = False
            if len(team1) > len(team2) + 1:
                random_pop = random.randint(0, len(team1) - 1)
                team2.append(team1[random_pop])
                team1.pop(random_pop)
            elif len(team1) > len(team3) + 1:
                random_pop = random.randint(0, len(team1) - 1)
                team3.append(team1[random_pop])
                team1.pop(random_pop)
            elif len(team1) > len(team4) + 1:
                random_pop = random.randint(0, len(team1) - 1)
                team4.append(team1[random_pop])
                team1.pop(random_pop)
            elif(len(team2) > len(team1) + 1):
                random_pop = random.randint(0, len(team2) - 1)
                team1.append(team2[random_pop])
                team2.pop(random_pop)
            elif len(team2) > len(team3) + 1:
                random_pop = random.randint(0, len(team2) - 1)
                team3.append(team2[random_pop])
                team2.pop(random_pop)
            elif(len(team2) > len(team4) + 1):
                random_pop = random.randint(0, len(team2) - 1)
                team4.append(team2[random_pop])
                team2.pop(random_pop)
            elif len(team3) > len(team1) + 1:
                random_pop = random.randint(0, len(team3) - 1)
                team1.append(team3[random_pop])
                team3.pop(random_pop)
            elif len(team3) > len(team2) + 1:
                random_pop = random.randint(0, len(team3) - 1)
                team2.append(team3[random_pop])
                team3.pop(random_pop)
            elif len(team3) > len(team4) + 1:
                random_pop = random.randint(0, len(team3) - 1)
                team4.append(team3[random_pop])
                team3.pop(random_pop)
            elif len(team4) > len(team1) + 1:
                random_pop = random.randint(0, len(team4) - 1)
                team1.append(team4[random_pop])
                team4.pop(random_pop)
            elif len(team4) > len(team2) + 1:
                random_pop = random.randint(0, len(team4) - 1)
                team2.append(team4[random_pop])
                team4.pop(random_pop)
            elif len(team4) > len(team3) + 1:
                random_pop = random.randint(0, len(team4) - 1)
                team3.append(team4[random_pop])
                team4.pop(random_pop)

        team1 = teamSeperator.join(sorted(team1))
        team2 = teamSeperator.join(sorted(team2))
        team3 = teamSeperator.join(sorted(team3))
        team4 = teamSeperator.join(sorted(team4))

        await message.channel.send(f"----- team 1 ----- \n- {team1}\n\n----- team 2 ----- \n- {team2}\n\n----- team 3 ----- \n- {team3}\n\n----- team 4 ----- \n- {team4}".title())


# OVERWATCH TEAM MAKER
    if msg.startswith("!ow"):
        rolesAndPlayers = msg.split("!ow ")[1]

        result = []

        tanks = [
            "D.Va",
            "Orisa",
            "Reinhardt",
            "Roadhog",
            "Winston",
            "Wrecking Ball",
            "Zarya",
            "Sigma",
        ]
        dpss = [
            "Ashe",
            "Bastion",
            "Cassidy",
            "Doomfist",
            "Genji",
            "Hanzo",
            "Echo",
            "Junkrat",
            "Mei",
            "Pharah",
            "Reaper",
            "Soldier: 76",
            "Sombra",
            "Symmetra",
            "Torbjorn",
            "Tracer",
            "Widowmaker",
        ]
        supports = [
            "Brigitte",
            "Lucio",
            "Mercy",
            "Moira",
            "Zenyatta",
            "Ana",
            "Baptiste",
        ]

        numTanks = 0
        numDps = 0
        numSup = 0

        availableRoles = ["tank", "tank", "dps", "dps", "sup", "sup"]

        players = rolesAndPlayers.split(" ")
        # random.shuffle(players)

        playersWithoutRole = []

        for player in players:
            person = player.split(":")[0].title()
            if "tank" in player or "dps" in player or "sup" in player:
                role = player.split(":")[1]
                if role == "tank":
                    numTanks += 1
                    chosenTank = tanks[random.randint(0, len(tanks)-1)]
                    result.append(
                        ":small_blue_diamond: " + f"[ {person} ] is playing [ {chosenTank} ] " + ":small_blue_diamond:")
                    tanks.pop(tanks.index(chosenTank))
                    availableRoles.pop(availableRoles.index("tank"))
                    # print(tanks)
                elif role == "dps":
                    numDps += 1
                    chosenDps = dpss[random.randint(0, len(dpss)-1)]
                    result.append(":small_orange_diamond: " + f"[ {person} ] is playing [ {chosenDps} ] " + ":small_orange_diamond: ")
                    dpss.pop(dpss.index(chosenDps))
                    availableRoles.pop(availableRoles.index("dps"))
                    # print(dpss)
                elif role == "sup":
                    numSup += 1
                    chosenSup = supports[random.randint(0, len(supports)-1)]
                    result.append(
                        ":yellow_heart: " + f"[ {person} ] is playing [ {chosenSup} ] " + ":yellow_heart:")
                    supports.pop(supports.index(chosenSup))
                    availableRoles.pop(availableRoles.index("sup"))
                    # print(supports)
            else:
                playersWithoutRole.append(player)

            if player == players[-1]:
                for player in playersWithoutRole:
                    choseAvailableRole = availableRoles[random.randint(
                        0, len(availableRoles)-1)]
                    if choseAvailableRole == "tank":
                        numTanks += 1
                        chosenTank = tanks[random.randint(0, len(tanks)-1)]
                        result.append(
                            ":small_blue_diamond: " + f"[ {player.title()} ] is playing [ {chosenTank} ] " + ":small_blue_diamond:")
                        tanks.pop(tanks.index(chosenTank))
                        availableRoles.pop(availableRoles.index("tank"))
                    elif choseAvailableRole == "dps":
                        numDps += 1
                        chosenDps = dpss[random.randint(0, len(dpss)-1)]
                        result.append(
                            ":small_orange_diamond: " + f"[ {player.title()} ] is playing [ {chosenDps} ] " + ":small_orange_diamond:")
                        dpss.pop(dpss.index(chosenDps))
                        availableRoles.pop(availableRoles.index("dps"))
                    elif choseAvailableRole == "sup":
                        numSup += 1
                        chosenSup = supports[random.randint(
                            0, len(supports)-1)]
                        result.append(
                            ":yellow_heart: " + f"[ {player.title()} ] is playing [ {chosenSup} ] " + ":yellow_heart:")
                        supports.pop(supports.index(chosenSup))
                        availableRoles.pop(availableRoles.index("sup"))

        result = "\n\n".join(sorted(result))

        msgSend = ""

        if len(rolesAndPlayers.split(" ")) > 6:
            msgSend += ":red_circle: Cannot be over 6 players in Overwatch! \n"
        else:
            if(numTanks > 2):
                msgSend += f":red_circle: You have {numTanks - 2} too many tanks in your team! \n"
            if(numDps > 2):
                msgSend += f":red_circle: You have {numDps - 2} too many Dps characters in your team! \n"
            if(numSup > 2):
                msgSend += f":red_circle: You have {numSup - 2}  too many supports in your team! \n"

        if msgSend == "":
            await message.channel.send(result)
        else:
            await message.channel.send(msgSend)

client.run(discord_token)
