from fabric.api import env, run, sudo

env.hosts = [
"192.168.1.200"
]
env.user = "pi"
gpios = [13, 19, 26, 6]
sofa_lights = [6, 19]
sofa_power = [13]

def update():
    """
    Update and Upgrade the nodes
    """
    sudo("apt-get -y update")
    sudo("apt-get -y upgrade")

def setup_gpio():
    """
    Set up GPIO pins that are being used
    """
    for gpio in gpios:
        sudo('echo "{pin}" > /sys/class/gpio/export'.format(pin=gpio))
        sudo('echo "out" > /sys/class/gpio/gpio{pin}/direction'.format(pin=gpio))

def sofa_lights_on():
    """
    Turn lights on
    """
    for gpio in sofa_lights:
        run("echo '0' > /sys/class/gpio/gpio{pin}/value".format(pin=gpio))

def sofa_lights_off():
    """
    Turn lights off
    """
    for gpio in sofa_lights:
        run("echo '1' > /sys/class/gpio/gpio{pin}/value".format(pin=gpio))

def sofa_power_on():
    """
    Turn sofa power on
    """
    for gpio in sofa_power:
        run("echo '0' > /sys/class/gpio/gpio{pin}/value".format(pin=gpio))

def sofa_power_off():
    """
    Turn sofa power off
    """
    for gpio in sofa_power:
        run("echo '1' > /sys/class/gpio/gpio{pin}/value".format(pin=gpio))
