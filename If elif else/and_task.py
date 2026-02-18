# You are in your room,and looking at the window. # TEMP or is it 
# You see the clouds.You know it's going to rain today.
# But you stil need to work.
# You decide you will go to your office only IF the temp doesnt go below -5
# And if you have a umbrella








temperature = float(input("Enter the temperature in °C: "))
has_umbrella = input("Do you have a umbrella    y/n? ")

if temperature >= -5 and has_umbrella=="y": 
    print("You have to go to your office.")
else:
    print("You will not go to office")

