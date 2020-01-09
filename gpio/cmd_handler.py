from gpio.cmd import push, on, off


def handle_cmd(cmd, pin):
    if cmd == 'push':
        push(pin, 0.2)
    elif cmd == 'on':
        on(pin)
    elif cmd == 'off':
        off(pin)