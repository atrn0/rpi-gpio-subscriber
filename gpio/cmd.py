from gpiozero import LED


def push(pin, duration):
    LED(pin).blink(on_time=duration, n=1)


def on(pin):
    LED(pin).on()


def off(pin):
    LED(pin).off()
