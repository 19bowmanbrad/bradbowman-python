import pygame


pygame.init()


display_width = 512
display_height = 512

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Brad's game")

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

car_width = 73
car_height = 73


clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load("/home/19bowmanbradley@bprep.org/Downloads/racecar.png")
backGround = pygame.image.load("/home/19bowmanbradley@bprep.org/Downloads/road.png")
backGround2 = pygame.image.load("/home/19bowmanbradley@bprep.org/Downloads/road.png")


def car(x,y):
    gameDisplay.blit(backGround, (0,bgY))
    gameDisplay.blit(backGround2, (0, (bgY + display_height)))
    gameDisplay.blit(backGround2, (0, (bgY - display_height)))
    gameDisplay.blit(carImg, (x,y))


bgX = display_width
bgY = 0
bgY2 = 0


x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
bgY_change = 0
car_speed = 0


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if (x > 355 or x < 70):
                bgY_change = -5
            # elif (x < 355 and x > 70):
            #     bgY_change = -10
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP and x < 355 and x > 70:
                y_change = -5
                bgY_change = -10
            elif event.key == pygame.K_DOWN:
                y_change = 5
            # bgY_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0

    x += x_change
    y += y_change
    bgY -= bgY_change
    # print(bgY)
    print (x)
    gameDisplay.fill(white)
    car(x,y)

    if x > display_width - car_width:
            x = display_width - car_width
    elif x < 0:
        x = 0

    if y > display_height - car_height:
        y = display_height - car_height
    elif y < 0:
        y = 0

    if bgY > display_height:
        bgY = display_height * -1
    elif bgY2 < display_height:
        bgY2 = display_height


    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
