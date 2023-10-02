from gtts import gTTS
import pygame

# Texto que deseas convertir en voz
texto_a_convertir = "¿Puedes hacer este programa bien de una maldita vez?"

# Crear una instancia de gTTS con el texto
tts = gTTS(text=texto_a_convertir, lang='es')

# Guardar el audio en un archivo MP3 en el directorio actual
nombre_archivo = "texto_a_voz.mp3"
tts.save(nombre_archivo)

# Inicializar pygame
pygame.init()

# Cargar el archivo de audio
pygame.mixer.music.load(nombre_archivo)

# Reproducir el audio
pygame.mixer.music.play()

# Esperar a que termine la reproducción
while pygame.mixer.music.get_busy():
    pass



###########################3


from pydub import AudioSegment
import os

# Ruta al archivo MP3 original
archivo_original = "texto_a_voz.mp3"

# Cargar el archivo MP3 con pydub
audio = AudioSegment.from_mp3(archivo_original)

# Acelerar la velocidad de reproducción (por ejemplo, duplicar la velocidad)
factor_aceleracion = 1.25  # Puedes ajustar este valor según tus necesidades

# Aplicar el cambio de velocidad
audio_acelerado = audio.speedup(playback_speed=factor_aceleracion)

# Guardar el audio acelerado en un nuevo archivo MP3
nombre_archivo_acelerado = "texto_a_voz_acelerado.mp3"
audio_acelerado.export(nombre_archivo_acelerado, format="mp3")

# Reproducir el audio acelerado (opcional)
os.system(f"mpg123 {nombre_archivo_acelerado}")
