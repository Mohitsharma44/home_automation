## Home Automation Scripts

### Smart-Plug
Connected Rpi2 to a Relay.

#### Shell commands: 
- Export the GPIO pins controlling the relays
```
echo "23" > /sys/class/gpio/export
echo "19" > /sys/class/gpio/export
echo "13" > /sys/class/gpio/export
echo "6" > /sys/class/gpio/export
```

- Set the direction of the GPIO pins being used to "out"
```
echo "out" > /sys/class/gpio/gpio23/direction
echo "out" > /sys/class/gpio/gpio19/direction
echo "out" > /sys/class/gpio/gpio13/direction
echo "out" > /sys/class/gpio/gpio6/direction
```

- Control the relay excitation (0 or 1)
```
echo "0" > /sys/class/gpio/gpio23/value
echo "0" > /sys/class/gpio/gpio19/value
echo "0" > /sys/class/gpio/gpio13/value
echo "0" > /sys/class/gpio/gpio6/value
```

#### Fabric commands:
```
fab <function_name>
```
