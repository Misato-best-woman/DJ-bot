import discord
from discord.ext import commands
import random

respuestas = ["Simón.",
              "No sé pero te ves deshidratado, ve por agua.",
              "Yes yes en inglés \U0001F1FA\U0001F1F8",
              "Taka taka en japonés \U0001F1EF\U0001F1F5",
              "Wi wi en francés \U0001F1EB\U0001F1F7",
              "Así las cosas deben ser.",
              "Tal vez.",
              "Todo pinta que sí.",
              "Yeah carnal.",
              "Sin duda alguna.",
              "Sí.",
              "La fe es lo último que muere.",
              "***\\*Le da una respuesta vaga\\* ***\n**uwu**",
              "vuelve a intentarlo cuando tenga ganas.",
              "No quiero predecirlo ahora",
              "Chance wey",
              "Nah",
              "No te tocaba Karnal.",
              "Pff...",
              "\U0001F940\U0001F987\U0001F5A4nOoo\U0001F5A4\U0001F987\U0001F940",
              "**¡Jamás!**"
              ]

class Respuestas(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bolita(self, ctx, *, pregunta=''):
        """¡Hazle una pregunta al bot!
        Te puede responder positivamente, negativamente o darte una respuesta vaga.
        úsalo de esta manera: .bolita {aquí tu pregunta}?"""
        if pregunta == '':
            res = ":middle_finger:"
            indice = None
        else:
            res = random.choice(respuestas)
            indice = respuestas.index(res)
        if indice == 26:
            await ctx.send(f"**Haz preguntado:** {pregunta}\n**La respuesta es:** {res}", file=discord.File(
                '/respuestas/jamas.png'))
        else:
            await ctx.send(f"**Haz preguntado:** {pregunta}\n**La respuesta es:** {res}")

def setup(client):
    client.add_cog(Respuestas(client))
