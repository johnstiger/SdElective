from adafruit_clue import clue
from time import sleep

# myTitle = clue.simple_text_display(title= "Message Streamer", title_scale= 3 , title_color= (clue.RED,))


clue_display = clue.simple_text_display(text_scale=2,)
message1 = " This message move from right to left "
message2 =  " This message moves from left to right "

while True:
    clue_display[0].text = "Message Streamer"
    clue_display[0].color = clue.RED

    clue_display[2].text = message1
    clue_display[2].color = clue.YELLOW

    temp = message1[0]
    message1 = message1[1:] + temp

    clue_display[4].text = message2
    clue_display[4].color = clue.WHITE

    temp = message2[len(message2)-1]
    message2 = temp + message2[:-1] 

    clue_display[6].text = "This message blinks"
    clue_display[6].color = clue.SKY
    clue_display.show()
    sleep(0.5)
    clue_display[6].color = clue.BLACK  
    












    