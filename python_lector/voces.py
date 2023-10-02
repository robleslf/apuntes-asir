import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Obtener la lista de voces disponibles
voices = engine.getProperty('voices')

# Imprimir las voces disponibles
for voice in voices:
    print("Voz: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Idioma: %s" % voice.languages)
    print(" - Acento: %s" % voice.accent)
    print()
