this = input("Do you want to convert Celsius to Fahrenheit(1) or Fahrenheit to Celsius(2)")
this = int(this)
if this == 1:
        degrees = input("How many degrees Celsius do you want to convert to Fahrenheit? ")
        degrees = float(degrees)
        fahrenheit = degrees * 1.8 + 32
        print(fahrenheit)
elif this == 2:
        degrees1 = input("How many degrees Fahrenheit do you want to convert to Celsius? ")
        degrees1 = float(degrees1)
        celcius = degrees1 * 1.8 + 32
        print(celcius)