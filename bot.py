#se importan librerias
import discord
from discord.ext import commands
#se importa el archivo model junto con la función que se va a usar 
from model import predic_image
#se configuran los permisos y las intenciones del bot
intents = discord.intents.default()
intents.message_content = True
#se le da nombre al bot
gol_de_messi_min83 = commands.Bot(command_prefix="/", intents=intents)

#evento que verifica que el bot este en linea en el servidor 
@gol_de_messi_min83.event
async def on_ready():
    print(f"el bot esta en linea {gol_de_messi_min83.user.name}")


#comandos
@gol_de_messi_min83.command()
async def check(ctx):
    await ctx.send("por favor ingresa una imagen para analizar")
    #verifica que la imagen enviada sea del mismo usuari que se comunico inicialmente con el bot 
    def verificar(mensaje):
        return mensaje.author == ctx.author and len(mensaje.attachments) > 0
    #espera que la imagen sea enviada para analizarla 
    try:
        mensaje = await gol_de_messi_min83.wait_for("mensaje", check = verificar, timeout= 60)
        imagen = mensaje.attachments[0]
        #guarda la imagen con el nombre de imagen.filename en la carpeta de image
        await imagen.save(f"image/{imagen.filename}")
        #responde al ususario y le pide tiempo mientras se procesa la imagen
        await ctx.send("imagen recibida y guardada para ser analizada")
        #llamar a la funcion image_predic para que se traiga el producto de la imagen para dar una devolución
        resultado = predic_image(image_path="/img/{imagen.filename}", model_path="keras_model.h5", labels_path="labels.txt")
        await ctx.send(f"la imagen corresponde a:{resultado}")
    except:
        #el bot respondera esto en caso de que no haya podido recibir la imagen
        await ctx.send("por favor envia una imagen para analizar, recuerda que tienes 60 segundos")

gol_de_messi_min83.run("token")
    
