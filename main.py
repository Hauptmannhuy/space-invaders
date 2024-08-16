import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1080))
running = True

y,x = 700,800
width,height = 50,50

start_projectile_y, start_projectile_x = y,x
fps = pygame.time.Clock()

while (running):
  fps.tick(60)
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
      
  screen.fill('black') 
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] == True:
    y-= 8
  elif keys[pygame.K_s] == True:
    y+= 8
  elif keys[pygame.K_a] == True:
    x-= 8
  elif keys[pygame.K_d] == True:
    x+= 8
  elif keys[pygame.K_SPACE] == True:
    pygame.draw.line(screen,'red',(x+width/2,y-10),(x+width/2,y-40),5)
  pygame.draw.rect(screen,'yellow',pygame.Rect(x,y,width,height))
  pygame.display.update()

pygame.quit()