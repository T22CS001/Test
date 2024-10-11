import random

# Function to simulate a Rock-Paper-Scissors game with 3 rounds
def rock_paper_scissors_best_of_three():
    choices = ['Rock', 'Paper', 'Scissors']
    player_wins = 0
    computer_wins = 0
    rounds_played = 0

    # Play 3 rounds
    while rounds_played < 3:
        # Randomly choosing for player and computer
        player_choice = random.randint(0, 2)
        computer_choice = random.randint(0, 2)

        player_choice_str = choices[player_choice]
        computer_choice_str = choices[computer_choice]

        # Deciding the winner of the round
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            result = "A wins!"
            player_wins += 1
        else:
            result = "B wins!"
            computer_wins += 1

        # Print the result of the current round
        print(f"Round {rounds_played + 1}: A's hand: {player_choice_str} vs. B's hand: {computer_choice_str} → {result}")
        rounds_played += 1

    # Final result after 3 rounds
    if player_wins > computer_wins:
        final_result = "A is the overall winner!"
    elif computer_wins > player_wins:
        final_result = "B is the overall winner!"
    else:
        final_result = "It's a tie after 3 rounds!"

    return final_result

# Run the best of 3 simulation
print(rock_paper_scissors_best_of_three())
