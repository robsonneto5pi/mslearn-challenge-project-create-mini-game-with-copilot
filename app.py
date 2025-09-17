import random
import os

# Caminho do arquivo de placar
score_file = "score.txt"

# Função para carregar o placar do arquivo
def load_score():
    if os.path.exists(score_file):
        with open(score_file, "r") as file:
            lines = file.readlines()
            if len(lines) == 2:
                try:
                    rounds = int(lines[0].strip())
                    wins = int(lines[1].strip())
                    return rounds, wins
                except ValueError:
                    pass
    return 0, 0

# Função para salvar o placar no arquivo
def save_score(rounds, wins):
    with open(score_file, "w") as file:
        file.write(f"{rounds}\n{wins}\n")

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
    rounds, wins = load_score()
    print(f"Placar atual: {rounds} rodadas jogadas, {wins} vitórias.")

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

        save_score(rounds, wins)

        play_again = input("Deseja jogar novamente? (s/n): ").lower()
        if play_again != "s":
            break

    print("\nPontuação final:")
    print(f"Rodadas jogadas: {rounds}")
    print(f"Vitórias: {wins}")

# Executa o jogo
if __name__ == "__main__":
    play_game()