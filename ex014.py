#Conversor de Temperaturas
celsius=float(input('Qual é a temperatura em Celsius?'))
kelvin=(celsius+273.15)
fahrenheit=((celsius*1.8)+32)
print('A temperatura {}°C corresponde a:'.format(celsius))
print('{:.1f}K'.format(kelvin))
print('{:.1f}°F'.format(fahrenheit))