# by Kami Bigdely
# Docstrings and blank lines
class Temp_sensor:
    volts_to_temp = 5.6 # [celsius]
    def __init__(self):
        pass

    def read_volts(self):        
        return 2.7

    def get_temp(self):
        return self.read_volts() * Temp_sensor.volts_to_temp


class Co_sensor: # Carbin Manoxide == CO
    volts_to_co = 0.048
    def __init__(self, temp_sensor):
        self.temp_sensor = temp_sensor
        if not self.temp_sensor:
            self.temp_sensor = Temp_sensor()

    def get_co_lvl(self):
        sensor_volts = self.temp_sensor.read_volts()
        self.co = Co_sensor.volts_to_co_lvl(sensor_volts,
          self.temp_sensor.get_temp())
        return self.co

    def read_sensor_voltage(self):
        # In real life, it should read from hardware.        
        return 2.3

    def volts_to_co_lvl(volts, temp):
        return volts * Co_sensor.volts_to_co * temp


class Display_unit:
    def __init__(self):
        self.string = ''

    def display(self,msg):
        print(msg)


class Co_device():
    def __init__(self, co_sensor, display_unit):
        self.co_sensor = co_sensor 
        self.display_unit = display_unit 

    def Display(self):
        msg = 'Carbon Monoxide Level is : ' + str(self.co_sensor.get_co_lvl())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = Temp_sensor()
    co_sensor = Co_sensor(temp_sensor)
    display_unit = Display_unit()
    co_device = Co_device(co_sensor, display_unit)
    co_device.Display()
    