'''
Run mainX
uncomment to run mainRX
'''
# import mainRX
print('main initiated using wifi99')
from machine import Pin, Timer
led = Pin(2, Pin.OUT)
def cb(t):
    led.toggle()

tim = Timer(0, freq=2, mode=Timer.PERIODIC, callback=cb)
