# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.

primeiro_numero = int(input('Qual o primeiro número? '))
segundo_numero = int(input('Qual o segundo número? '))
numero_real = float(input('Qual o número real? '))

print(f'O produto do dobro do primeiro com a metade do segundo é {primeiro_numero * segundo_numero}')
print(f'A soma do triplo do primeiro com o número real é {(primeiro_numero*3)+numero_real:.2f}')
print(f'O número real elevado ao cubo é {numero_real**3}')