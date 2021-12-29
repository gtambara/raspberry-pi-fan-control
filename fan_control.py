import RPi.GPIO as GPIO
import time
import os
import signal
import sys

GPIO.setmode(GPIO.BOARD)

FAN_PIN = 32            # GPIO 12 (in BCM) para sinal de controle PWM
WAIT_TIME = 5           # Segundos entre mudancas
PWM_FREQ = 25000        # Frequencia do PWM em Hz

GPIO.setup(FAN_PIN, GPIO.OUT, initial = GPIO.LOW)
pwm = GPIO.PWM(FAN_PIN, PWM_FREQ)

FAN_OFF = 0
FAN_LOW = 25
FAN_MID = 50
FAN_HIGH = 75
FAN_MAX = 100

pwm.start(FAN_OFF)

while(True):
    aux = input('Selecione a velocidade:\n0-OFF\n1-LOW\n2-MID\n3-HIGH\n4-MAX\n9-sair\n')
    if(aux == '0'):
        pwm.ChangeDutyCycle(FAN_OFF)
    elif(aux == '1'):
        pwm.ChangeDutyCycle(FAN_LOW)
    elif(aux == '2'):
        pwm.ChangeDutyCycle(FAN_MID)
    elif(aux == '3'):
        pwm.ChangeDutyCycle(FAN_HIGH)
    elif(aux == '4'):
        pwm.ChangeDutyCycle(FAN_MAX)
    elif(aux == '9'):
        pwm.ChangeDutyCycle(FAN_OFF)
        GPIO.cleanup()
        exit()
        break
    time.sleep(WAIT_TIME)