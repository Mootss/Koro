# Owner : Moots (Moots#1239)
# Koro-V0.2.0

import keep_alive
import discord
from discord.ext import commands
from os import listdir, path, environ

Prefixes = ["..", "//", "koro", "Koro"]
bot = commands.Bot(command_prefix=Prefixes, case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
	print("Koro Tester is online~!")
	await bot.change_presence(activity=discord.Game(name="..help | Testing Koro"))


# only users in this list will have access to these commands, which is ofc myself only 
AllowedUsers = ["688374144294977659"]
#                   Moots#1239

@bot.command(aliases=['lo'])
async def load(ctx, cog):
	if str(ctx.message.author.id) in AllowedUsers: # checks if the user has access to this command
		try: # a try except to catch common errors
			bot.load_extension(f"cogs.{cog}")
			LoadEmbed = discord.Embed(title=":white_check_mark: Success~!", description=f"`{cog}` module loaded" ,color=0xFFFFFF)
			await ctx.send(embed=LoadEmbed)

		except commands.ExtensionAlreadyLoaded:
			AlrLoadedEmbed = discord.Embed(title=f":grey_exclamation: `{cog}` module is already loaded", color=0xFFFFFF)
			await ctx.send(embed=AlrLoadedEmbed)

		except commands.ExtensionNotFound:
			NotFoundEmbed = discord.Embed(title=f":exclamation: could not find `{cog}` module", color=0xFFFFFF)
			await ctx.send(embed=NotFoundEmbed)

	elif str(ctx.message.author.id) not in AllowedUsers:
		NoPermsEmbed = discord.Embed(title=":x: Error", description="You do not have the permission to use this command" ,color=0xFFFFFF)
		await ctx.send(embed=NoPermsEmbed)


@bot.command(aliases=["un"])
async def unload(ctx, cog):
	if str(ctx.message.author.id) in AllowedUsers:
		try:
			bot.unload_extension(f"cogs.{cog}")
			UnloadEmbed = discord.Embed(title=":white_check_mark: Success~!", description=f"`{cog}` module unloaded" ,color=0xFFFFFF)
			await ctx.send(embed=UnloadEmbed)

		except commands.ExtensionNotLoaded:
			AlrUnloadedEmbed = discord.Embed(title=f":grey_exclamation: `{cog}` module is already unloaded", color=0xFFFFFF)
			await ctx.send(embed=AlrUnloadedEmbed)

		except commands.ExtensionNotFound:
			NotFoundEmbed = discord.Embed(title=f":exclamation: could not find `{cog}` module", color=0xFFFFFF)
			await ctx.send(embed=NotFoundEmbed)

	elif str(ctx.message.author.id) not in AllowedUsers:
		NoPermsEmbed = discord.Embed(title=":x: Error", description="You do not have the permission to use this command" ,color=0xFFFFFF)
		await ctx.send(embed=NoPermsEmbed)


@bot.command(aliases=["re"])
async def reload(ctx, cog):
	if str(ctx.message.author.id) in AllowedUsers:
		try:
			bot.reload_extension(f"cogs.{cog}")
			UnloadEmbed = discord.Embed(title=":white_check_mark: Success~!", description=f"`{cog}` module reloaded" ,color=0xFFFFFF)
			await ctx.send(embed=UnloadEmbed)

		except commands.ExtensionNotFound:
			NotFoundEmbed = discord.Embed(title=f":exclamation: could not find `{cog}` module", color=0xFFFFFF)
			await ctx.send(embed=NotFoundEmbed)
		
		except commands.ExtensionNotLoaded:
			NotLoadedEmbed = discord.Embed(title=":x:", description=f'`{cog}` module has not been loaded yet')
			await ctx.send(embed=NotLoadedEmbed)

	elif str(ctx.message.author.id) not in AllowedUsers:
		NoPermsEmbed = discord.Embed(title=":x: Error", description="You do not have the permission to use this command" ,color=0xFFFFFF)
		await ctx.send(embed=NoPermsEmbed)


@bot.command(aliases=["cl"])
async def close(ctx):
	if str(ctx.message.author.id) in AllowedUsers:
		CloseEmbed = discord.Embed(title=":wave: connection closed", color=0xFFFFFF)
		await ctx.send(embed=CloseEmbed)
		await bot.close()

	elif str(ctx.message.author.id) not in AllowedUsers:
		FailedCloseEmbed = discord.Embed(title=":x: Error",description="You cannot use this command", color=0xFFFFFF)
		await ctx.send(embed=FailedCloseEmbed)

@bot.command(aliases=["cogs", "show cogs", "modules", "show modules"])
async def show_cogs(ctx):
	if str(ctx.message.author.id) in AllowedUsers:
		ShowCogsEmbed = discord.Embed(title="Available Cogs", color=0xFFFFFF)
		for filename in listdir("./cogs"):
			if filename.endswith(".py"):
				''' simple try except to check if a cog is loaded or not and returns the status'''
				CogSize = path.getsize("./cogs/"+filename)
				try:
				    bot.load_extension(f"cogs.{filename[:-3]}")
				except commands.ExtensionAlreadyLoaded:
				    CogStatus = ":green_circle: loaded"
				else:
				    CogStatus = ":red_circle: unloaded"
				    bot.unload_extension(f"cogs.{filename[:-3]}")

				ShowCogsEmbed.add_field(name=f'{filename}',value=CogStatus+" - "+f'`{round(CogSize / 1000, 1)} KB`',inline=False)
		await ctx.send(embed=ShowCogsEmbed)

	elif str(ctx.message.author.id) not in AllowedUsers:
		NoPermsEmbed = discord.Embed(title=":x: Error", description="You cannot use this command" ,color=0xFFFFFF)
		await ctx.send(embed=NoPermsEmbed)


for filename in listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")


keep_alive.keep_alive()
token = environ.get("Token")
bot.run(token)
