import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=== 🎮 Rock Paper Scissors Game ===")

while True:
    print("\nChoose: rock / paper / scissors (or 'q' to quit)")
    user = input("Your choice: ").lower()

    # exit option
    if user == 'q':
        print("👋 Exiting game...")
        break

    # validation
    if user not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"\n🧑 You chose     : {user}")
    print(f"💻 Computer chose: {computer}")

    # game logic
    if user == computer:
        print("🤝 It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("🎉 You win!")
        user_score += 1
    else:
        print("💻 Computer wins!")
        computer_score += 1

    # score display
    print(f"\n📊 Score → You: {user_score} | Computer: {computer_score}")

    # play again
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break