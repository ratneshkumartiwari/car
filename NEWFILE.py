import pygame


#game initialising
pygame.init()

#display
screen = pygame.display.set_mode((1500,640))

#background
background = pygame.image.load("newbg.png")

#players car
car = pygame.image.load("car.png")
carX = 710
carY  = 320
car_changeX = 0
car_changeY = 0


#trees
tree = pygame.image.load("trees.png")
treeX = 90
treeY = 250

def player(x,y):
    screen.blit(car, (x,y))
def forest(x,y):
    screen.blit(background, (x,y))









running = True
while running:
    screen.blit(background, (0, 0))
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

    forest(treeX, treeY)


    player(carX, carY)
    pygame.display.update()
