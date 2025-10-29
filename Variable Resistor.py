import machine
from machine import ADC
import utime

#A0 = Variable resister middle pin (Sensor Output)
#ADC 10bit resolution = 0-1024

variable_resistor = machine.ADC(0)

while True:
    adc_value = variable_resistor.read()
    print('step_value:',adc_value)
    utime.sleep_ms(200)