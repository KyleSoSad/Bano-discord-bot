import discord
from discord.ext import commands

class greeting(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #@commands.Cog.listener()
    #async def on_message(self, message: discord.Message):
    #   await message.add_reaction("✅")

    @commands.command()
    async def hello(self, ctx, *, member):
        await ctx.send(f"hi {member}")

async def setup(bot):
    await bot.add_cog(greeting(bot))