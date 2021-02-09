from adafruit_clue import clue
from time import sleep

# myTitle = clue.simple_text_display(title= "Message Streamer", title_scale= 3 , title_color= (clue.RED,))


clue_display = clue.simple_text_display(text_scale=2,)
msg1 = " This is a message."

while True:

    clue_display[2].text = msg1
    clue_display[2].color = clue.CYAN

    temp = msg1[0]
    msg1 = msg1[1:] + temp

    clue_display.show()
    sleep(1)
    clue_display[2].color = clue.BLACK 

    



