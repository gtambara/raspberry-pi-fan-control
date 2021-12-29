# raspberry-pi-fan-control
A simple raspberry pi code for reading and controlling via pwm a 4 wire computer fan.

It's worth mentioning that there is a limit to the frequency of the raspberry pi gpio signal, which affects the input on the fan. In my case, the frequency was something like 25 kHz, which i presume was the cause for such a bad response from the system. At the moment, as i see it, there is no reason to believe that the data aquisition from the tachometer is not precise, but the control itself is limited by the reasons previously mentioned.

The code doesn't display the data nonstop by default. It keeps measuring data and periodically calculates the mean value and displays it in the screen periodically. Those period attributes can be changed. I believed that was necessary since there was a considerable ammount of fluctuation in the speed measurements, and it seems that as the fan speed grows, sometimes the error increased until some peak value, which i haven't found a proper reasoning behind why yet in the net.

PS: the code is commented in brazilian portuguese.
