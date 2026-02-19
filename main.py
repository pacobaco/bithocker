import discord
from discord.ext import commands
import config
from cogs.logging import LoggingCog
from cogs.recording import RecordingCog
from cogs.accessibility import AccessibilityCog
from cogs.spytrap import SpyTrapCog

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'BitHocker logged in as {bot.user}')

bot.add_cog(LoggingCog(bot))
bot.add_cog(RecordingCog(bot))
bot.add_cog(AccessibilityCog(bot))
bot.add_cog(SpyTrapCog(bot))

bot.run(config.DISCORD_TOKEN)