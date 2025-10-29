# 🎛️ ESP8266 Variable Resistor (Potentiometer) ADC Reading — MicroPython

## 🧠 Overview
This project demonstrates how to read **analog voltage values** from a **variable resistor (potentiometer)** using the **ADC (Analog-to-Digital Converter)** on the **ESP8266** board with **MicroPython**.  
The sensor’s analog output is connected to the **A0** pin, and the digital value (0–1024) is printed on the Thonny IDE console.

---

## ⚙️ Hardware Setup

| Component            | ESP8266 Pin | Description |
|----------------------|-------------|--------------|
| Variable Resistor    | A0          | Analog Input |
| Power (VCC)          | 3.3V        | +3.3 V Supply |
| Ground (GND)         | GND         | Common Ground |

🔹 Connect the **middle pin** of the potentiometer to **A0**.  
🔹 Connect one side to **3.3 V** and the other side to **GND**.  

---

## 🧩 Code

```python
import machine
from machine import ADC
import utime

# A0 = Variable resistor middle pin (Sensor Output)
# ADC 10-bit resolution = 0–1024

variable_resistor = machine.ADC(0)

while True:
    adc_value = variable_resistor.read()
    print('step_value:', adc_value)
    utime.sleep_ms(200)
