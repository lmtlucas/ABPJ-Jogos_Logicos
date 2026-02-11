import random

print('PEDRA PAPEL ou TESOURA\n\nPreparado para a batalha? \n\nEscolha Pedra, Papel ou Tesoura para vencer o computador\n\n**Lembre as regras:\n - pedra vence tesoura, tesoura vence papel e papel vence pedra\n\n Então vamos lá:\n\n3\n...\n2\n..\n1\n.')

jogada = input(print('Faça sua jogada (Digite: pedra , papel ou tesoura): '))

opcoes = ['pedra','papel','tesoura']
jogada_com = random.choice(opcoes)
continuar = 's'

while continuar == 's':
    while jogada == jogada_com:
        print(f"Você escolheu {jogada} e o computador escolheu {jogada_com}\n Temos um EMPATE!!!")
        jogada = input(print('Faça sua jogada (Digite: pedra , papel ou tesoura): '))
        jogada_com = random.choice(opcoes)
    if jogada == 'pedra' and jogada_com=='tesoura' or jogada == 'papel'and jogada_com =='pedra' or jogada == 'tesoura' and jogada_com =='papel':
        print(f"Você escolheu {jogada} e o computador escolheu {jogada_com}\n PARABÉNS!!! Você ganhou!!")
        continuar = input(print('Quer tentar novamente? (Digite "s" para sim ou "n" para não): '))
        jogada = input(print('Faça sua jogada (Digite: pedra , papel ou tesoura): '))
        jogada_com = random.choice(opcoes)
    else:
        print(f"Você escolheu {jogada} e o computador escolheu {jogada_com}\n Você perdeu.")
        continuar = input(print('Quer tentar novamente? (Digite "s" para sim ou "n" para não): '))
        jogada = input(print('Faça sua jogada (Digite: pedra , papel ou tesoura): '))
        jogada_com = random.choice(opcoes)
