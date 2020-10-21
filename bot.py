import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    print(client.users)
    #for user in client.users:
    #    print(user)
    #print(client.get_user(335772228643979285))
    print(client.get_user(768242287254831129))
    # print(await client.fetch_user(768242287254831129))
    myUser = client.get_user(304262449627136000)
    print(myUser)
    print(client.get_user(768206444176474132))

    #print(client.guilds)
    #print(guild.members)

    #members = '\n - '.join([member.name for member in guild.members])
    members = [member for member in client.get_all_members() if not member.bot]
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    """
    If bot write something to chat ignore that
    """
    if message.author == client.user:
        return

    print('Author of the message is \'{}\'\n{}'.format(message.author.name, message.author.id))
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if "gif" in message.content.lower():
        await message.channel.send(file=discord.File('math.gif'))

    # Say hi to author of the message
    if "hi" == message.content.lower():
        if message.author.dm_channel == None:
            await message.author.create_dm()
        print(message.author.dm_channel)
        await message.author.dm_channel.send('hell.o')


client.run(TOKEN)
