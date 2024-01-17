import time
import keyboard
import gi
import os
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from PIL import ImageGrab
import RPi.GPIO as GPIO

#Button setup
GPIO.setmode(GPIO.BOARD)
buttonPin = 37
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonState = GPIO.input(buttonPin)



# Funzione per catturare lo screenshot della finestra di OBS
def capture_obs_screenshot():
    try:
        # Inizializza il gestore delle finestre
        screen = Wnck.Screen.get_default()
        screen.force_update()
        # Cattura lo screenshot
        screenshot = ImageGrab.grab()
        # Genera un nome unico per il file
        base_filename = 'screenshot.png'
        file_counter = 1
        while os.path.exists("/home/pi/Desktop/foto/"+base_filename):
            base_filename = f'screenshot_{file_counter}.png'
            file_counter += 1

        screenshot.save("/home/pi/Desktop/foto/"+base_filename)

        print(f"Screenshot catturato con successo e salvato come {base_filename}!")

    except Exception as e:
        print(f"Errore: {str(e)}")


# Associa la funzione alla pressione della barra spaziatrice   
keyboard.on_press_key('space', lambda e: capture_obs_screenshot())



# Mantieni lo script in esecuzione
try:
    while True:
        buttonState = GPIO.input(buttonPin)
        if buttonState == 0:
            #keyboard.send('space')
            capture_obs_screenshot()
            time.sleep(0.1)
        #time.sleep(1)
except KeyboardInterrupt:
    pass


