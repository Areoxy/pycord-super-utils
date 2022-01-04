from __future__ import annotations

import asyncio
from math import ceil
from typing import TYPE_CHECKING

import discord

if TYPE_CHECKING:
    from datetime import datetime

__all__ = ("generate_embeds", "EmojiError", "PageManager", "ButtonsPageManager")


def generate_embeds(
    list_to_generate,
    title,
    description,
    fields=25,
    color=0xFF0000,
    string_format="{}",
    footer: str = "",
    display_page_in_footer=False,
    timestamp: datetime = discord.Embed.Empty,
    page_format: str = "(Page {}/{})",
):
    num_of_embeds = ceil((len(list_to_generate) + 1) / fields)

    embeds = []

    for i in range(1, num_of_embeds + 1):
        embeds.append(
            discord.Embed(
                title=title
                if display_page_in_footer
                else f"{title} {page_format.format(i, num_of_embeds)}",
                description=description,
                color=color,
                timestamp=timestamp,
            ).set_footer(
                text=f"{footer} {page_format.format(i, num_of_embeds)}"
                if display_page_in_footer
                else footer
            )
        )

    embed_index = 0
    for index, element in enumerate(list_to_generate):
        embeds[embed_index].add_field(
            name=f"**{index + 1}.**", value=string_format.format(element), inline=False
        )

        if (index + 1) % fields == 0:
            embed_index += 1

    return embeds


class ButtonError(Exception):
    pass


class EmojiError(Exception):
    pass


class PageManager:
    __slots__ = ("ctx", "messages", "timeout", "emojis", "public", "index")

    def __init__(self, ctx, messages, timeout=60, emojis=None, public=False, index=0):
        self.ctx = ctx
        self.messages = messages
        self.timeout = timeout
        self.emojis = emojis if emojis is not None else ["⏪", "◀️", "▶️", "⏩"]
        self.public = public
        self.index = index

    async def run(self):
        if len(self.emojis) != 4:
            raise EmojiError(f"Passed {len(self.emojis)} emojis when 4 are needed.")

        self.index = 0 if not -1 < self.index < len(self.messages) else self.index

        message_to_send = self.messages[self.index]
        if isinstance(message_to_send, discord.Embed):
            message = await self.ctx.send(embed=message_to_send)
        else:
            message = await self.ctx.send(message_to_send)

        for emoji in self.emojis:
            await message.add_reaction(emoji)

        while True:
            try:
                reaction, user = await self.ctx.bot.wait_for(
                    "reaction_add",
                    check=lambda x, y: x.message == message,
                    timeout=self.timeout,
                )

                if user.bot:
                    continue

                if user != self.ctx.author and not self.public:
                    continue

            except asyncio.TimeoutError:
                break

            if reaction.emoji == self.emojis[0]:
                self.index = 0

            elif reaction.emoji == self.emojis[1]:
                if self.index > 0:
                    self.index -= 1

            elif reaction.emoji == self.emojis[2]:
                if self.index < len(self.messages) - 1:
                    self.index += 1

            elif reaction.emoji == self.emojis[3]:
                self.index = len(self.messages) - 1

            await message.remove_reaction(reaction.emoji, user)
            message_to_send = self.messages[self.index]

            if isinstance(message_to_send, discord.Embed):
                await message.edit(embed=message_to_send, content=None)
            else:
                await message.edit(content=message_to_send, embed=None)
