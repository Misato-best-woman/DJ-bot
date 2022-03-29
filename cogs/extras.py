import discord
from discord.ext import commands
import math
import random

dababy = ['/extras/dababy.jpeg',
          '/extras/dababy02.jpeg',
          '/extras/dababy03.jpeg',
          '/extras/dababy04.jpeg',
          '/extras/dababy05.jpeg',
          '/extras/dababycar.jpeg',
          '/extras/samuel.jpeg'
          ]


class Extras(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def marco(self, ctx):
        await ctx.send("*Polo!*")

    @commands.command()
    async def marquito(self, ctx):
        await ctx.send("¡Habla bien!")

    @commands.command()
    async def hola(self, ctx):
        await ctx.send("¿Qué quieres?")

    @commands.command()
    async def volao(self, ctx):
        if random.getrandbits(1):
            await ctx.send("Águila. \U0001F985")
        else:
            await ctx.send("Sol. \U0001F31E")

    @commands.command()
    async def general(self, ctx, *, nums=None):
        """Resuelve ecuaciones cuadráticas.
        Dale tres números separados por espacios, por ejemplo: .general 1 1 -2"""
        try:
            if nums is None:
                await ctx.send("No me diste ningún número.")
            else:
                num = map(int, nums.split())
                lista = list(num)
                if len(lista) == 3:
                    a = lista[0]
                    b = lista[1]
                    c = lista[2]

                    raiz = (b**2)-(4*a*c)
                    if raiz < 0:
                        await ctx.send("Dame otros valores porque obtuve un número imaginario en la raiz.")
                    else:
                        x1 = (-b+math.sqrt(raiz))/(2*a)
                        x2 = (-b-math.sqrt(raiz))/(2*a)
                        await ctx.send(f"**X1:** {x1:0.3f}\n**X2:** {x2:0.3f}")
                else:
                    await ctx.send("Tres números y solo tres números acepto.")
        except ValueError:
            await ctx.send("Solo acepto numeros enteros complejos, bb.")

    @commands.command(aliases=['LESSGO'])
    async def lessgo(self, ctx):
        img = random.choice(dababy)

        await ctx.send(file=discord.File(img))

    @commands.command()
    @commands.has_role("Admin")
    async def test(self, ctx):
        """Aquí solo hacemos pruebas.
        Evita spamear el chat, el comando probablemente no te devuelva nada."""
        pass


def setup(client):
    client.add_cog(Extras(client))
