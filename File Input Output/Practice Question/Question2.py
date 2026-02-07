# The game() function in a program lets a user play a game and returns the score as an integer .You need to read a file "hiscore.txt"which is either blank or contains the previous high-score where game() breaks the High-score.
import random
import time

def game():
    print("He is play the game write now")
    # time.sleep(5)
    newscore = random.randrange(1, 1000,10)
    return newscore

newscore = game()
with open("Highscore.txt","r+") as f:
    oldscore = int(f.read())
    print("Newscore: ",newscore)
    print("Oldscore: ",oldscore)
    if(oldscore==""):
        f.write(newscore)
    elif(newscore>=oldscore):
        print("His high score is ",newscore)
        f.write(newscore)
    else:
        print("His high score is ",oldscore)
        f.write(oldscore)
