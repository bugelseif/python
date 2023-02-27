# '''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
# (0 °C × 9/5) + 32 '''

c = float(input('Digite a temperatura em Fahrenheit\n'))
f = (c * 9 / 5) + 32

print(f'A temperatura é {f:.2f}°F')
