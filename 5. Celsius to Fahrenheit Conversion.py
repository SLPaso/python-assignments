# Lambda and map to convert Celsius to Fahrenheit
celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)