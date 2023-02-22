# program to convert temperature to and from celsius, fahrenheit

def temp_conversion(temp, unit):
    if unit == 'F':
        c_temp = ((temp-32)/9)*5
        print('Temperature converted from Fahrenheit to Celsius is: ' + str(c_temp))
    elif unit == 'C':
        f_temp = ((temp/5)*9)+32
        print('Temperature converted from Celsius to Fahrenheit is: ' + str(f_temp))

temp_conversion(60,'C')
temp_conversion(140,'F')