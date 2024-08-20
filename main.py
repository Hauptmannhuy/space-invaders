import pygame
import projectile_object

pygame.init()

screen = pygame.display.set_mode((1920,1080))
running = True


y,x = 700,800
width,height = 50,50
projectiles = []

end_projectile_y = y
fps = pygame.time.Clock()

start_projectile_x = start_projectile_y = end_projectile_y = 0

while (running):
  fps.tick(60)
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        start_projectile_x = x+width/2
        start_projectile_y = y
        end_projectile_y = start_projectile_y-850
        projectile = projectile_object.Projectile(start_projectile_x,start_projectile_y,end_projectile_y)
        projectiles.append(projectile)
        
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    y-= 8
  elif keys[pygame.K_s]:
    y+= 8
  elif keys[pygame.K_a]:
    x-= 8
  elif keys[pygame.K_d]:
    x+= 8
  
  

  screen.fill('black')
  
  
  for projectile in projectiles:
    if projectile.reached_destination() is False:      
      projectile.start_y-=20
      projectile_start_x = projectile.start_x
      projectile_start_y = projectile.start_y
      projectile_end_y = projectile.end_y
      pygame.draw.line(screen,'red',(projectile_start_x,projectile_start_y),(projectile_start_x,projectile_start_y-20),5)
  
  for projectile in projectiles:
    if projectile.reached_destination():
      projectiles.remove(projectiles[0])  
      
      
  pygame.draw.rect(screen,'yellow',pygame.Rect(x,y,width,height))
  pygame.display.update()
pygame.quit()