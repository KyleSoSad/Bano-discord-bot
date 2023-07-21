from discord.ext import commands

@commands.group()       
async def tính(ctx):
        if ctx.invoked_subcommand is None:
           await ctx.send(f"Không, {ctx.subcommand_passed} đây không phải là 1 bài toán")

@tính.command()
async def cộng(ctx, one : int  , two : int ):
    await ctx.send(one + two)

@tính.command()       
async def trừ(ctx, one: int, two: int) :
        await ctx.send(f"Kết quả là {one - two}")

@tính.command()       
async def nhân(ctx, one: int, two: int):
        await ctx.send(f"Kết quả là {one * two}")

@tính.command()       
async def chia(ctx, one: int, two: int):
        await ctx.send(f"Kết quả là {one / two}")
    
async def setup(bot):
    bot.add_command(tính)
    bot.add_command(cộng)
    bot.add_command(trừ)
    bot.add_command(nhân)
    bot.add_command(chia)