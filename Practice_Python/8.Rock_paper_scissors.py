player1_score = 0
player2_score = 0

while player1_score or player2_score < 5:
    player1 = input("Player 1, Please choose rock, paper or scissors: ")
    player2 = input("Player 2, Please choose rock, paper or scissors: ")
    if player1 == 'rock' and player2 == 'scissors':
        print("Player 1 wins!")
        player1_score += 1
    elif player1 == 'rock' and player2 == 'paper':
        print("Player 2 wins!")
        player2_score += 1
    elif player1 == 'rock' and player2 == 'rock':
        print("Its a Draw!")
    elif player1 == 'scissors' and player2 == 'scissors':
        print("Its a Draw!")
    elif player1 == 'scissors' and player2 == 'rock':
        print("Player 2 wins!")
        player2_score += 1
    elif player1 == 'scissors' and player2 == 'paper':
        print("Player 1 wins!")
        player1_score += 1
    elif player1 == 'paper' and player2 == 'paper':
        print("Its a Draw!")
    elif player1 == 'paper' and player2 == 'scissors':
        print("Player 2 wins!")
        player2_score += 1
    elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 wins!")
        player1_score += 1

