import PyPDF2
from gtts import gTTS
from pydub import AudioSegment
import pygame
import os
from tqdm import tqdm

# Ruta al archivo PDF
ruta_pdf = "tu_archivo.pdf"

# Función para extraer texto de un archivo PDF
def extraer_texto_desde_pdf(ruta_pdf):
    texto = ""
    with open(ruta_pdf, "rb") as archivo_pdf:
        lector_pdf = PyPDF2.PdfReader(archivo_pdf)
        for pagina in lector_pdf.pages:
            texto += pagina.extract_text()
    return texto

# Extraer el texto del PDF
texto_del_pdf = extraer_texto_desde_pdf(ruta_pdf)

# Crear una instancia de gTTS con el texto extraído
tts = gTTS(text=texto_del_pdf, lang='es')

# Guardar el audio en un archivo MP3 en el directorio actual
nombre_archivo = "texto_a_voz.mp3"
tts.save(nombre_archivo)

# Cargar el archivo MP3 con pydub
audio = AudioSegment.from_mp3(nombre_archivo)

# Acelerar la velocidad de reproducción (por ejemplo, duplicar la velocidad)
factor_aceleracion = 1.25  # Puedes ajustar este valor según tus necesidades

# Aplicar el cambio de velocidad
audio_acelerado = audio.speedup(playback_speed=factor_aceleracion)

# Guardar el audio acelerado en un nuevo archivo MP3
nombre_archivo_acelerado = "texto_a_voz_acelerado.mp3"
audio_acelerado.export(nombre_archivo_acelerado, format="mp3")

# Inicializar pygame
pygame.init()

# Cargar el archivo de audio acelerado
pygame.mixer.music.load(nombre_archivo_acelerado)

# Reproducir el audio acelerado
pygame.mixer.music.play()

# Barra de progreso
total_frames = len(audio_acelerado)
for i in tqdm(range(total_frames), desc="Creando archivo MP3"):
    pygame.time.delay(1)

# Esperar a que termine la reproducción
while pygame.mixer.music.get_busy():
    pass

