#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Oct 6th, 2021
# Version: 1.0

from machine import Pin, PWM
from time import sleep

buzzerPIN=15
BuzzerObj=PWM(Pin(buzzerPIN))

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


# Play following notes by changing frequency:
#C (DO)
#buzzer(BuzzerObj,523,0.5,0.1)

#D (RE)
#buzzer(BuzzerObj,587,0.5,0.1)

#E (MI)
#buzzer(BuzzerObj,659,0.5,0.1)

#F (FA)
#buzzer(BuzzerObj,698,0.5,0.1)

#G (SOL)
#buzzer(BuzzerObj,784,0.5,0.1)

#A (LA)
#buzzer(BuzzerObj,880,0.5,0.1)

#B (SI)
#buzzer(BuzzerObj,987,0.5,0.1)

# Bip
buzzer(BuzzerObj,2000,0.05,0.1)

#Deactivates the buzzer
BuzzerObj.deinit()