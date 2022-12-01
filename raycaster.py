from OpenGL.GL import *
import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Conway's Game Of Life")

