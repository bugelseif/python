# '''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. '''

valor = float(input('Quanto você ganha por hora?\n'))
horas = float(input('Quantas horas você trabalha por mes?\n'))

salario = valor * horas

print(f'O salario do mês é R${salario}')