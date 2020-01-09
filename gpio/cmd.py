from gpiozero import LED


def push(pin, duration):
    print(f'push {pin}')
    pin = LED(pin)
    pin.blink(on_time=duration, n=1)


def on(pin):
    print(f'on {pin}')
    pin = LED(pin)
    pin.on()


def off(pin):
    print(f'off {pin}')
    pin = LED(pin)
    pin.off()
