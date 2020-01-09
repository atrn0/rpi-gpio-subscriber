from time import sleep

from gpiozero import LED


def push(pin, duration):
    print(f'push {pin}')
    pin = LED(pin)
    pin.blink(on_time=duration, n=1)
    sleep(2)


def on(pin):
    print(f'on {pin}')
    pin = LED(pin)
    pin.on()
    sleep(2)


def off(pin):
    print(f'off {pin}')
    pin = LED(pin)
    pin.off()
    sleep(2)
