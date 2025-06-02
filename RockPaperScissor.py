import random

# 1. Define moves
moves = ['rock', 'paper', 'scissors']

# 2. User input
user_move = input("Choose rock, paper, or scissors: ").lower()

# 3. AI decision logic (nested conditionals)
if user_move in moves:
    # AI uses weighted probabilities (optional: change weights)
    ai_move = random.choices(
        moves, 
        weights=[0.4, 0.3, 0.3],  # 40% rock, 30% paper, 30% scissors
        k=1
    )[0]
    
    print(f"AI chose: {ai_move}")

    # 4. Determine winner
    if user_move == ai_move:
        print("Tie!")
    elif user_move == 'rock':
        if ai_move == 'scissors':
            print("You win! Rock crushes scissors.")
        else:
            print("You lose! Paper covers rock.")
    elif user_move == 'paper':
        if ai_move == 'rock':
            print("You win! Paper covers rock.")
        else:
            print("You lose! Scissors cut paper.")
    elif user_move == 'scissors':
        if ai_move == 'paper':
            print("You win! Scissors cut paper.")
        else:
            print("You lose! Rock crushes scissors.")
else:
    print("Invalid move. Please choose rock, paper, or scissors.")
