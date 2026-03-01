'''
Run mainX
uncomment to run mainRX
'''
# import mainRX
print('main initiated')
from machine import Pin, Timer
led12 = Pin(12, Pin.OUT)
led02 = Pin(2, Pin.OUT)
led02.on()
def cb(t):
    led02.toggle()
    led12.toggle()

tim = Timer(0, freq=1, mode=Timer.PERIODIC, callback=cb)
