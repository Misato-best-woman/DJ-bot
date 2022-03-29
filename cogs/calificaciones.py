import discord
from discord.ext import commands
import random

good = ['Ayñññ, ten, te regalo este dibujito que hice. \U0001F449\U0001F448\n',
        'A huevo.\n',
        'Un placer.\n'
        ]
good_pics = ['/calificaciones/goodbot/anuel.jpeg',
             '/calificaciones/goodbot/gracias.jpeg',
             '/calificaciones/goodbot/person.jpeg'
             ]


bad = ['Cámara, no me awito. \U0001F63F\n',
       'Ahí tengo a mi alchichicle nomás esperando orden para darte un levantón.\n',
       'Pero hay un Dios que todo lo ve.\n',
       '',
       'Vivimos en una sociedad, ten más cuidado con tus palabras.',
       'Eso está muy efe, como dicen los chavos.'
       ]
bad_pics = ['/calificaciones/badbot/gato.JPG',
            '/calificaciones/badbot/mercenario.JPG',
            '/calificaciones/badbot/mevale.jpeg',
            '/calificaciones/badbot/perrito.jpg',
            '/calificaciones/badbot/sociedad.jpeg',
            '/calificaciones/badbot/valerverga.JPG'
            ]


# def contador(band):
#    if band:
#        archivo = open('/calificaciones/goodContador.txt', 'r+')
#    else:
#        archivo = open('/calificaciones/badContador.txt', 'r+')
#    cont = int(archivo.readline())
#    cont += 1
#    archivo.seek(0)
#    archivo.write(str(cont))
#    archivo.close()


class Calificaciones(commands.Cog):
    def ___init__(self, client):
        self.client = client

    @commands.command()
    async def goodbot(self, ctx):
        """Si el bot se lo ha ganado dale una calificación positiva."""
        frase = random.choice(good)
        indice = good.index(frase)
        await ctx.send(frase, file=discord.File(good_pics[indice]))

    @commands.command()
    async def badbot(self, ctx):
        """Si se lo ha buscado, dale una calificación negativa al bot."""
        frase = random.choice(bad)
        indice = bad.index(frase)
        await ctx.send(frase, file=discord.File(bad_pics[indice]))


def setup(client):
    client.add_cog(Calificaciones(client))
