import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! Saya adalah bot {bot.user}!')
    
@bot.command()
async def limbah(ctx):
    await ctx.send(f'Limbah adalah bahan buangan tidak terpakai yang berdampak negatif terhadap masyarakat jika tidak dikelola dengan baik. Air limbah industri maupun rumah tangga (domestik) apabila tidak dikelola dengan baik akan menimbulkan dampak negatif bagi kesehatan.')

@bot.command()
async def jenis_limbah(ctx):
    await ctx.send(f'Kelompok jenis limbah ini dibagi menjadi tiga, yaitu limbah padat, limbah cair, dan limbah gas.')

@bot.command()
async def limbah_padat(ctx):
    with open('image/limbahpadat.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def limbah_cair(ctx):
    with open('image/limbahcair.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def limbah_gas(ctx):
    with open('image/limbahgas.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def cara_memilah(ctx):
    await ctx.send(f'pertama, Menyediakan tempat sampah (karung pemilah) terpilah 3 di rumah kita masing-masing (Organik, Anorganik, Residu). Lalu yang kedua, Memilah sampah sesuai jenisnya (organik, anorganik, residu). Ketiga, Sampah hasil pemilahan yang mempunyai nilai ekonomi disetorkan ke Bank Sampah terdekat atau dibuat kreasi daur ulang. Keempat, Sampah organik dari hasil pemilahan sebaiknya dikelola secara mandiri misal dijadikan pupuk kompos, pakan ternak atau pakan maggot. Kelima, Sampah residu diserahkan ke pengelola sampah untuk dibawa ke TPA. Keenam, Perpanjang usia makanan untuk mengurangi jumlah sampah organik. Ketujuh, Melalukan Zero waste, menyediakan makanan secukupnya jangan berlebihan. Kedelapan, Mengurangi penggunaan plastik sekali pakai.')
    
@bot.command()
async def dampak(ctx):
    await ctx.send(f'Limbah yang dibuang langsung ke lingkungan dapat berdampak negatif apabila terdapat dalam jumlah dan konsentrasi tinggi. Keberadaan limbah yang tidak diolah ini dapat menimbulkan pencemaran tanah, air maupun udara, menyebabkan bau tidak sedap, dapat menjadi sumber penyakit bahkan sumber bencana.')

@bot.command()
async def cara_mengurangi_polusi(ctx):
    await ctx.send(f'Pertama, Memeriksa Kualitas Udara. Kedua, Mengurangi Aktivitas di Luar Ruangan dan Menutup Ventilasi. Ketiga, Menggunakan Masker. Keempat, Menggunakan Penjernih Udara dalam Ruangan. Kelima, Menghindari Asap Rokok dan Sumber Polusi lainnya. Keenam, Melaksanakan Perilaku Hidup Bersih dan Sehat (PHBS)')
    
bot.run("TOKEN MU")
