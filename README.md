# raspberry-pi-fan-control
A simple raspberry pi code for reading and controlling via pwm a 4 wire computer fan.

It's worth mentioning that there is a limit to the frequency of the raspberry pi gpio signal, which affects the input on the fan. In my case, the frequency was somethink like 25kHz, which i presume was the cause for such a bad response from the system. At the moment, as i see it, there is no reason to believe that the data aquisition is not precise, but the control itself is limited by the reasons previously mentioned.

PS: the code is commented in brazilian portuguese.
