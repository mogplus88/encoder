'''
Run mainX
uncomment to run mainRX
'''
# import mainRX
print('main initiated')
from machine import Pin, Timer
led = Pin(12, Pin.OUT)
def cb(t):
    led.toggle()

tim = Timer(0, freq=10, mode=Timer.PERIODIC, callback=cb)
