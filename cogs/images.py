import discord, nekos, random
from discord.ext import commands
from animals import Animals

KoroIcon = "https://cdn.discordapp.com/attachments/784738139938750475/793149673212608522/Koro_pfp.png"

class Images(commands.Cog): 
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cat(self, ctx, aliases=["cats","pussy","meow","myeow"]):
		CatImgEmbed = discord.Embed(title=":cat: Myeow!", color=random.randint(0, 0xFFFFFF))
		CatImgEmbed.set_image(url=nekos.cat())
		await ctx.send(embed=CatImgEmbed)

	@commands.command()
	async def goose(self, ctx, aliases=["geese", "honk"]):
		goose='https://cdn.discordapp.com/emojis/792455524762648604.png?v=1'
		GooseImgEmbed = discord.Embed(icon_url=goose ,title="Honk!", color=random.randint(0, 0xFFFFFF))
		GooseImgEmbed.set_image(url=nekos.img("goose"))
		await ctx.send(embed=GooseImgEmbed)

	@commands.command()
	async def dog(self, ctx):
		dog = Animals('dog')
		DogImgEmbed = discord.Embed(title=":dog: Woof!", description=str(dog.fact()) , color=random.randint(0, 0xFFFFFF))
		DogImgEmbed.set_image(url=dog.image())
		await ctx.send(embed=DogImgEmbed)


	@commands.command(aliases=["racoon"])
	async def trashpanda(self, ctx):
		racoon = Animals("racoon")
		RacoonImgEmbed = discord.Embed(title="issa racoon!", description=str(racoon.fact()) , color=random.randint(0, 0xFFFFFF))
		RacoonImgEmbed.set_image(url=racoon.image())
		await ctx.send(embed=RacoonImgEmbed)


	@commands.command()
	async def panda(self, ctx):
		panda = Animals("panda")
		PandaImgEmbed = discord.Embed(title=":panda:",description=str(panda.fact()) , color=random.randint(0, 0xFFFFFF)) 
		PandaImgEmbed.set_image(url=panda.image())
		await ctx.send(embed=PandaImgEmbed)


	@commands.command()
	async def fox(self, ctx):
		fox = Animals("fox")
		FoxImgEmbed = discord.Embed(title=":fox:", description=str(fox.fact()) ,color=random.randint(0, 0xFFFFFF))
		FoxImgEmbed.set_image(url=fox.image())
		await ctx.send(embed=FoxImgEmbed)


	@commands.command()
	async def koala(self, ctx):
		koala = Animals("koala")
		KoalaImgEmbed = discord.Embed(title=":koala:", description=str(koala.fact()) ,color=random.randint(0, 0xFFFFFF))
		KoalaImgEmbed.set_image(url=koala.image())
		await ctx.send(embed=KoalaImgEmbed)


	@commands.command(aliases=["kitten","kittens","kitties","nyan"])
	async def kitty(self, ctx):
		kitty = Animals("cat")
		KatImgEmbed = discord.Embed(title=":cat: Nyan~!", description=str(kitty.fact()) , color=random.randint(0, 0xFFFFFF))
		KatImgEmbed.set_image(url=kitty.image())
		await ctx.send(embed=KatImgEmbed)


	@commands.command()
	async def kangaroo(self, ctx):
		kangaroo = Animals("kangaroo")
		KangarooImgEmbed = discord.Embed(title=":kangaroo:", description=str(kangaroo.fact()) , color=random.randint(0, 0xFFFFFF))
		KangarooImgEmbed.set_image(url=kangaroo.image())
		await ctx.send(embed=KangarooImgEmbed)


	@commands.command(aliases=["neko"])
	async def catgirl(self, ctx):
		CatGirlEmbed = discord.Embed(title="Nyan~!", color=random.randint(0, 0xFFFFFF))
		CatGirlEmbed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=CatGirlEmbed)


	@commands.command(aliases=["fox girls", "foxxygirls","foxxy girls","foxgirls", "fg"])
	async def foxgirl(self, ctx):
		FoxGirlEmbed = discord.Embed(title="kawaii deshouuuu!", color=random.randint(0, 0xFFFFFF))
		FoxGirlEmbed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=FoxGirlEmbed)

	@commands.command()
	async def daily_dose_of_catgirls(self, ctx):
		embed = discord.Embed(title="Aight here yer daily dose of cat grills", color=random.randint(0, 0xFFFFFF))
		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)


		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)

		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)

		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)

		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)

		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)

		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)

		embed.set_image(url=nekos.img("neko"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("fox_girl"))
		await ctx.send(embed=embed)
		embed.set_image(url=nekos.img("ngif"))
		await ctx.send(embed=embed)



def setup(bot):
	bot.add_cog(Images(bot))


