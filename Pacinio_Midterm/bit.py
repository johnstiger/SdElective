from microbit import *

dot1 = Image("90000:09000:00900:00009")
dot2 = Image("09000:00900:00090:00009:90000")
dot3 = Image("00900:00090:0000:90000:09000")
dot4 = Image("00090:00009:90000:09000:00900")
dot5 = Image("00009:90000:09000:00900:00090")

all_dots = [dot1,dot2,dot3,dot4,dot5]
display.show(all_dots, loop = True, delay = 1000)
    