import pygame, sys

score = 0
lost = False

class enemy(object): #definition of enemy object class
    def __init__(self, x, y, size, width): #initialing parameters of enemy
        self.vec = 0.2
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.pos = [self.x, self.y]
        self.enemyS = pygame.image.load("enemy.png")
        self.enemyR = self.enemyS.get_rect()
        self.enemyR.center = self.pos
        self.screen = pygame.display.set_mode(self.size)
        self.counter = 0

    def spawner(self): #function for drawing enemy on screen
        screen.blit(self.enemyS, self.enemyR)

    def move(self): #function for changing x and y of enemy and for making enemy "die"
        deleted = False
        if deleted == False:
            if self.x > width:
                self.vec = -0.2
                self.y = self.y + 10
            if self.x < 0:
                self.vec = 0.2
                self.y = self.y + 10
            self.x = self.x + self.vec
            self.pos = [self.x, self.y]
            self.enemyR.center = self.pos
            #if bullet is iny enemy "hitbox" then change it position to somewhere not located in screen and add 1 to score
            if bulletrect.center[0] > self.enemyR.left and bulletrect.center[0] < self.enemyR.right and \
                    bulletrect.center[1] > self.enemyR.top and bulletrect.center[1] < self.enemyR.bottom:
                #print("hit!", score)
                can = True
                bulletrect.center = bulletPos
                self.x = -400
                self.y = -400
                self.pos = [self.x, self.y]
                self.enemyR.center = self.pos
                deleted = True
                global score
                score = score + 1
            # If player is in enemy hit box, game is lost
            if shiprect.center[0] > self.enemyR.left and shiprect.center[0] < self.enemyR.right and \
                    shiprect.center[1] > self.enemyR.top and shiprect.center[1] < self.enemyR.bottom:
                global lost
                lost = True

#initialing game, setting up player, and it speed
pygame.init()
pygame.display.set_caption('Space Invaders!')
font = pygame.font.Font('freesansbold.ttf', 16)
size = width, height = 512, 512
screen = pygame.display.set_mode(size)
ship = pygame.image.load("ship.png")
shiprect = ship.get_rect()
speedCh = [1, 0]

can = True # variable for shooting, if can == True, you can shoot a bullet

red = 255, 0, 0
mypos = [260, 490]
shiprect.center = mypos
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

scoreTxt = font.render("Score : ", True, green, blue)
scoreTxtrect = scoreTxt.get_rect()
scoreTxtPos = [30, 10]
scoreTxtrect.center = scoreTxtPos
scoreString = str(score)
sc = font.render(scoreString, True, green, blue)
scrc = sc.get_rect()
scpos = [70, 10]
scrc.center = scpos




#################################################
bullet = pygame.image.load("bullet.png")  #
bulletrect = bullet.get_rect()  #
bulletPos = [-700, -700]  #
bulletrect.center = bulletPos  #
#################################################

##################################################
#Creating enemies objects
##################################################

enemy1 = enemy(150, 100, size, width)
enemy2 = enemy(200, 100, size, width)
enemy3 = enemy(250, 100, size, width)
enemy4 = enemy(300, 100, size, width)
enemy5 = enemy(175, 150, size, width)
enemy6 = enemy(225, 150, size, width)
enemy7 = enemy(275, 150, size, width)
enemy8 = enemy(225, 200, size, width)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()

    if score < 8 and lost == False:
        scoreString = str(score)
        sc = font.render(scoreString, True, green, blue)
        scrc = sc.get_rect()
        scpos = [70, 10]
        scrc.center = scpos

        pygame.time.delay(2)


        if key[pygame.K_LEFT]:
            if shiprect.left > 0: shiprect = shiprect.move(-speedCh[0], speedCh[1])
        if key[pygame.K_RIGHT]:
            if shiprect.right < width: shiprect = shiprect.move(speedCh)
        if key[pygame.K_SPACE]:
            if can == True:
                bulletrect.center = shiprect.center
                can = False
        if can == False:
            bulletrect = bulletrect.move(0, -1)
        if bulletrect.top < 0:
            can = True
            bulletrect.center = bulletPos
        screen.fill(red)
        screen.blit(ship, shiprect)
        screen.blit(bullet, bulletrect)
        screen.blit(scoreTxt, scoreTxtrect)
        screen.blit(sc, scrc)
        enemy1.spawner()
        enemy2.spawner()
        enemy3.spawner()
        enemy4.spawner()
        enemy5.spawner()
        enemy6.spawner()
        enemy7.spawner()
        enemy8.spawner()
        enemy1.move()
        enemy2.move()
        enemy3.move()
        enemy4.move()
        enemy5.move()
        enemy6.move()
        enemy7.move()
        enemy8.move()
        pygame.display.flip()
    if lost == True :
        font = pygame.font.Font('freesansbold.ttf', 32)
        won = font.render("You Lost :C !", True, green, blue)
        wonrect = won.get_rect()
        wonPos = [300, 300]
        wonrect.center = wonPos
        screen.fill(red)
        screen.blit(won, wonrect)
        pygame.display.flip()
    if score == 8 and lost == False:
        font = pygame.font.Font('freesansbold.ttf', 32)
        won = font.render("congratulation! You won!", True, green,blue)
        wonrect = won.get_rect()
        wonPos = [300, 300]
        wonrect.center = wonPos
        screen.fill(red)
        screen.blit(won, wonrect)
        pygame.display.flip()
