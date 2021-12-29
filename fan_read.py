# Programa responsavel por ler os dados obtidos pelo tacometro, inbutido nas ventoinhas utilizadas nos HSMs.

import RPi.GPIO as GPIO
import time
import math
import numpy as np

GPIO.setmode(GPIO.BOARD)

TACH_PIN = 36  		# Pino que recebe dados do tacometro no BCM 16 no Raspberry Pi
PULSES = 2 			# Numero de pulsos por revolucao da ventoinha
PRECISION = 0.01 	# Precisao do tacometro
SAMPLE_SPACE = 100 	# Numero de medicoes realizadas antes de apresenta-las
TIME = 2			# Tempo entre loops, permitindo as coletas de dados

GPIO.setup(TACH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
t = time.time()

# define rpm se nao estiver definido
try: rpm
except NameError: rpm = [0]

def fall(argument):
	global t, rpm
	dt = time.time() - t
	if(dt >= PRECISION):
		freq = 1 / dt
		rpm.append(freq * 60 / PULSES)
		t = time.time()

GPIO.add_event_detect(TACH_PIN, GPIO.FALLING, fall)

while True:
	time.sleep(TIME)
	rpm_mean = 0
	
	if(time.time() - t > TIME):
		print(0)
		t = time.time()

	if(len(rpm) >= SAMPLE_SPACE):
		for i in range(1, len(rpm)-1):	
			rpm_mean += rpm[i]

		rpm_mean = rpm_mean / (len(rpm) - 1)
		print( "\nmean: %.f" % rpm_mean)
		print("std. deviation: " +  "%.1f" % np.std(rpm))
		rpm.clear()
		rpm.append(0)