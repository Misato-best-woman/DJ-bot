# todo: 1.- Si comando = perreo, reproducir cancion aleatoria de playlist, 2.- A futuro tomar el
#  nombre del usuario que manda el mensaje y llevar la cuenta de puntos positivos y negativos

import os
import time
import discord
from discord.ext import commands
from datetime import date

intents = discord.Intents.default()
intents.members = True

message = """
Te invitamos a pasarte por el **MINISTERIO DE OIDOS SORDOS** para que puedas leer una descripción de los canales así como las reglas del servidor.\n
De igual manera te comento que debes sugerirnos un nuevo rol el cual será de uso exclusivo para ti, puede ser lo que tú quieras ¡yay!\n
Esperamos que tu obligada permanencia voluntaria en este servidor sea de tu agrado.\n\n
_Beep bop, soy un bot._
"""


client = commands.Bot(command_prefix='.', intents=intents)


# *********** Eventos ***********
@client.event
async def on_ready():
    print("Estoy ready.")
    await client.change_presence(activity=discord.Game("Metroid Prime"))


@client.event
async def on_member_join(member):
    channel = client.get_channel(808524213194457110)
    rol = discord.utils.get(member.guild.roles, id=820196062295228416)
    hoy = date.today()
    await member.add_roles(rol)

    if hoy.weekday() == 3:
        await channel.send("**¡¡¡FELIZ JUEVES!!!**", file=discord.File(
            './images/jueves.gif'
        ))
        time.sleep(1)

    await channel.send(f"Saluden todxs al niño nuevo: {member.mention}\n{message}")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No reconozco ese comando, prueba con otro.")


# ***************** Comandos *****************
@client.command()
@commands.has_role("Admin")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    #    path = "./cogs"
    #    for (dirpath, dirnames, filenames) in os.walk(path):
    #        for filename in filenames:
    #            if filename.endswith('.py') and (filename[:-3] == extension):
    #                client.load_extension(f"{dirpath[60:]}.{filename[:-3]}")
    #            else:
    #                await ctx.send("La extension no existe pa.")
    #    # Para cargar cogs dentro de otras carpetas se utiliza el formato cogs.nombre_carpeta.nombre_archivo


@client.command()
@commands.has_role("Admin")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
@commands.has_role("Admin")
async def reload(ctx, extension):
    for file in os.listdir('./cogs'):
        if file.startswith(f'{extension}'):
            client.unload_extension(f'cogs.{extension}')
            client.load_extension(f'cogs.{extension}')


# Estas funciones no me sirven de momento, solo fueron ejemplo
#
# @client.event
# async def on_member_remove(member):
#    print(f"{member} ha sido removido.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Dentro de run() va mi token
with open('secret.txt', 'r') as secret:
    my_token = secret.readline()
client.run(my_token)
