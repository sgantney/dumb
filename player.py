import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = .1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x -= self.width/2
        mouse_y -= self.height/2
        left, middle, right = pygame.mouse.get_pressed(num_buttons=3)
        if left:
            self.color = (255, 0, 0)
            x_dist = abs(mouse_x - self.x)
            y_dist = abs(mouse_y - self.y)
            if mouse_x < self.x:
                self.x -= self.vel * x_dist
            if mouse_x > self.x:
                self.x += self.vel * x_dist
            if mouse_y < self.y:
                self.y -= self.vel * y_dist
            if mouse_y > self.y:
                self.y += self.vel * y_dist
        else:
            self.color = (0, 255, 0)
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)