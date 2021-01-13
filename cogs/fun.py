import discord, nekos, random, aiohttp
from discord.ext import commands

class Fun(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def hug(self, ctx):
		author = ctx.message.author
		HugEmbed = discord.Embed(color=random.randint(0, 0xFFFFFF))
		HugEmbed.set_image(url=nekos.img("hug"))
		await ctx.send(embed=HugEmbed)


	@commands.command()
	async def poke(self, ctx):
		author = ctx.message.author
		PokeEmbed = discord.Embed(color=random.randint(0, 0xFFFFFF))
		PokeEmbed.set_image(url=nekos.img("poke"))
		await ctx.send(embed=PokeEmbed)


	@commands.command()
	async def tickle(self, ctx):
		TickEmbed = discord.Embed(icon_url=str(ctx.message.author.avatar_url),description=str(ctx.message.author.name) ,color=random.randint(0, 0xFFFFFF))
		TickEmbed.set_image(url=nekos.img("tickle"))
		await ctx.send(embed=TickEmbed)


	@commands.command()
	async def feed(self, ctx):
		FeedEmbed = discord.Embed(color=random.randint(0, 0xFFFFFF))
		FeedEmbed.set_image(url=nekos.img("feed"))
		await ctx.send(embed=FeedEmbed)


	@commands.command(aliases=["aho","bakayaro"])
	async def baka(self, ctx):
		HugEmbed = discord.Embed(color=random.randint(0, 0xFFFFFF))
		HugEmbed.set_image(url=nekos.img("baka"))
		await ctx.send(embed=HugEmbed)


	@commands.command(aliases=["wp"])
	async def wallpaper(self, ctx):
		WallpaperEmbed = discord.Embed(description="wallpaper" ,color=random.randint(0, 0xFFFFFF))
		WallpaperEmbed.set_image(url=nekos.img("wallpaper"))
		await ctx.send(embed=WallpaperEmbed)


	@commands.command()
	async def catgirlgif(self, ctx):
		NgifEmbed = discord.Embed(description="ngif" ,color=random.randint(0, 0xFFFFFF))
		NgifEmbed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=NgifEmbed)


	@commands.command()
	async def pat(self, ctx):
		embed = discord.Embed(color=random.randint(0, 0xFFFFFF)).set_image(url=nekos.img('pat'))
		await ctx.send(embed=embed)


	@commands.command()
	async def smug(self, ctx):
		embed = discord.Embed(color=random.randint(0, 0xFFFFFF)).set_image(url=nekos.img('smug'))
		await ctx.send(embed=embed)


	@commands.command()
	async def cuddle(self, ctx):
		author = ctx.message.author
		embed = discord.Embed(icon_url=str(author.avatar_url), description=author.name,color=random.randint(0, 0xFFFFFF)
			).set_image(url=nekos.img('cuddle'))
		await ctx.send(embed=embed)


	@commands.command(aliases=["wa"])
	async def waifu(self, ctx):
		embed = discord.Embed(color=random.randint(0, 0xFFFFFF)).set_image(url=nekos.img('waifu'))
		await ctx.send(embed=embed)


	@commands.command()
	async def wink(self, ctx):
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://some-random-api.ml/animu/wink') as r:
				res = await r.json()
				imgUrl = res['link']
		PikaEmbed = discord.Embed(title='Wink Wink', color=0xFFFFFF).set_image(url=imgUrl)
		await ctx.send(embed=PikaEmbed)	


def setup(bot):
	bot.add_cog(Fun(bot))