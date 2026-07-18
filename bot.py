import discord
from discord.ext import commands

from model import predic_image

intents = discord.intents.default()
intents.message_content = True

gol_de_messi_min83 = commands.Bot(command_prefix="/", intents=intents)

#eventos
@gol_de_messi_min83.event
async def on_ready():
    print(f"el bot esta en linea {gol_de_messi_min83.user.name}")


#comandos
@gol_de_messi_min83.command()
async def check(ctx):
    await ctx.send("por favor ingresa una imagen para analizar")

    def verificar(mensaje):
        return mensaje.author == ctx.author and len(mensaje.attachments) > 0
    
    try:
        mensaje = await gol_de_messi_min83.wait_for("mensaje", check = verificar, timeout= 60)
        imagen = mensaje.attachments[0]
        await imagen.save(f"image/{imagen.filename}")
        await ctx.send("imagen recibida y guardada para ser analizada")
        #llamar a la funcion image_predic
        resultado = predic_image(image_path="/img/{imagen.filename}", model_path="keras_model.h5", labels_path="labels.txt")
        await ctx.send(f"la imagen corresponde a:{resultado}")
    except:
        await ctx.send("por favor envia una imagen para analizar, recuerda que tienes 60 segundos")

gol_de_messi_min83.run("token")
    
