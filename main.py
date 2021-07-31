import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----MAIN-----#

prefix = "!"#you can change token#

#add your token to .env for safe connection

keep_alive()
token = os.getenv("TOKEN")

#-------OTHER--------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help Whisky owo Generator", color=420699, description=f"**{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n\n**{prefix}stopautoOwO**\nstops autoOwO.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/788420527165407243/871026752389021766/standard_15.gif")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('Whisky owo Generator is now **online**')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('owoh')
			print(f"{Fore.GREEN}succefully owoh")
			await asyncio.sleep(15)
			await ctx.send('owo sell all')
			print(f"{Fore.GREEN}succefully sell")
			await ctx.send('owo flip 500')
			print(f"{Fore.GREEN}succefully owo flip 500")
			await asyncio.sleep(10)
			await ctx.send('owo cash')
			print(f"{Fore.GREEN}succefully cash")
			await asyncio.sleep(10)


@bot.command()
async def stopautoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('Whisky OwO generator  is now **offline**')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="ITS WHISKY MAGIC", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}

──────────────────────────────────────────────
░██╗░░░░░░░██╗██╗░░██╗██╗░██████╗██╗░░██╗██╗░░░██╗
░██║░░██╗░░██║██║░░██║██║██╔════╝██║░██╔╝╚██╗░██╔╝
░╚██╗████╗██╔╝███████║██║╚█████╗░█████═╝░░╚████╔╝░
░░████╔═████║░██╔══██║██║░╚═══██╗██╔═██╗░░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║██████╔╝██║░╚██╗░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
──────────────────────────────────────────────{Fore.RED}
   

{Fore.GREEN}

░██╗░░░░░░░██╗██╗░░██╗██╗░██████╗██╗░░██╗██╗░░░██╗
░██║░░██╗░░██║██║░░██║██║██╔════╝██║░██╔╝╚██╗░██╔╝
░╚██╗████╗██╔╝███████║██║╚█████╗░█████═╝░░╚████╔╝░
░░████╔═████║░██╔══██║██║░╚═══██╗██╔═██╗░░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║██████╔╝██║░╚██╗░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

Whisky OwO generator is running!
''')

bot.run(token, bot=False)