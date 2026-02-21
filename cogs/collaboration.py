import discord
from discord.ext import commands
import config  # Import for channel restrictions if needed

class CollaborationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="create_poll")
    @commands.has_permissions(administrator=True)  # Restrict to admins for collectives
    async def create_poll(self, ctx, question: str, *options: str):
        """Create a simple poll with reactions. Requires admin permissions."""
        if len(options) < 2 or len(options) > 10:
            await ctx.send("Provide between 2 and 10 options.")
            return
        # Optional: Check consent or channel
        if config.POLL_CHANNEL_ID and ctx.channel.id != config.POLL_CHANNEL_ID:
            await ctx.send("Polls can only be created in the designated channel.")
            return
        embed = discord.Embed(title=question, description="Vote with reactions!", color=discord.Color.blue())
        for i, option in enumerate(options, 1):
            embed.add_field(name=f"Option {i}", value=option, inline=False)
        message = await ctx.send(embed=embed)
        for i in range(1, len(options) + 1):
            await message.add_reaction(f"{i}\u20e3")  # Number reactions (1️⃣, 2️⃣, etc.)

    @commands.command(name="start_thread")
    async def start_thread(self, ctx, name: str):
        """Start a new public thread in the current channel for focused discussions."""
        if not isinstance(ctx.channel, discord.TextChannel):
            await ctx.send("This command can only be used in text channels.")
            return
        thread = await ctx.channel.create_thread(name=name, type=discord.ChannelType.public_thread)
        await thread.send(f"Thread started by {ctx.author.mention} for collective discussion!")
        await ctx.send(f"Thread created: {thread.mention}")

    @commands.Cog.listener()
    async def on_ready(self):
        print("CollaborationCog loaded successfully.")

async def setup(bot):
    await bot.add_cog(CollaborationCog(bot))