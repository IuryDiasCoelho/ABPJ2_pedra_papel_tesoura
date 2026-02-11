import random

print("Bem vindo\n")
print("Vamos jogar Pedra, Papel ou Tesoura")

while True:

    opcoes = ['pedra', 'papel', 'tesoura']
    entrada_usuario=input("\nDigite pedra, papel ou tesoura :").lower()

    if entrada_usuario not in opcoes:
        print("\n Entre com uma opção valida\n")
    else:
        print(f"\nVocê escolheu {entrada_usuario}\n")

        maquina=random.choice(opcoes)
        print(f"A maquina escolheu {maquina}\n")

        if entrada_usuario == maquina:
            print("Empate\n")
        elif (entrada_usuario == 'pedra' and maquina == 'papel') or \
             (entrada_usuario == 'papel' and maquina == 'tesoura') or \
             (entrada_usuario == 'tesoura' and maquina == 'pedra'):

            print("Você perdeu!\n")
        else:
            print("Parabéns, você ganhou!\n")

        finalizar = input("Deseja jogar novamente? (s/n):").lower()
        if finalizar == 'n':
            print("\nFim de jogo")
            break

