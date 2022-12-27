import pygame

# init
pygame.init()

# variable running game
isRun = True

speed = 10

# Membuat display surface object
win_x = 500
win_y = 500

window = pygame.display.set_mode((win_x,win_y))

# object game
red = 255
green = 255
blue = 255
color_box = (red,green,blue)

# box
x = win_x/2
y = win_y/2
size_box = lebar = panjang = 20

def random_color(col):
    if col >= 0 and col <= 255:
         

while isRun:
    pygame.time.delay(50)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LCTRL] and (y > 0 and x > 0):
        speed = 20
    else:
        speed = 10

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_DOWN] and y < win_y-panjang:
        y += speed

    if keys[pygame.K_RIGHT] and x < win_x-lebar:
        x += speed
    
    
    
    window.fill((255,255,255))
    pygame.draw.rect(window,color_box,(x,y,lebar,panjang))
    # pygame.draw.polygon(window,(255,0,0),[(255,255),(100,100),(300,300)],width=10)


    # render ke display
    pygame.display.update()

pygame.quit()

# user input, databasepip list
