import discord
from discord.ext import commands
import aiohttp
from ..utils.database import Database
import config

class SpyTrapCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Trap suspicious commands
        self.db.log_event('spy_probe', str(error), ctx.author.id)
        spy_channel = self.bot.get_channel(config.SPY_LOG_ID)
        await spy_channel.send(f"Spy trap triggered: {ctx.author.name} - {error}")

    @commands.command(name='third_party_optin')
    @commands.has_permissions(administrator=True)
    async def third_party_optin(self, ctx, user_id: int, api_key: str):
        if api_key not in config.APPROVED_THIRD_PARTIES:
            await ctx.send("Invalid third-party key - trap triggered!")
            self.db.log_event('spy_invalid_key', api_key, user_id)
            return
        self.db.set_consent(user_id, True, 'third_party')
        user = await self.bot.fetch_user(user_id)
        await user.send("Consent opted in via third party. Revoke with !optout.")
        consent_channel = self.bot.get_channel(config.CONSENT_CHANNEL_ID)
        await consent_channel.send(f"Opt-in applied for {user.name} via third party.")

    # Webhook for remote third-party signals (setup in Discord server settings)
    # Example: Use aiohttp to handle incoming webhooks in a separate server if needed.