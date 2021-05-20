from machine import I2C

class MLX90615():
    """
    Creates a MLX90615 instance using the ESP-32 I2C circuitory, either I2C bus 0 or 1.
    The created instance is easy and ready to use.
    """
    def __init__(self, i2c_interface):
        try:
            self.i2c_interface = int(i2c_interface)
        except:
            raise ValueError("The i2c_interface must be an integer")
        
        if i2c_interface == 0:
            self.mlx90615 = I2C(0, freq=100000)
        elif i2c_interface == 1:
            self.mlx90615 = I2C(1, freq=100000)
        else:
            raise ValueError("The i2c_interface must be 0 or 1")

    def temperature(self):
        """
        Returns the temperature in Celsius of the object the mlx90615 is pointing towards.
        """
        raw = self.mlx90615.readfrom_mem(0x5b, 0x27,3)
        temp = (raw[0] + (raw[1]<<8)) * 0.02 - 273.15
        return temp

    def ambient(self):
        """
        Returns the ambient temperature in Celsius. The ambient temperature is the temperature inside the MLX90615 senor package.
        """
        raw = self.mlx90615.readfrom_mem(0x5b, 0x26,3)
        temp = (raw[0] + (raw[1]<<8)) * 0.02 - 273.15
        return temp

    def raw(self):
        """
        Returns the raw infrared readings.
        """
        raw = self.mlx90615.readfrom_mem(0x5b, 0x25,3)
        temp = (raw[0] + ((raw[1] & 0x7f)<<8))
        if raw[1]&0x7f:
            temp = -temp
        return temp