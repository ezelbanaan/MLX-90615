import MLX90615, time

mlx90615 = MLX90615.MLX90615(0) # Creates an mlx90615 instance on I2C bus 0.

while True:
    print("Object Temperature: ", mlx90615.temperature()) # Prints the temperature in Celcius of the object the MLX90615 is pointing at.
    print("Ambient Temperature: ", mlx90615.ambient()) # Prints the temperature in Celcius of the MLX90615 package.
    print("Raw data: ", mlx90615.raw()) # Prints the raw ir sensor data.
    print("-"*50)
    time.sleep(1)