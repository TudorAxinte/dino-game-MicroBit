# // The Chrome Dinosaur no internet game // BBC MicroBit edition //
# //
# // Project by Tudor Axinte, University College London
# //
from microbit import *
import random


# Coordonates & Variables
playing = False
pause = False
score = 0

playerx = 1
playery = 2
jumping = 0
playerTimer = 0

enemyx = 4
enemyy = 2
enemyCount = 0
enemyTimer = 0
enemySpeed = 8

display.scroll("PRESS B TO START / PAUSE", delay=100, wait=False, loop=True)


while playing is False:
    if button_b.is_pressed():
        playing = True
        display.clear()
        sleep(100)


# Draw the ground / Set led brightness
for i in range(0, 5):
    display.set_pixel(i, 3, 5)
for i in range(0, 5):
    display.set_pixel(i, 4, 3)

# Main Game Loop
while playing:

    if pause is False:
        # Player Movement
        if button_a.is_pressed() and playery == 2:
            jumping = 1

        display.set_pixel(playerx, playery, 0)
        if jumping == 1 and playery > 0:
            playery -= 1
        elif jumping == 1:
            if playerTimer == 7:
                playerTimer = 0
                jumping = 0
            else:
                playerTimer += 1

        if jumping == 0 and playery < 2:
            if playerTimer == 7:
                playerTimer = 0
                playery += 1
            else:
                playerTimer += 1

        # Enemy Movement

        if enemyTimer == enemySpeed:
            enemyTimer = 0
            display.set_pixel(enemyx, enemyy, 0)
            if enemyCount > 0 and enemyx > 0:
                enemyx -= 1
            elif enemyx == 0:
                enemyCount -= 1
        else:
            enemyTimer += 1

        # Spawn Enemies
        if enemyCount == 0:
            enemyCount = enemyCount + 1
            enemyx = 4
            enemyy = random.randint(0, 5)

            if enemyy >= 2:
                enemyy = 2
                enemySpeed = random.randint(2, 12)
            else:
                enemySpeed = random.randint(1, 6)

    # Pause system
    if button_b.is_pressed() and score > 5:
        if pause is True:
            pause = False
        else:
            pause = True

    # Draw Sprites
    display.set_pixel(playerx, playery, 9)
    display.set_pixel(enemyx, enemyy, 6)

    # Collision / Death
    if playerx == enemyx and playery == enemyy:
        playing = False

    print(enemySpeed)
    score += 1
    sleep(100)


# Ending
sadface = Image("99099:"
                "99099:"
                "00000:"
                "99999:"
                "90009")

display.show(sadface)
sleep(2000)
display.scroll("SCORE: " + str(score), loop=True)