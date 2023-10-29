# Prompting the user to enter information related to their golf game.
player_name = input("Enter player's name: ")
score = input("Enter the player's score: ")
date = input("Enter the date of the game: ")

# Opening the file in write mode to write data inside
with open("golf_scores.txt", mode="w") as file:
    # Writing the information given above to the file
    file.write(f"Player Name: {player_name}\n")
    file.write(f"Score: {score}\n")
    file.write(f"Date of the Game: {date}\n")