import random

print("Bem vindo\n")
print("Vamos jogar Pedra, Papel , Tesoura , largato Spock\n ")
print("Regras do jogo\n")
print("É muito simples: Tesoura corta papel, papel cobre pedra, pedra esmaga lagarto, lagarto envenena Spock,\n"
      " Spock esmaga tesoura, tesoura decapita lagarto, lagarto come papel, papel refuta Spock, Spock vaporiza\n "
      "pedra e, como sempre foi, pedra amassa tesoura.")

while True:

    opcoes = ['pedra', 'papel', 'tesoura','largato','spock']
    entrada_usuario=input("\nDigite pedra, papel , tesoura ,largato ou Spock :").lower()

    if entrada_usuario not in opcoes:
        print("\nEntre com uma opção valida\n")
    else:
        print(f"\nVocê escolheu {entrada_usuario}\n")

        maquina=random.choice(opcoes)
        print(f"A maquina escolheu {maquina}\n")

        if entrada_usuario == maquina:
            print("Empate\n")
        elif (entrada_usuario == 'pedra' and maquina == 'papel') or \
             (entrada_usuario == 'papel' and maquina == 'tesoura') or \
             (entrada_usuario == 'tesoura' and maquina == 'pedra') or\
            (entrada_usuario == 'largato' and maquina == 'pedra') or \
            (entrada_usuario == 'spock' and maquina == 'largato') or\
            (entrada_usuario == 'tesoura' and maquina == 'spock') or \
            (entrada_usuario == 'largato' and maquina == 'tesoura') or\
            (entrada_usuario == 'papel' and maquina == 'largato') or\
            (entrada_usuario == 'spock' and maquina == 'papel') or\
            (entrada_usuario == 'pedra' and maquina == 'spock'):

            print("Você perdeu!\n")
        else:
            print("Parabéns, você ganhou!\n")

        finalizar = input("Deseja jogar novamente? (s/n):").lower()
        if finalizar == 'n':
            print("\nFim de jogo")
            break

