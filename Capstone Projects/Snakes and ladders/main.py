import pygame
from random import randint

pygame.init()
screen_width = 457
screen = pygame.display.set_mode((screen_width, screen_width))
background = bg = pygame.image.load("snakes_and_ladders_board.png")


x_positions = [(x * 45.5 + 25) for x in range(10)]
y_positions = [457 - (y * 45.5 + 25) for y in range(10)]

ladders = [[1, 38], [4, 14], [8, 30], [21, 42], [28, 76], [50, 67], [71, 92], [80, 99]]
snakes = [[32, 20], [36, 6], [48, 26], [62, 18], [88, 24], [95, 56], [97, 78]]

square_number = 0
number_of_rolls = 0


def roll_dice():
    return randint(1, 6)


def position(num):
    row = (num-1) // 10
    if row % 2 != 0 and num > 10:
        column = 10 - (num - ((num-1) // 10) * 10)
    else:
        column = num - ((num-1)//10) * 10 - 1
    return [column, row]


def position_to_pixels(x_y):
    return x_positions[x_y[0]], y_positions[x_y[1]]


# Script
print("Click space to roll")
started = False
run = True
while run:

    screen.blit(background,(-17, -17))
    if started:
        pygame.draw.circle(screen, (117, 18, 163), position_to_pixels(position(square_number)), 15)
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            started = True

            if event.key == pygame.K_SPACE:
                print("\n")
                number_of_rolls += 1
                print(f'Roll number: {number_of_rolls}')
                roll = roll_dice()
                square_number += roll
                print(f"You rolled a {roll}")
                if square_number < 100:
                    print(f"Current square: {square_number}")
                if square_number >= 100:
                    print(f"You win in {number_of_rolls} rolls!")
                    run = False
                    break

                for squares in ladders:
                    if square_number == squares[0]:
                        print(f"LADDER to {squares[1]}")
                        square_number = squares[1]
                for squares in snakes:
                    if square_number == squares[0]:
                        print(f"SNAKE to {squares[1]}")
                        square_number = squares[1]

        if event.type == pygame.QUIT:
            run = False
    if run:
        pygame.display.update()
pygame.quit()

