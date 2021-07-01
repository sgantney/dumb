import pygame
from network import Network
import pickle
from player import Player

width, height = 900, 500
pygame.display.set_caption("Dumb")
win = pygame.display.set_mode((width, height))


def reddrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        reddrawWindow(win, p, p2)

if __name__ == "__main__":
    main()