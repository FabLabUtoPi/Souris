# Importer la librairie machine - Pin
from machine import Pin, PWM
# Importer Sleep
from time import sleep
import sys

# Définir la sortie vibreur
vibreurPIN = 14
pin_vibreur = Pin(vibreurPIN
                  , mode=Pin.OUT, value=0)

# Définir le Buzzer
buzzerPIN = 15
BuzzerObj=PWM(Pin(buzzerPIN))

# Fonction du Buzzer
def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):
    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.2))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(silence_duration)


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

# Déclarer lejoystick
pin_joystick_H = Pin(10, mode=Pin.IN, pull=Pin.PULL_UP)
pin_joystick_B = Pin(11, mode=Pin.IN, pull=Pin.PULL_UP)
pin_joystick_G = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
pin_joystick_D = Pin(13, mode=Pin.IN, pull=Pin.PULL_UP)


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
LED_OFF()

# Allumer la LED si un bouton est appuyé
# On sort si les deux boutons extrèmes sont ppuyés
while True:
    if (pin_button1.value() == 1 & pin_button5.value() == 1):
        print("Arrêt du programme")
        LED_OFF()
        # Bip
        buzzer(BuzzerObj,2000,0.05,0.05)
        sleep(0.05)
        buzzer(BuzzerObj,2000,0.05,0.05)

        #Deactivates the buzzer
        BuzzerObj.deinit()
        sys.exit()

    # Gestion de GPIO14
    pin_vibreur.on()
    print("ON")
    sleep(0.1)

    pin_vibreur.off()
    print("OFF")
    sleep(0.05)
    
    pin_vibreur.on()
    print("ON")
    sleep(0.1)

    pin_vibreur.off()
    print("OFF")
    buzzer(BuzzerObj,2000,0.05,0.1)

    sleep(2)



