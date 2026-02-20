import random

print('----------------------\nPEDRA PAPEL ou TESOURA\n----------------------\
    \n\nPreparado para a batalha???\
    \n\nEscolha Pedra, Papel ou Tesoura para vencer o computador\
    \n\n|**Lembre as regras:**|\n| PEDRA vence TESOURA |\n| TESOURA vence PAPEL |\n| PAPEL vence PEDRA   |\
    \n\nEntão vamos lá:\n\n'
    )

for i in range(3,0,-1): # Contagem regressiva
    print(f'{i} ...\n')

opcoes = ['PEDRA','PAPEL','TESOURA'] # opções para o a jogada do computador selecionar ramdomicamente
continuar = 'S'
batalha = 0
vitorias = 0
empates = 0
derrotas = 0

while continuar == 'S': # loop de jogadas
    while True: # validação de entrada
        jogada = input('\n> Faça sua jogada (Digite: PEDRA, PAPEL ou TESOURA): ').upper() # jogada do usúario
        if jogada in ['PEDRA', 'PAPEL', 'TESOURA']: # verificação das possibilidades aceitas
            break
        print("Opção inválida! Digite PEDRA, PAPEL ou TESOURA.")
    jogada_com = random.choice(opcoes) # jogada do computador
    batalha += 1 # contador de batalhas

    if jogada == jogada_com: # condição de empate
        print(f"\nVocê escolheu {jogada} e o computador escolheu {jogada_com}\n# Temos um EMPATE!!!\n")
        empates += 1 # contador 

    elif jogada == 'PEDRA' and jogada_com=='TESOURA' or jogada == 'PAPEL'and jogada_com =='PEDRA' or jogada == 'TESOURA' and jogada_com =='PAPEL': # condições de vitória
        print(f"\nVocê escolheu {jogada} e o computador escolheu {jogada_com}\n# PARABÉNS!!! Você ganhou!!")
        while True: # validação de entrada
            continuar = input('\n> Quer tentar novamente? (Digite "S" para sim ou "N" para não): \n').upper()
            if continuar in [ 'S', 'N']: # verificação das possibilidades aceitas
                break
            print("Opção inválida! Digite 'S' ou 'N'.")
        vitorias += 1 # contador 

    else: # derrota
        print(f"\nVocê escolheu {jogada} e o computador escolheu {jogada_com}\n# Você perdeu.")
        while True: # validação de entrada
            continuar = input('\n> Quer tentar novamente? (Digite "S" para sim ou "N" para não): \n').upper()
            if continuar in ['S', 'N']: # verificação das possibilidades aceitas
                break
            print("Opção inválida! Digite 'S' ou 'N'.")
        derrotas += 1 # contador 

print(f'\n\nVocê batalhou {batalha} vezes! Veja seus resultados: \n\
# Vitórias: {vitorias}\n# Derrotas: {derrotas}\n# Empates: {empates}\n\n\n---\nFIM\n---') # feedbacks
