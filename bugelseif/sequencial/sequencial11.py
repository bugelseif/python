# '''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     a)o produto do dobro do primeiro com metade do segundo .
#     b)a soma do triplo do primeiro com o terceiro.
#     c)o terceiro elevado ao cubo. '''

primeiro = int(input('Digite o primeiro numero em inteiro\n'))
segundo = int(input('Digite o segundo numero em inteiro\n'))
terceiro = float(input('Digite o terceiro numero em real\n'))

a = (primeiro * 2) * (segundo / 2)
b = (primeiro * 3) + terceiro
c = (terceiro**3)

print(f'Os resultados são, sequencialmente, são: {a}, {b}, {c}')