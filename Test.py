import time
import requests
from bs4 import BeautifulSoup

# Configuración de Telegram
TELEGRAM_BOT_TOKEN = "7496474239:AAGyTG2LXnwyVTb9A5gcILT2Cfk6WnrVHeM"
TELEGRAM_CHAT_ID = "1494623726"

# URL de la página de citas NIE
URL_CITAS = "https://icp.administracionelectronica.gob.es/icpplus/citar"


# Función para enviar notificación a Telegram
def enviar_telegram():
    mensaje = "¡Se ha detectado disponibilidad de citas para el NIE! Ingresa rápidamente en: " + URL_CITAS
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    try:
        requests.get(url, params=params)
        print("Mensaje enviado a Telegram")
    except Exception as e:
        print("Error enviando mensaje a Telegram:", e)


# Función para verificar la disponibilidad de citas
def verificar_citas():
    try:
        response = requests.get(URL_CITAS)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Aquí debes inspeccionar el HTML de la página para encontrar el mensaje de "No hay citas disponibles"
        if "no hay citas disponibles" not in soup.text.lower():
            enviar_telegram()
            print("¡Cita detectada! Se ha enviado un mensaje a Telegram.")
        else:
            print("No hay citas disponibles. Reintentando...")
    except Exception as e:
        print("Error al verificar citas:", e)


# Ejecutar el script cada 5 minutos
while True:
    verificar_citas()
    time.sleep(300)


