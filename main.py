import discord
from discord.ext import commands
from discord import guild

#if hosted_as_repl is set to true, paste token in env with value TOKEN
#if hosted_as_repl is set to false, paste token below
#botID is always required
hosted_as_repl = False
botID = 'bot id here'
token = 'token here'

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(case_insensitive=True, command_prefix="r>",activity= discord.Streaming(name="poppy code", url="https://cloverbrand.xyz"), status=discord.Status.online)
bot.remove_command('help') #disables the built in help command

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} is ready to start chatting!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    if message.webhook_id is not None:
        return 
    
    if message.content.lower().startswith(f'<@{botID}>'):
        webhook = await message.channel.create_webhook(name=message.author.name)
        await webhook.send(str(message.content.replace(f'<@{botID}>','')), username=message.author.name, avatar_url=message.author.avatar_url)
        await message.delete()

        webhooks = await message.channel.webhooks()
        for webhook in webhooks:
                await webhook.delete()
if hosted_as_repl:
    import os
    global TOKEN
    TOKEN = os.environ['TOKEN']
else:
    TOKEN = token
bot.run(TOKEN)