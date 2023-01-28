import os

def get_brightness():
    with open('/sys/class/backlight/intel_backlight/brightness', 'r') as f:
        return f.read().strip()

def get_max_brightness():
    with open('/sys/class/backlight/intel_backlight/max_brightness', 'r') as f:
        return f.read().strip()

def set_brightness(value):
    os.system(f"echo {value} > /sys/class/backlight/intel_backlight/brightness")

def brightness():
    return f'☀ {int(get_brightness())/240}%'

def up():
    set_brightness(int(get_brightness()) + 100)

def down():
    set_brightness(int(get_brightness()) - 100)
