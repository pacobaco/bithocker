import discord
from discord.ext import commands
from ..utils.database import Database

class LoggingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and self.db.get_consent(message.author.id):
            self.db.log_event('message', message.content, message.author.id)
            log_channel = self.bot.get_channel(config.LOG_CHANNEL_ID)
            await log_channel.send(f"Logged: {message.author.name}: {message.content}")

    @commands.command(name='usage')
    async def usage_stats(self, ctx):
        # Stub: Fetch from DB or Discord stats
        await ctx.send("Usage stats: Placeholder - e.g., online time tracked.")

# Add more for edits/deletes