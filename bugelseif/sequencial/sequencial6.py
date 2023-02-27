# '''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. '''
from math import pi

raio = float(input('Digite o raio do círculo\n'))
area = pi * raio**2

print(f'A área é {area:.2f}')