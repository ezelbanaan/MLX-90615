# MLX-90615
MicroPython driver for the MLX90615 IR temperature sensor. Used with the ESP-32.

# How to use this?
It is really easy to use, first you import MLX90615
```python
import MLX90615
```

Then you need to create a MLX90615 object on I2C bus 0 or 1:
```python
mlx90615 = MLX90615.MLX90615(0)
```

Then you can use the following functions:
```python
mlx90615.temperature()  # Prints the temperature in Celcius of the object the MLX90615 is pointing at.
mlx90615.ambient()      # Prints the temperature in Celcius of the MLX90615 package.
mlx90615.raw()          # Prints the raw ir sensor data.
```
Thats it!
# Pin layout
The following pins can be used:

I2C bus 0
```
SCL=18
SDA=19
```
I2C bus 1
```
SCL=25
SDA=26
```
