import random
from getpass import getpass
import time

def print_intro():
    print("\n\U0001F3AE Welcome to the Ultimate Rock-Paper-Scissors Game!")
    print("1. Play with Bot\n2. Play with Friend\n3. Exit")

def decide_winner(p1, p2):
    outcomes = {
        ('rock', 'scissors'): 1,
        ('scissors', 'paper'): 1,
        ('paper', 'rock'): 1,
        ('scissors', 'rock'): 2,
        ('paper', 'scissors'): 2,
        ('rock', 'paper'): 2,
    }
    if p1 == p2:
        return 0
    return outcomes.get((p1, p2), -1)

def get_valid_move(player_name):
    while True:
        move = getpass(f"{player_name}, enter your move (rock/paper/scissors): ").lower()
        if move in ['rock', 'paper', 'scissors']:
            return move
        print("❌ Invalid move. Try again.")

def play_with_friend():
    print("\n\U0001F91D Player vs Player Mode")
    p1 = get_valid_move("Player 1")
    p2 = get_valid_move("Player 2")
    print("\n\u23F3 Deciding winner...")
    time.sleep(1)
    result = decide_winner(p1, p2)
    print(f"\nPlayer 1 chose: {p1}\nPlayer 2 chose: {p2}")
    if result == 0:
        print("\n🤝 It's a Draw!")
    elif result == 1:
        print("\n🏆 Player 1 Wins!")
    else:
        print("\n🏆 Player 2 Wins!")

def play_with_bot():
    print("\n🤖 Player vs Bot Mode")
    player = get_valid_move("You")
    bot = random.choice(['rock', 'paper', 'scissors'])
    print("\n🤖 Bot is thinking...")
    time.sleep(1)
    print(f"Bot chose: {bot}")
    result = decide_winner(player, bot)
    if result == 0:
        print("\n🤝 It's a Draw!")
    elif result == 1:
        print("\n🏆 You Win!")
    else:
        print("\n💀 Bot Wins!")

def main():
    while True:
        print_intro()
        choice = input("Choose your mode (1/2/3): ").strip()
        if choice == '1':
            play_with_bot()
        elif choice == '2':
            play_with_friend()
        elif choice == '3':
            print("\n👋 Thanks for playing. Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
        input("\nPress Enter to continue...\n")

if __name__ == "__main__":
    main()