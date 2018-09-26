# Create a program to convert Celsius to Fahrenheit
# September 26 2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Matthew Salmon
#

#Ask the user to input the temperature in Celsius
celsius = int(input("Enter the temperature in Celsius that you wish to convert to \
Fahrenheit: "))

#Convert the entered temperature to Fahrenheit
fahrenheit = int((9/5) * celsius + 32)

#Display the converted temperature in Fahrenheit
print("The tempterature", celsius ,"in Celsius is", fahrenheit,"in Fahrenheit.")
