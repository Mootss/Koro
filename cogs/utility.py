import discord, time
from discord.ext import commands
from datetime import datetime, timedelta

# some variables 
KoroVersion = "Koro-V0.2.0"
KoroIcon = "https://cdn.discordapp.com/avatars/784747681632485400/e0fc7f04a257b63cd9f745f6831203d2.png?size=1024"

AdminInvite = "https://discord.com/api/oauth2/authorize?client_id=792758878675795978&permissions=8&scope=bot"
BasicInvite = "https://discord.com/api/oauth2/authorize?client_id=792758878675795978&permissions=268823798&scope=bot"



class Utility(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		global StartTime
		StartTime = time.time()
	
	@commands.command(aliases=["commands"]) 
	async def help(self, ctx):
		HelpEmbed = discord.Embed(color=0xFDFD96)
		HelpEmbed.set_author(name="Koro Help Menu", icon_url=KoroIcon)
		HelpEmbed.add_field(name=":camera: Images", 
			value="`cat`\n`goose`\n`kitty`\n`fox`\n`dog`\n`panda`\n`kangaroo`\n`koala`\n`trashpanda`\n`neko`\n`foxgirl`")
		
		HelpEmbed.add_field(name=":grinning: Fun", 
			value="`hug`\n`poke`\n`tickle`\n`feed`\n`baka`\n`pat`\n`smug`\n`cuddle`\n`wink`")
		
		HelpEmbed.add_field(name=":wrench: Utility", 
			value="`ping`\n`stats`\n`help`\n`userinfo`\n`serverinfo`")	

		HelpEmbed.set_footer(text=KoroVersion, icon_url=ctx.message.author.avatar_url)
	
		await ctx.send(embed=HelpEmbed)	
		
	@commands.command(aliases=["pong","latency"])
	async def ping(self, ctx):
		await ctx.send(f'**Pong~!** `{round(self.bot.latency * 1000)}ms` :ping_pong:')

	@commands.command()
	async def invite(self, ctx):
		InviteEmbed = discord.Embed(title="Invite me to your server :D", color=0xFDFD96)
		InviteEmbed.add_field(name="Admin Invite (Recommended)", value=AdminInvite)
		InviteEmbed.add_field(name="Basic permissions Invite", value=BasicInvite)

		InviteEmbed.set_footer(text=KoroVersion, icon_url=ctx.message.author.avatar_url)
		await ctx .send(embed=InviteEmbed)

	@commands.command(aliases=["statistics","status", "s"])
	async def stats(self, ctx):
		StatsEmbed = discord.Embed(title="Koro Stats", color=0xFDFD96)

		CurrentTime = time.time()
		difference = int(round(CurrentTime - StartTime))
		UptimeVal = str(timedelta(seconds=difference))

		StatsEmbed.add_field(name="Servers", value=len(self.bot.guilds))
		StatsEmbed.add_field(name="Uptime", value=UptimeVal)
		StatsEmbed.add_field(name="discord.py version", value=discord.__version__)

		await ctx.send(embed=StatsEmbed)


def setup(bot):
	bot.add_cog(Utility(bot))




