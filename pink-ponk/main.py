from pygame import *
window = display.set_mode((700, 500))
display.set_caption("tipo ping-pong")
background = transform.scale(image.load("blue.png"), (700, 500))
FPS = 144
ball_speed_x = 3
ball_speed_y = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 40:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 40:
            self.rect.y += self.speed


player = Player("tarelka.png", 5, 250, 7,65,65)
player1 = Player("tarelka.png", 650, 250, 7,65,65)
ball = GameSprite("images.jpg",350,250,3,65,65)
game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish:
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        if  ball.rect.y > 500-40 or ball.rect.y < 0:
            ball_speed_y *=-1
        if sprite.collide_rect(player,ball) or sprite.collide_rect(player1,ball):
            ball_speed_x *= -1
        clock = time.Clock()
        clock.tick(FPS)
        player.update()
        player1.update1()
        window.blit(background,(0, 0))
        ball.reset()
        player.reset()
        player1.reset()
        display.update() 
