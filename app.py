import random

# Função para obter a escolha aleatória do computador
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Função para obter a escolha do jogador
def get_user_choice():
    choice = input("Escolha rock, paper ou scissors: ").lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("Opção inválida. Tente novamente.")
        return None
    return choice

# Função para determinar o vencedor da rodada
def determine_winner(user, computer):
    if user == computer:
        return "Empate"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

# Função principal do jogo
def play_game():
    rounds = 0
    wins = 0

    while True:
        user_choice = None
        while user_choice is None:
            user_choice = get_user_choice()

        computer_choice = get_computer_choice()
        print(f"O computador escolheu: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        rounds += 1
        if result == "Você venceu!":
            wins += 1

        play_again = input("Deseja jogar novamente? (s/n): ").lower()
        if play_again != "s":
            break

    print("\nPontuação final:")
    print(f"Rodadas jogadas: {rounds}")
    print(f"Vitórias: {wins}")

# Executa o jogo
if __name__ == "__main__":
    play_game()