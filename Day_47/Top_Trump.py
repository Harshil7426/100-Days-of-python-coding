import random

# Define the 2D dictionary for the "Top Trump" cards
Top_Trump = {
    "Dinesh": {"Intelligence": 100, "Speed": 50, "Guile": 50, "Baldness": 0},
    "Ram": {"Intelligence": 100, "Speed": 50, "Guile": 50, "Baldness": 0},
    "Krishna": {"Intelligence": 100, "Speed": 50, "Guile": 50, "Baldness": 0},
    "Shyam": {"Intelligence": 100, "Speed": 50, "Guile": 50, "Baldness": 0}
}

# Function to display the Top Trump cards
def prettyPrint():
    print()
    for key, value in Top_Trump.items():
        print("\n" + key, end=": ")
        for subKey, subValue in value.items():
            print(subKey, "->", subValue, end=" | ")
    print()

# Infinite loop for user interaction
while True:
    print("\nAvailable Top Trump Cards:")
    prettyPrint()

    # Get user's choice of the first card
    chosen_card = input("\nPick the first card by typing its name (or type 'exit' to quit): ").strip()
    if chosen_card.lower() == "exit":
        break
    elif chosen_card not in Top_Trump:
        print("Invalid choice. Try again.")
        continue

    # Randomly pick the second card that is not the chosen one
    opponent_name = random.choice([name for name in Top_Trump if name != chosen_card])

    # Show the available stats
    print("\nStats available to compare:")
    for stat in Top_Trump[chosen_card]:
        print(stat)

    # Get user's stat choice
    chosen_stat = input("\nPick a stat to compare: ").strip()
    if chosen_stat not in Top_Trump[chosen_card]:
        print("Invalid stat. Try again.")
        continue

    # Get values for chosen stat
    chosen_value = Top_Trump[chosen_card][chosen_stat]
    opponent_value = Top_Trump[opponent_name][chosen_stat]

    # Display the result
    print(f"\n{chosen_card}'s {chosen_stat}: {chosen_value}")
    print(f"{opponent_name}'s {chosen_stat}: {opponent_value}")

    # Determine the winner
    if chosen_value > opponent_value:
        print(f"{chosen_card} wins!")
    elif chosen_value < opponent_value:
        print(f"{opponent_name} wins!")
    else:
        print("It's a tie!")
