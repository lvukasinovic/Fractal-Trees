import pygame
import math

pygame.init()

# Sets up screen and some definitions
WIDTH, HEIGHT = (500, 500)
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Trees")

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
screen.fill(WHITE)
pygame.display.update()


# Takes in initial x1, y1 coordinates, length of the branch, the angle to draw the branches at, and how many branches
def drawTrees(x1, y1, length, angleRad, level):
    if level == 0:
        return

    # Gets x2, y2 coordinates
    x2 = x1 + int((math.cos(angleRad)) * length)
    y2 = y1 + int((math.sin(angleRad)) * length)

    # Draws current branch
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 1)
    pygame.display.update()
    pygame.time.delay(20)

    # Recursively calls method to finish every branch
    drawTrees(x2, y2, length / 2, angleRad + math.pi / 6.0, level - 1)
    drawTrees(x2, y2, length / 2, angleRad + math.pi / 3.0, level - 1)
    drawTrees(x2, y2, length / 2, angleRad, level - 1)
    drawTrees(x2, y2, length / 2, angleRad - math.pi / 6.0, level - 1)
    drawTrees(x2, y2, length / 2, angleRad - math.pi / 3.0, level - 1)


drawTrees(WIDTH / 2, HEIGHT, 200, -math.pi / 2, 5)
