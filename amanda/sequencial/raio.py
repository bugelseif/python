# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
# https://wiki.python.org.br/EstruturaSequencial
from math import pi

raio = float(input('Qual o raio do círculo? '))
print(f'A área do círculo é {pi * raio**2:.2f}')