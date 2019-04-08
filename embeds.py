import discord
import datetime

def add_embed_footer(embed):
    embed.set_footer(
        text="Scheduler bot by blairg23 | " + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S"),
        icon_url="https://cdn.discordapp.com/avatars/564547605716271114/fa9bbe6f5f35ce9c9953a29c02786728.png",
    )


def Info(title, description):
    embed = discord.Embed(title=":information_source: " + title, description=description, color=0x007BFF)
    add_embed_footer(embed)
    return embed


def Success(title, description):
    embed = discord.Embed(title=":white_check_mark: " + title, description=description, color=0x28A745)
    add_embed_footer(embed)
    return embed


def Error(title, description):
    embed = discord.Embed(title=":x: " + title, description=description, color=0xDC3545)
    add_embed_footer(embed)
    return embed