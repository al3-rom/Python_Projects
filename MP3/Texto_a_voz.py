from gtts import gTTS
from main import os

palabras = input("Pon lo que te apetezca: ")

tts = gTTS(text=palabras, lang='es')

tts.save("MP3\Saludo.mp3")
os.system("start MP3\saludo.mp3")

# Simplemente convierte el texto en voz
