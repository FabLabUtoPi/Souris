# Importer la librairie machine - Pin
from machine import Pin
# Importer Sleep
from time import sleep
import sys

# Déclarer les LEDs des Boutons Poussoirs
pin_led1 = Pin(0, mode=Pin.OUT, value=1)
pin_led2 = Pin(1, mode=Pin.OUT, value=1)
pin_led3 = Pin(2, mode=Pin.OUT, value=1)
pin_led4 = Pin(3, mode=Pin.OUT, value=1)
pin_led5 = Pin(4, mode=Pin.OUT, value=1)

# Déclarer les boutons poussoirs
pin_button1 = Pin(5, mode=Pin.IN, pull=Pin.PULL_UP)
pin_button2 = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)
pin_button3 = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)
pin_button4 = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)
pin_button5 = Pin(9, mode=Pin.IN, pull=Pin.PULL_UP)

# Eteindre les LEDs 
def LED_OFF():
    pin_led1.off()
    pin_led2.off()
    pin_led3.off()
    pin_led4.off()
    pin_led5.off()
    
# Allumer les LEDs 
def LED_ON():
    pin_led1.on()
    pin_led2.on()
    pin_led3.on()
    pin_led4.on()
    pin_led5.on()
    
# Attendre 0.2 secondes et éteindre les LEDs
sleep(0.2)
LED_OFF()
sleep(0.2)
LED_ON()
sleep(0.2)

# Allumer la LED si un bouton est appuyé
# On sort si les deux boutons extrèmes sont ppuyés
while True:
    if (pin_button1.value() == 1 & pin_button5.value() == 1):
        print("Arrêt du programme")
        LED_OFF()
        sys.exit()
    
    if pin_button1.value() == 1:
        pin_led1.on()
    else:
        pin_led1.off()
    if pin_button2.value() == 1:
        pin_led2.on()
    else:
        pin_led2.off()
    if pin_button3.value() == 1:
        pin_led3.on()
    else:
        pin_led3.off()
    if pin_button4.value() == 1:
        pin_led4.on()
    else:
        pin_led4.off()
    if pin_button4.value() == 1:
        pin_led4.on()
    else:
        pin_led4.off()
    if pin_button5.value() == 1:
        pin_led5.on()
    else:
        pin_led5.off()
