#To cheack clothing based on temp

temperature = int(input("Enter the temperature in °C: "))

if temperature >= 25:
    print("You can wear light and soft clothes because its warm.")
elif temperature >= 15 and temperature < 25:
    print("You can wear light clothes, but carry a light jacket because it might be chilly.")
else:
    print("It is cold. Wear a jacket or pullover.")
1516