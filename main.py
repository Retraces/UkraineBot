import discord
import os
from discord.ext.commands import Bot
from libraries import tgnews,tgtime

activity = discord.Game(name="!commands")
client = Bot(command_prefix="!", activity=activity, status=discord.Status.online,help_command=None,case_insensitive=True)


@client.command()
async def donate(ctx):
    donate=discord.Embed(title="How to support the Ukrainian People! :flag_ua:", url="https://savelife.in.ua/en/donate/", description="Different ways to donate", color=0xFFFF00)
    donate.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/800px-Flag_of_Ukraine.svg.png")
    donate.add_field(name="Cryptocurrency", value="BTC — 357a3So9CbsNfBBgFYACGvxxS6tMaDoa1P\nETH — 0x165CD37b4C644C2921454429E7F9358d18A45e14\nUSDT (trc20) — TEFccmfQ38cZS1DTZVhsxKVDckA8Y6VfCy", inline=True)
    donate.add_field(name="Websites :flag_ua:", value="https://savelife.in.ua/en/donate\nhttps://donatenow.wfp.org/ukraine-appeal/", inline=True)
    donate.set_footer(text="Glory to Ukraine!")
    await ctx.send(embed=donate)

@client.command()
async def commands(ctx):
    commands=discord.Embed(title="Commands :flag_ua:", description="Various commands available:", color=0xFFFF00)
    commands.add_field(name="**Commands**", value="**!donate** - Ways to donate to the Ukrainian people\n**!commands** - This.\n**!news** - Provides the latest message from UkraineNOW, a trusted news source\n**!sources** - List of reliable sources", inline=True)
    commands.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Outline_of_Ukraine.svg/1200px-Outline_of_Ukraine.svg.png")
    commands.set_footer(text="Glory to Ukraine!")
    await ctx.send(embed=commands)

@client.command()
async def news(ctx):
    news=discord.Embed(title="Latest news from UkraineNOW :flag_ua:", description="https://t.me/ukrainenowenglish:", color=0xFFFF00)
    news.add_field(name="**News**", value=tgnews(), inline=True)
    news.set_thumbnail(url="https://cdn4.telesco.pe/file/nomsgLLU2J0A8VmU5KJs1BfrtimS1uGuTrw2LbDwe5QddqWgNmcZknotLBqLoFtL2Sa4zWSQkFSp37Mcjj0F9d1AFBBySuywOq8CqblqkeuwQ4HMphOfaEVJq2Iu4MjTiu2tsqDybh0xO67HNHplRsoXHd1k1iHVUkTW9gAnm14H3tBqsh0cFmwa7VEZSSJLzv1rXiVHYtGoimt2tMSrzdxQub0BXG8Rqt7919t8SEcc_EWeHbYGghZ2QrepB2EiULFjlcgeCK6bFPY86GPlr2x0EuFZJiU6mLvsuI4iIaN_FNHAll2Hd6cnhKSRmXklYsNmgkiRe5sMc0iAIB-9mQ.jpg")
    news.set_footer(text=f"Posted at {tgtime()} UTC")
    await ctx.send(embed=news)

@client.command()
async def sources(ctx):
        sources=discord.Embed(title="Trusted Sources :flag_ua:", description="Sources found to be accurate, subject to change at any moment!", color=0xFFFF00)
        sources.add_field(name="Trusted Sources:", value="[Ukraine.ua](https://war.ukraine.ua/)\n[UkraineNOW](https://t.me/s/ukrainenow)\n[UkraineNOW (EN)](https://t.me/s/ukrainenowenglish)\n[Zelenskiy / Official](https://t.me/s/V_Zelenskiy_official)", inline=True)
        sources.set_footer(text="Glory to Ukraine!")
        await ctx.send(embed=sources)
  
client.run(os.getenv('TOKEN'))
