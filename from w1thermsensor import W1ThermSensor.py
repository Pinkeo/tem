from w1thermsensor import W1ThermSensor

def read_temperature():
    sensor = W1ThermSensor()

    try:
        temperature = sensor.get_temperature()
        return temperature
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None

if __name__ == "__main__":
    temperature = read_temperature()

    if temperature is not None:
        print(f"Temperature: {temperature:.2f} °C")
