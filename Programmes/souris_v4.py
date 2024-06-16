# Souris pilotée par joystick
# MIT License

# Copyright (c) 2024 FabLabUtoPi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Licence MIT

# Copyright (c) 2024 FabLabUtoPi

# L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce
# logiciel et des fichiers de documentation associés (le "Logiciel"), de l'utiliser
# sans restriction, y compris sans limitation d'utilisation, de copie, de modification, de fusion, 
# de publication, de distribution, d'accorder des sous-licences et/ou de vendre des copies du logiciel.
# et/ou de vendre des copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni
# de le faire, sous réserve des conditions suivantes :

# La licence ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les
# copies ou parties substantielles du logiciel.

# LE LOGICIEL EST FOURNI "EN L'ETAT", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU
# EXPLICITE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE,
# D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS LES AUTEURS OU
# LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS POUR
# RESPONSABLES D'UNE RÉCLAMATION, D'UN DOMMAGE OU D'UNE AUTRE RESPONSABILITÉ, 
# QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE,
# PROVENANT DE OU EN RELATION AVEC LE LOGICIEL OU AVEC SON UTILISATION 
# OU D'AUTRES TRANSACTIONS LIEES AU LOGICIEL.


# Références
# Source https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/mouse.html
# https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.mouse.Mouse
#
# Créé par le FabLab UtoPi Le Creusot
# Contact : contact@fablab-utopi.org 


# La position x=0, y=0 pour la souris est en haut à gauche de l'écran
#
# Connexion des switchs
# UP                   Souris vers le haut           GP12
# DOWN                 Souris vers le bas            GP13
# RIGHT                Souris vers la gauche         GP10
# LEFT                 Souris vers la droite         GP11

# GAUCHE               Appui bouton gauche           GP5
# DROITE               Appui bouton droit            GP6

# PROG                 Lancement programme           GP7

# Wheel UP             Roulette vers le haut         GP8
# Wheel DOWN           Roulette vers le bas          GP9

# Connexion des LEDs
# DROITE               Bouton droit                  GP0
# GAUCHE               Bouton gauche                 GP1
# PROG                 Lancement programme           GP2
# Wheel UP             Roulette vers le haut         GP3
# Wheel DOWN           Roulette vers le bas          GP4

# Vibreur                                            GP14
# Buzzer                                             GP15

# Importation des bibliothèques utilisées
import time
import board
import digitalio
import usb_hid
import array
import pulseio
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialiser la souris
mouse = Mouse(usb_hid.devices)
# Initialiser le clavier
kbd = Keyboard(usb_hid.devices)

# LED de la carte PICO
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
# LED de la souris
led1 = digitalio.DigitalInOut(board.GP0)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP1)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP2)
led3.direction = digitalio.Direction.OUTPUT

led4 = digitalio.DigitalInOut(board.GP3)
led4.direction = digitalio.Direction.OUTPUT

led5 = digitalio.DigitalInOut(board.GP4)
led5.direction = digitalio.Direction.OUTPUT

# Vibreur
vibreur = digitalio.DigitalInOut(board.GP14)
vibreur.direction = digitalio.Direction.OUTPUT

# Buzzer
buzzer = pulseio.PulseOut(board.GP15, frequency=3000, duty_cycle=32768)
pulses = array.array('H', [65000, 1000, 65000, 65000, 1000])

# Faire Flasher la LED de la carte PICO
def blink() :
    led.value = 1
    time.sleep(0.05)
    led.value = 0


v_lent = 5
v_rapide = 40

# Temps au premier appui sur un bouton
tZero = time.monotonic()
# Temps de départ du comptage du temps avant répétition
tDepart = tZero
# Temps actuel dans le programme
tActuel = tZero
# Temps en s avant répétition 0,5s
tRepete = 0.500


# Définir les boutons du joystick et de la souris
# ===============================================
# Curseur vers le haut
# SORTIE UP
cursUP = digitalio.DigitalInOut(board.GP12)
cursUP.direction = digitalio.Direction.INPUT
cursUP.pull = digitalio.Pull.UP

# Curseur vers le bas
# SORTIE DWN
cursDOWN = digitalio.DigitalInOut(board.GP13)
cursDOWN.direction = digitalio.Direction.INPUT
cursDOWN.pull = digitalio.Pull.UP

# Curseur vers la gauche
# SORTIE LFT
cursLEFT = digitalio.DigitalInOut(board.GP10)
cursLEFT.direction = digitalio.Direction.INPUT
cursLEFT.pull = digitalio.Pull.UP

# Curseur vers la droite
# SORTIE RHT
cursRIGHT = digitalio.DigitalInOut(board.GP11)
cursRIGHT.direction = digitalio.Direction.INPUT
cursRIGHT.pull = digitalio.Pull.UP

# Clic gauche / Appui sur Joystick
LEFT_BUTTON = digitalio.DigitalInOut(board.GP5)
LEFT_BUTTON.direction = digitalio.Direction.INPUT
LEFT_BUTTON.pull = digitalio.Pull.UP

# Clic droit
RIGHT_BUTTON = digitalio.DigitalInOut(board.GP6)
RIGHT_BUTTON.direction = digitalio.Direction.INPUT
RIGHT_BUTTON.pull = digitalio.Pull.UP

# Bouton PROG
PROG_BUTTON = digitalio.DigitalInOut(board.GP7)
PROG_BUTTON.direction = digitalio.Direction.INPUT
PROG_BUTTON.pull = digitalio.Pull.UP

# Roulette UP
up = digitalio.DigitalInOut(board.GP8)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.UP

# Roulette DOWN
down = digitalio.DigitalInOut(board.GP9)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.UP

# Clignoter pour montrer que le programme démarre
for i in range(0, 5):
    blink()
    time.sleep(0.02)

# Chenillard des LEDs
led1.value = True
time.sleep(0.05)
led2.value = True
time.sleep(0.05)
led3.value = True
time.sleep(0.05)
led4.value = True
time.sleep(0.05)
led5.value = True
time.sleep(0.4)
led5.value = False
time.sleep(0.05)
led4.value = False
time.sleep(0.05)
led3.value = False
time.sleep(0.05)
led2.value = False
time.sleep(0.05)
led1.value = False
time.sleep(0.05)

# Test vibreur
vibreur.value = True
time.sleep(0.1)
vibreur.value = False
time.sleep(0.5)
# Test buzzer
buzzer.send(pulses)

# Fermer la fenêtre CIRCUITPI qui s'ouvre à la connexion
kbd.send(Keycode.LEFT_ALT, Keycode.F4)

while True:
    try:
        # Si on active 2 directions simultanément
        # Actionner le vibreur
        if (cursUP.value is False) and (cursLEFT.value is False) :
            print("Activation vibreur")
            vibreur.value = True
            time.sleep(0.1)
            vibreur.value = False
        if (cursDOWN.value is False) and (cursLEFT.value is False) :
            print("Activation vibreur")
            vibreur.value = True
            time.sleep(0.1)
            vibreur.value = False
        if (cursUP.value is False) and (cursRIGHT.value is False) :
            print("Activation vibreur")
            vibreur.value = True
            time.sleep(0.1)
            vibreur.value = False
        if (cursDOWN.value is False) and (cursRIGHT.value is False) :
            print("Activation vibreur")
            vibreur.value = True
            time.sleep(0.1)
            vibreur.value = False

        # Curseur monte de 1 GP12
        if (cursUP.value is False):
            # Lire le temps actuel
            tActuel = time.monotonic()
            # Est ce le temps est > au temps de répétition de 100ms environ (150ms)
            if tActuel > ((tDepart) + 0.200):
                # On vient juste d'appuyer sur la bouton pour la première fois
                # Prendre ce moment comme référence
                tZero = tActuel
            # Si non, vérifier si on appuie depuis plus de tRepete (0,5s)
            if tActuel > ((tZero) + tRepete):
                # On appuie depuis plus que tRepete accélérer le déplacement
                v = v_rapide
            else:
                # On est encore dans les 500ms
                v = v_lent
            # print("tActuel : {:.2f}".format(tActuel*1000))
            # print("tDepart : {:.2f}".format(tDepart*1000))
            # print("tZero : {:.2f}".format(tZero*1000))
            # print("Vitesse : ", v)
            # print("\n\r")
            tDepart = tActuel
            mouse.move(y=-v)
            blink()

        # Curseur descend de 1 GP13
        if (cursDOWN.value is False):
            # Lire le temps actuel
            tActuel = time.monotonic()
            # Est ce le temps est > au temps de répétition de 100ms environ (150ms)
            if tActuel > ((tDepart) + 0.200):
                # On vient juste d'appuyer sur la bouton pour la première fois
                # Prendre ce moment comme référence
                tZero = tActuel
            # Si non, vérifier si on appuie depuis plus de tRepete (0,5s)
            if tActuel > ((tZero) + tRepete):
                # On appuie depuis plus que tRepete accélérer le déplacement
                v = v_rapide
            else:
                # On est encore dans les 500ms
                v = v_lent
            # print("tActuel : {:.2f}".format(tActuel*1000))
            # print("tDepart : {:.2f}".format(tDepart*1000))
            # print("tZero : {:.2f}".format(tZero*1000))
            # print("Vitesse : ", vU)
            # print("\n\r")
            tDepart = tActuel
            mouse.move(y=v)
            blink()

        # Curseur vers la gauche  GP2
        if (cursLEFT.value is False):
            # Lire le temps actuel
            tActuel = time.monotonic()
            # Est ce le temps est > au temps de répétition de 100ms environ (150ms)
            if tActuel > ((tDepart) + 0.200):
                # On vient juste d'appuyer sur la bouton pour la première fois
                # Prendre ce moment comme référence
                tZero = tActuel
            # Si non, vérifier si on appuie depuis plus de tRepete (0,5s)
            if tActuel > ((tZero) + tRepete):
                # On appuie depuis plus que tRepete accélérer le déplacement
                v = v_rapide
            else:
                # On est encore dans les 500ms
                v = v_lent
            # print("tActuel : {:.2f}".format(tActuel*1000))
            # print("tDepart : {:.2f}".format(tDepart*1000))
            # print("tZero : {:.2f}".format(tZero*1000))
            # print("Vitesse : ", vU)
            # print("\n\r")
            tDepart = tActuel
            mouse.move(x=v)
            blink()

        # Curseur vers la droite GP3
        if (cursRIGHT.value is False):
            # Lire le temps actuel
            tActuel = time.monotonic()
            # Est ce le temps est > au temps de répétition de 100ms environ (150ms)
            if tActuel > ((tDepart) + 0.200):
                # On vient juste d'appuyer sur la bouton pour la première fois
                # Prendre ce moment comme référence
                tZero = tActuel
            # Si non, vérifier si on appuie depuis plus de tRepete (0,5s)
            if tActuel > ((tZero) + tRepete):
                # On appuie depuis plus que tRepete accélérer le déplacement
                v = v_rapide
            else:
                # On est encore dans les 200ms
                v = v_lent
            # print("tActuel : {:.2f}".format(tActuel*1000))
            # print("tDepart : {:.2f}".format(tDepart*1000))
            # print("tZero : {:.2f}".format(tZero*1000))
            # print("Vitesse : ", vU)
            # print("\n\r")
            tDepart = tActuel
            mouse.move(x=-v)
            blink()

        # Bouton gauche de la souris
        if (LEFT_BUTTON.value is True):
            # Si un bouton est appuyé on positionne le flag
            flag = 1
            print("BOUTON GAUCHE valeur = ", LEFT_BUTTON.value)
            mouse.click(Mouse.LEFT_BUTTON)
            led1.value = True
        else:
            led1.value = False

        # Bouton droit de la souris
        if (RIGHT_BUTTON.value is True):
            # Si un bouton est appuyé on positionne le flag
            flag = 1
            print("BOUTON DROIT valeur = ", RIGHT_BUTTON.value)
            mouse.click(Mouse.RIGHT_BUTTON)
            led2.value = True
        else:
            led2.value = False

        # Bouton PROGRAMMABLE de la souris
        if (PROG_BUTTON.value is True):
            # Si un bouton est appuyé on positionne le flag
            flag = 1
            print("BOUTON CENTRAL valeur = ", PROG_BUTTON.value)
            buzzer.send(pulses)
            # Envoyer code clavier
            kbd.press(Keycode.WINDOWS)
            time.sleep(.09)
            kbd.release(Keycode.WINDOWS)
            led3.value = True
        else:
            led3.value = False

        # Roulette haut
        if (up.value is True):
            # Si un bouton est appuyé on positionne le flag
            flag = 1
            print("Roulette UP valeur = ", up.value)
            mouse.move(wheel=1)
            led4.value = True
        else:
            led4.value = False

        # Roulette bas
        if (down.value is True):
            # Si un bouton est appuyé on positionne le flag
            flag = 1
            print("Roulette DOWN valeur = ", down.value)
            mouse.move(wheel=-1)
            led5.value = True
        else:
            led5.value = False

        # Tempo de la boucle de lecture des boutons
        time.sleep(0.1)
    except KeyboardInterrupt:
        raise Exception("Arrêté par l'utilisateur")
