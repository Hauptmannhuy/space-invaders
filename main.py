import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1080))
running = True

y,x = 700,800
width,height = 50,50

end_projectile_y, end_projectile_x = y,x
fps = pygame.time.Clock()

shot = False
start_projectile_x = start_projectile_y = end_projectile_y = end_projectile_x = 0

while (running):
  fps.tick(60)
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
      
  screen.fill('black') 
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    y-= 8
  elif keys[pygame.K_s]:
    y+= 8
  elif keys[pygame.K_a]:
    x-= 8
  elif keys[pygame.K_d]:
    x+= 8
  
  if keys[pygame.K_SPACE]:
    if not shot:
      start_projectile_x = x+width/2
      start_projectile_y = y
      end_projectile_y = start_projectile_y-850
      shot = True
  
  if(shot == True and start_projectile_y > end_projectile_y):
    start_projectile_y-=20
    pygame.draw.line(screen,'red',(start_projectile_x,start_projectile_y),(start_projectile_x,start_projectile_y-20),5)
  else:
    shot = False
    
      
  pygame.draw.rect(screen,'yellow',pygame.Rect(x,y,width,height))
  pygame.display.update()

pygame.quit()