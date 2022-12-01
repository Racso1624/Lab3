from OpenGL.GL import *
import pygame
import numpy as np
import random

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Conway's Game Of Life")

state = np.zeros((20, 10), dtype=int)

for s in range(random.randint(1, 10)):
    state[random.randint(0, len(state) - 1)][random.randint(0, len(state[0]) - 1)] = 1

var = True
while var:
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    next_state = [[0 for x in range(len(state[0]))] for y in range(len(state))]
    color = (1.0, 1.0, 1.0, 1.0)

    for x in range(len(next_state)):
        for y in range(len(next_state[0])):
            cell = state[x][y]
            rows = state[(x - 1) : (x + 2)]
            neighbor_cells = []

            for row in rows:
                neighbor_cells.append(row[(y - 1) : (y + 2)])

            count = sum([sum(row) for row in neighbor_cells]) - cell

            if (state[x][y] == 1) and ((count < 2) or (count > 3)):
                color = (0.0, 0.0, 0.0, 1.0)
            elif ((state[x][y] == 1) and (2 <= count <= 3)) or ((state[x][y] == 0) and (count == 3)):
                next_state[x][y] = 1
                color = (0.0, 0.0, 0.0, 1.0)
            

            glEnable(GL_SCISSOR_TEST)
            glScissor(x, y, 10, 10)
            glClearColor(*color)
            glClear(GL_COLOR_BUFFER_BIT)
            glDisable(GL_SCISSOR_TEST)

    state = next_state

    pygame.display.flip()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            var = False