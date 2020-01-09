from gpiozero import LED


def push(pin, duration):
    print(f'push {pin}')
    LED(pin).blink(on_time=duration, n=1)


def on(pin):
    print(f'on {pin}')
    LED(pin).on()


def off(pin):
    print(f'off {pin}')
    LED(pin).off()
