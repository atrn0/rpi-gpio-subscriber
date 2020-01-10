from time import sleep

from gpiozero import DigitalOutputDevice

pins = list(
    map(
        lambda pin: DigitalOutputDevice(pin, active_high=False, initial_value=False),
        range(1, 26)
    )
)


def push(pin, duration):
    print(f'push {pin}')
    pins[pin - 1].blink(on_time=duration, n=1)
    sleep(2)


def on(pin):
    print(f'on {pin}')
    pins[pin - 1].on()
    sleep(2)


def off(pin):
    print(f'off {pin}')
    pins[pin - 1].off()
    sleep(2)
