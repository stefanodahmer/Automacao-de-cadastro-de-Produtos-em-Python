import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('...')
pygame.mixer.music.play()
pygame.event.wait()

