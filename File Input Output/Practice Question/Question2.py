import random
import time

def game():
    print("He is play the game write now")
    time.sleep(2)
    newscore = random.randrange(1, 1000, 10)
    return newscore


newscore = game()

with open("Highscore.txt", "a+") as f:
    f.seek(0)
    oldscore = f.read().strip()

    print("Newscore: ", newscore)
    print("Oldscore: ", oldscore)

    if oldscore == "":
        f.seek(0)
        f.truncate()
        f.write(str(newscore))

    elif newscore >= int(oldscore):
        print("His high score is ", newscore)
        f.seek(0)
        f.truncate()
        f.write(str(newscore))

    else:
        print("His high score is ", oldscore)

