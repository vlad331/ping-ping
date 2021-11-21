from pygame import *
from random import randint

from time import time as timer
window = display.set_mode((700, 500))
display.set_caption("tipo shuter")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
lost = 0
score = 0
num_fire=0
healf = 3
rel_time=False
FPS = 144
Bullets = sprite.Group()
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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
    def fire(self):
            Bullet=Bullets1 ("Bullet.png",player.rect.centerx - 6,player.rect.top + 2,-4,15,15)
            Bullets.add(Bullet)
            
class enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y < 435:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = -70
            self.rect.x = randint(20,450)
            lost = lost + 1
class Astro(GameSprite):
    def update(self):
        if self.rect.y < 435:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = -70
            self.rect.x = randint(20,450)


class Bullets1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()

        
monsters = sprite.Group()
for i in range(1,6):
    monster=enemy("ufo.png",randint(50,650),10,randint(1,2),65,65)
    monsters.add(monster)
astros = sprite.Group()
for i in range(1,3):
    astro=Astro("asteroid.png",randint(50,650),10,randint(1,2),65,65)
    astros.add(astro)

player = Player("rocket.png", 350, 400, 7,65,65)
font.init()
font = font.Font(None, 35)
game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                if num_fire<5 and rel_time==False:
                    num_fire=num_fire+1
                    player.fire()
                if num_fire>=5 and rel_time==False:
                    last_time = timer()
                    rel_time=True
    if not finish:
        clock = time.Clock()
        clock.tick(FPS)
        Bullets.update()
        player.update()
        monsters.update()
        astros.update()

        window.blit(background,(0, 0))
        lose1 = font.render('Проиграл ',1,(255,255,255))
        win1 = font.render('Выйграл',1,(255,255,255))
        lose = font.render('Пропущено: '+str(lost),1,(255,255,255))
        win = font.render('Убито: '+str(score),1,(255,255,255))
        live = font.render('Жизни: '+str(healf),1,(255,255,255))
        window.blit(lose,(5,25))
        window.blit(win,(5,50))
        window.blit(live,(5,75))
        Bullets.draw(window)
        player.reset()
        astros.draw(window)
        monsters.draw(window)

        if rel_time ==True:
            now_time=timer()
            if now_time-last_time<3:
                Reload=font.render("ПЕРЕЗАРЯДКА",1,(150,0,0))
                window.blit(Reload,(5,75))
            else:
                num_fire = 0 
                rel_time = False
        collides = sprite.groupcollide(monsters,Bullets,True,True)
        for i in collides:
            score = score+1
            monster=enemy("ufo.png",randint(50,650),10,randint(1,2),65,65)
            monsters.add(monster)
        collides1 = sprite.spritecollide(player,astros,True)
        
        for i in collides1:
            healf = healf-1
            astro=Astro("asteroid.png",randint(50,650),10,randint(1,2),65,65)
            astros.add(astro)
        if healf == 0:
            window.blit(lose1,(350,250))
            finish = True
        if score == 5:
            window.blit(win1,(350,250))
            finish = True
        if lost == 10:
            window.blit(lose1,(350,250))
            finish = True
        key_pressed = key.get_pressed()
        display.update() 
