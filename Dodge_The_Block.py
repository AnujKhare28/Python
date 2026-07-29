import pygame as p

class Paddle(p.sprite.Sprite):

    def __init__(self, x):
        super().__init__()
        self.x = x
        self.y = 300
        self.speed = 8
        self.image = p.image.load('paddle.png')
        self.image = p.transform.scale(self.image, (130, 24))
        self.rect = self.image.get_rect()

    def update(self):
        x, _ = p.mouse.get_pos()
        self.x = x
        self.rect.center = (self.x, self.y)

p.init()

WIDTH = 600
HEIGHT = 540

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Dodge the Blocks!')
clock = p.time.Clock()

paddle_group = p.sprite.Group()
paddle = Paddle(WIDTH/2)
paddle_group.add(paddle)

run = True

while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    win.fill((0,0,0))

    paddle_group.draw(win)

    paddle_group.update()


    p.display.update()

p.quit()