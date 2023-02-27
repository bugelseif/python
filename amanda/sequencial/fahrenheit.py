# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
# https://wiki.python.org.br/EstruturaSequencial

celsius = float(input('Qual a temperatura em celsius? '))
print(f'A temperatura em fahrenheit seria: {((celsius*9)/5)+32:.2f}°')