# Activity 7 - Reaction Game

from adafruit_clue import clue
from time import time,sleep
from random import randint
clue_display = clue.simple_text_display(title="REACTION GAME", title_color=(255,255 ,0 ), title_scale=2)

while True:
    clue_display[2].text = "Instructions:"
    clue_display[2].color = clue.GREEN
    clue_display[2].scale = 2
    clue_display[4].text = "Player A presses A"
    clue_display[4].color = clue.WHITE
    clue_display[4].scale = 2
    clue_display[6].text = "Player B presses B"
    clue_display[6].color = clue.WHITE
    clue_display[6].scale = 2
    clue_display[8].text = "Press if the number"
    clue_display[8].color = clue.SKY
    clue_display[8].scale = 2
    clue_display[10].text = "is divisible by 2."
    clue_display[10].color = clue.SKY
    clue_display[10].scale = 2
    clue_display[12].text = "Maximum score of 5"
    clue_display[12].color = clue.YELLOW
    clue_display[12].scale = 2

    for i in range(3, 0, -1): 
        clue_display[14].text = "Starts in " + str(i)
        clue_display[14].color = clue.RED
        clue_display[14].scale = 2
        sleep(2) 
       
        
        a = 0 
        b = 0 
        if i == 1:
            while True:
                random = randint(1, 100) 
                clue_display[2].text = "" 
                clue_display[4].text = "" 
                clue_display[6].text = "" 
                clue_display[8].text = "" 
                clue_display[10].text = ""
                clue_display[12].text = "Player A score: " + str(a)
                clue_display[12].color = clue.GREEN
                clue_display[14].text = "Player B score: " + str(b)
                clue_display[14].color = clue.SKY
                clue_display[4].text = "        " + str(random)

                time1 = time()
                time2 = time()
                ctr = 1
                while ctr > 0:
                    if time2 - time1 >= 1: 
                        ctr = 0 
                    else: 
                        time2 = time() 

                    if clue.button_a:
                        if random % 2 == 0:
                            a +=1
                        else: 
                            a -=1
                        break
                    if clue.button_b:
                        if random % 2 == 0:
                            b +=1 
                        else:
                            b -=1
                        break    

                if a == 5:
                    clue_display[12].text = "Player A score: " + str(a)
                    clue_display[2].text = "Player A WINS!" 
                    clue_display[2].color = clue.RED 
                    break 
                if b == 5:
                    clue_display[14].text = "Player B score: " + str(b)
                    clue_display[2].text = "Player B WINS!" 
                    clue_display[2].color = clue.RED 
                    break 
            sleep(10) 
        clue_display.show()