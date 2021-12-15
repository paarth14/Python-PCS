# Write a Python Program using function to convert celsius to farenheit.

def convert_cel_to_far(celsius):
    conversion = celsius * (9/5) + 32
    print(conversion, "F")
    
convert_cel_to_far(int(input("Enter the temperature in celsius: ")))
