from gpiozero import LED


def push(pin):
    LED(pin).blink(on_time=0.2, n=1)


def on(pin):
    LED(pin).on()


def off(pin):
    LED(pin).off()
