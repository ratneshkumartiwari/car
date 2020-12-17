import pygame
import random


#game initialising
pygame.init()

#display
screen = pygame.display.set_mode((1500,640))

distance = 0

#background
background = pygame.image.load("newbg.png")

#players car
car = pygame.image.load("car.png")
carX = 710
carY  = 320
car_changeX = 0
car_changeY = 0

#police jeep
jeep = pygame.image.load("jeep.png")
jeepX = random.randint(533,815)
jeepY = 30
jeep_change = 20




#stripe
stripe = pygame.image.load("stripe.png")
stripeX = 727
stripeY = 30
k = 230
l = 430
m = 630
stripeY_change = 10

#trees
tree = pygame.image.load("trees.png")
treeX = 50
treeY = 150

treeY_change = 10


tree2 = pygame.image.load("trees2.png")
tree2X = 50
tree2Y = 450

tree2Y_change = 10

def player(x,y):
    screen.blit(car, (x,y))
def forest(x,y):
    screen.blit(tree, (x,y))
def forest2(x,y):
    screen.blit(tree2 , (x,y))


def stp(x,y):
    screen.blit(stripe, (x,y))

def jp(x,y):
    screen.blit(jeep, (x,y))

def collision(jeepX,jeepY,carX,carY):
    distance = ((jeepX - carX)**2 + (jeepY - carY)**2)**0.5
    if distance<= 40:
        return True





running = True
while running:
    screen.blit(background, (0, 0))
    stp(stripeX, stripeY)
    stripeY += stripeY_change
    if stripeY == 660:
        stripeY = -20

    stp(727, k)
    k += stripeY_change
    if k == 660:
        k = -20

    stp(727, l)
    l += stripeY_change
    if l == 660:
        l = -20
    stp(727,m)
    m += stripeY_change
    if m == 730:
        m = -20


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_changeX = 10
            if event.key == pygame.K_LEFT:
                car_changeX = -10
            if event.key == pygame.K_UP:
                car_changeY = - 10
            if event.key == pygame.K_DOWN:
                car_changeY = 10

        if event.type == pygame.KEYUP:
            car_changeX = 0
            car_changeY = 0

    carY += car_changeY
    carX += car_changeX


    if carX <= 533:
        carX = 533
    if carX >= 815:
        carX = 815

    if carY >= 512:
        carY = 512
    if carY <= 0:
        carY = 0

    jeepY += jeep_change

    if jeepY >= 780:
        jeepY = -20
        jeepX =  random.randint(533,815)



    forest(treeX, treeY)

    forest(tree2X,tree2Y)

    forest2(1050, treeY)
    forest2(1050, tree2Y)


    treeY+= treeY_change


    tree2Y += tree2Y_change

    if treeY == 680:
        treeY = -20

    if tree2Y == 680:
        tree2Y = -20

    clsn = collision(jeepX,jeepY,carX,carY)
    if clsn == True:
        jeepX = random.randint(533,815)
        jeepY = 0


    player(carX, carY)
    jp(jeepX,jeepY)
    pygame.display.update()