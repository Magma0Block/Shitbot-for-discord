import random
import time
from random import randint
import discord
import discord.ext
from discord.ext import commands
import Token


def send_embed(title, member_name, action, channel):
    data = discord.Embed(
        title=title,
        description=f'{member_name} {action} {channel}',
        color=6094592,
    )
    return data


def main():
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    server_list = [624500639149588488]
    servers_voice_users_dict = {}
    nicknames = list(
        ["ЕБЛАН СНИЗУ", "ЕБЛАН СВЕРХУ", "ЕБЛАН ПОСЕРЕДИНЕ", "ЕБАНАТ", "ОБСОС", "ХУЕСОС", "БЛЯДУНЬЯ", "ПИДОРАС СНИЗУ",
         "ПИДОРАС ПОСЕРЕДИНЕ", "ПИДОРАС СВЕРХУ", "ПЕДИК", "ЖЕНЩИНА", "ЧУРКА", "КОЗОЕБ", "УЕБАН", "МУДАК", "ПЕТУХ",
         "ПИЗДОПРОЁБИЩЕ", "ЕВНУХ", "БЛЯДИНКА", "МАМОЁБ", "СОСУОТЦУ", "СПЕРМОЕД", "Игрок в лигу легенд", "ЕБАНИНА",
         "ТАДЖИК", "УЕБИЩЕ КОНЧЕНОЕ", "КОНЧЕНЫЙ", "ТАНКОЕБ", "Игрок в Геншин", "ПЕДОФИЛ", "ЗООФИЛ"])
    pinus_list = list(
        ["https://tenor.com/view/dragon-tale-dragon-covered-fell-down-here-gif-5524123",
         "https://media1.tenor.com/m/LqNVoPJu_cIAAAAd/dick.gif",
         "https://media1.tenor.com/m/28FCoR51U5AAAAAC/peen-meat.gif",
         "https://media1.tenor.com/m/7CZPqlmnRt4AAAAd/katzen-schwanz.gif",
         "https://media1.tenor.com/m/ZK1ZegeT9gYAAAAC/dick-penis.gif",
         "https://media1.tenor.com/m/4cwHkZkFtEYAAAAd/genshin-impact-true.gif"]
    )

    @client.event
    async def on_ready():
        await client.tree.sync(guild=discord.Object(id=601446482192629781))
        client.tree.copy_global_to(guild=discord.Object(id=601446482192629781))
        print("Бот готов к работе! Ожидание взаимодействия")

    @client.tree.command(name="send_pinus", description="8====3")
    async def send_pinus(interaction: discord.Interaction):
        # noinspection PyUnresolvedReferences
        gif = pinus_list[randint(0, len(pinus_list))]
        await interaction.response.send_message(gif, ephemeral=True)

    @client.event
    async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        info_output_channel = client.get_channel(1190273841201692723)
        if 1:
            try:
                if before.channel is None:
                    try:
                        servers_voice_users_dict[after.channel.guild].add(member)
                        data = send_embed(member.guild.name, member.name, 'зашел в войс', after.channel)
                        await info_output_channel.send(embed=data)
                    except KeyError:
                        servers_voice_users_dict[after.channel.guild] = set()
                        servers_voice_users_dict[after.channel.guild].add(member)
                        if after.channel.guild.id in server_list:
                            data = send_embed(member.guild.name, member.name, 'зашел в войс', after.channel)
                            await info_output_channel.send(embed=data)

                if after.channel is None:
                    servers_voice_users_dict[before.channel.guild].remove(member)
                    # servers_voice_users_dict.remove(member)
                    data = send_embed(member.guild.name, member.name, 'вышел из войса', before.channel)
                    if before.channel.guild.id in server_list:
                        await info_output_channel.send(embed=data)
                        if not servers_voice_users_dict:
                            data = send_embed(member.guild.name, None, 'Все вышли из войса', None)
                            await info_output_channel.send(embed=data)
            except KeyError:
                print(f"Из голосового канала {before.channel} на сервере {member.guild.name} вышли все")

    @client.tree.command(name='срать', description="Бот начинает тотальный обсер. Остановить НЕВОЗМОЖНО")
    async def poop(interaction: discord.Interaction):
        await interaction.response.send_message("ПРИШЛО ВРЕМЯ КАКАТЬ")
        while True:
            await interaction.channel.send('https://media1.tenor.com/m/2y0fwDpQ6sIAAAAC/poop-shit.gif')
            time.sleep(0.5)

    @client.command()
    async def срать(ctx):
        await ctx.channel.send("ПРИШЛО ВРЕМЯ КАКАТЬ")
        while True:
            await ctx.channel.send('https://media1.tenor.com/m/2y0fwDpQ6sIAAAAC/poop-shit.gif')
            time.sleep(0.5)

    # noinspection PyUnresolvedReferences
    @client.tree.command(name='sync', description='Owner only')
    async def sync(interaction: discord.Interaction):
        if interaction.user.id == 234214064107159552:
            await client.tree.sync()
            await interaction.response.send_message('Command tree synced.')
        else:
            await interaction.response.send_message('You must be the owner to use this command!')

    @client.tree.command(name='begin_spanking', description="Начинает настоящий Spanking. Невозможно остановить")
    async def begin_spanking(interaction: discord.Interaction):
        respond_message = discord.Embed(
            title=f"Spanking initialized",
            colour=discord.Colour.orange()
        )

        respond_message.set_image(url='https://media1.tenor.com/m/Z0A3V-aC7T8AAAAC/gachi.gif')
        await interaction.response.send_message(embed=respond_message)
        try:
            while True:
                for x in servers_voice_users_dict[interaction.guild]:
                    i = randint(0, len(nicknames) - 1)
                    print(i)
                    try:
                        await x.edit(nick=nicknames[i])
                    except discord.errors.Forbidden:
                        print(f"У пользователя {x.global_name} админ права")
                    print(nicknames[i])
                    time.sleep(2)
        except RuntimeError:
            print("Все вышли из голосового канала")

    @client.command()
    async def gay(ctx):
        await ctx.send(servers_voice_users_dict)
        print(len(nicknames))

    @client.tree.command(name="info", description="Отаправляет ваш IP адрес, а также данные кредитной карты шлакоблоку")
    async def info(interaction: discord.Interaction):
        await interaction.response.send_message("Отправлено в нужный канал")
        info_output_channel = client.get_channel(1190273841201692723)
        for x, y in servers_voice_users_dict.items():
            output_string = '\n'.join(j.name for j in y)
            await info_output_channel.send(embed=discord.Embed(
                title=f"В голосовом канале на сервере {x}",
                description=f"{output_string}",
                colour=discord.Colour.orange()
            ))

    @client.tree.context_menu(name="Показывает IP адрес пользователя")
    async def show_ip(interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"{member.global_name} IP = {randint(0, 191)}:{randint(128, 191)}:"
                                                f"{randint(0, 191)}:{randint(128, 191)}", ephemeral=True)

    client.run(Token.token)

if __name__ == "__main__":
    main()
