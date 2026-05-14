import discord
from discord.ext import commands
import os
import json
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="apl ", intents=intents)

ARCHIVO = "cartas.json"
POOL_FILE = "pool.json"

# 1. Pool de cartas que pueden salir en claim
# Aquí metes tus cartas propias
pool_cartas = {
    "ejemplo_jugador": {
        "nombre": "Ejemplo Jugador", 
        "posicion": "DC", 
        "rating": 85, 
        "stats": {"VIS": 80, "SHO": 85, "PAS": 82, "DRI": 83, "DEF": 70, "RCH": 75}
    },
    "ejemplo_por": {
        "nombre": "Ejemplo POR", 
        "posicion": "PO", 
        "rating": 87, 
        "stats": {"DIV": 85, "HAN": 88, "KIC": 80, "REF": 86, "SPD": 82, "POS": 87}
    }
}

# Carga el pool si ya existe
if os.path.exists(POOL_FILE):
    with open(POOL_FILE, "r", encoding="utf-8") as f:
        pool_cartas = json.load(f)

# 2. Cartas del usuario
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        cartas = json.load(f)
else:
    cartas = {}

def guardar_cartas():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(cartas, f, indent=4, ensure_ascii=False)

def guardar_pool():
    with open(POOL_FILE, "w", encoding="utf-8") as f:
        json.dump(pool_cartas, f, indent=4, ensure_ascii=False)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def claim(ctx):
    if not pool_cartas:
        await ctx.send("No hay cartas en el pool")
        return
        
    cantidad = random.randint(1, 2)
    cartas_sacadas = random.sample(list(pool_cartas.values()), min(cantidad, len(pool_cartas)))

    texto = f"*{ctx.author.name} sacó {cantidad} carta(s):*\n\n"
    for c in cartas_sacadas:
        key = c["nombre"].lower()
        cartas[key] = c
        texto += f"*{c['nombre']}* | {c['posicion']} | Rating: {c['rating']}\n"

    guardar_cartas()
    await ctx.send(texto)

@bot.command()
async def carta(ctx, *, nombre: str):
    carta = cartas.get(nombre.lower())
    if carta:
        s = carta["stats"]
        if "DIV" in s:
            stats_text = f"DIV: {s['DIV']} | HAN: {s['HAN']} | KIC: {s['KIC']} | REF: {s['REF']} | SPD: {s['SPD']} | POS: {s['POS']}"
        else:
            stats_text = f"VIS: {s['VIS']} | SHO: {s['SHO']} | PAS: {s['PAS']} | DRI: {s['DRI']} | DEF: {s['DEF']} | RCH: {s['RCH']}"
        await ctx.send(f"*{carta['nombre']}* | {carta['posicion']} | Rating: {carta['rating']}\n{stats_text}")
    else:
        await ctx.send("No tienes esa carta. Usa apl cartas para ver las que tienes")

@bot.command()
async def cartas(ctx):
    if not cartas:
        await ctx.send("No tienes cartas aún. Usa apl claim")
    else:
        lista = "\n".join([f"- {c['nombre']} {c['posicion']} {c['rating']}" for c in cartas.values()])
        await ctx.send(f"*Tus cartas:*\n{lista}")

@bot.command()
async def subir(ctx, nombre: str, posicion: str, rating: int, a: int, b: int, c: int, d: int, e: int, f: int):
    # Solo tú puedes subir cartas. Cambia TU_ID por tu ID de Discord
    TU_ID = 1234567890
    if ctx.author.id!= TU_ID:
        await ctx.send("No tienes permiso")
        return

    key = nombre.lower().replace(" ", "_")
    
    if posicion.upper() == "PO":
        stats = {"DIV": a, "HAN": b, "KIC": c

                 import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running')

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server).start(
    

