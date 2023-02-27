# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# https://wiki.python.org.br/EstruturaSequencial

valor = float(input('Quanto você ganha por hora? '))
hora = float(input('Quantas horas você trabalhou este mês? '))
print(f'Você irá receber este mês: R${valor*hora:.2f}')