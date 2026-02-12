import random

print('----------------------\nPEDRA PAPEL ou TESOURA\n----------------------\n\nPreparado para a batalha? \n\nEscolha Pedra, Papel ou Tesoura para vencer o computador\n\n|**Lembre as regras:**|\n| PEDRA vence TESOURA, |\n| TESOURA vence PAPEL  |\n| e PAPEL vence PEDRA  |\n\nEntão vamos lá:\n\n')
for i in range(3,0,-1): # Contagem regressiva
    print(f'{i} ...\n')

opcoes = ['PEDRA','PAPEL','TESOURA']
continuar = 'S'
batalha = 0
vitorias = 0
empates = 0
derrotas = 0

while continuar.upper() == 'S':
    jogada = input(print('> Faça sua jogada (Digite: PEDRA, PAPEL ou TESOURA): '))
    jogada_com = random.choice(opcoes)
    batalha += 1

    if jogada.upper() == jogada_com:
        print(f"\nVocê escolheu {jogada} e o computador escolheu {jogada_com}\n# Temos um EMPATE!!!")
        empates += 1

    elif jogada.upper() == 'PEDRA' and jogada_com=='TESOURA' or jogada.upper() == 'PAPEL'and jogada_com =='PEDRA' or jogada.upper() == 'TESOURA' and jogada_com =='PAPEL':
        print(f"\nVocê escolheu {jogada} e o computador escolheu {jogada_com}\n# PARABÉNS!!! Você ganhou!!")
        continuar = input(print('\n> Quer tentar novamente? (Digite "s" para sim ou "n" para não): '))
        vitorias += 1

    else:
        print(f"\nVocê escolheu {jogada} e o computador escolheu {jogada_com}\n# Você perdeu.")
        continuar = input(print('\n> Quer tentar novamente? (Digite "s" para sim ou "n" para não): '))
        derrotas += 1

print(f'\n\nVocê batalhou {batalha} vezes! Veja seus resultados: \n# Vitórias: {vitorias}\n# Derrotas: {derrotas}\n# Empates: {empates}\n\n\n---\nFIM\n---')
