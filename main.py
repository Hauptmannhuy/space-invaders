import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1920,1080))
running = True

obstacle_movement = []
obstacles = []

y,x = 700,800
width,height = 50,50

projectiles = []
end_coords = []
end_projectile_y = y


for _ in range(6):
  obstacle = pygame.Rect(random.randrange(0,1920),0,50,50)
  obstacles.append(obstacle)
  
for obstacle in obstacles:
  obstacle_x_start = obstacle.left
  obstacle_movement.append({'left': obstacle_x_start-150, 'right': obstacle_x_start+150, 'turn': 'left'})
  
fps = pygame.time.Clock()


def reached_destination(projectile,end_coord_y):
  return True if projectile.top < end_coord_y else False

while (running):
  fps.tick(40)
  
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        start_projectile_x = x+width/2
        start_projectile_y = y
        end_projectile_y = start_projectile_y-850
        projectile = pygame.Rect(start_projectile_x,start_projectile_y,5,15)      
        projectiles.append(projectile)
        end_coords.append(end_projectile_y)
        
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

            
  color_obstacle = 'blue'
  for i in range(len(projectiles)):
    projectile = projectiles[i]
    end_coord_y = end_coords[i]
    if reached_destination(projectile, end_coord_y) is False:     
      projectile.top-=20
      pygame.draw.rect(screen,'red',projectile)
  
  for i in range(len(projectiles)):
    if reached_destination(projectiles[i],end_coords[i]):
      projectiles.remove(projectiles[0])
      end_coords.remove(end_coords[0])
      break
  
  
  for i in range(len(obstacle_movement)):
    coordinator = obstacle_movement[i]
    obstacle = obstacles[i]
    if coordinator['turn'] == 'left':
      if obstacle.left <= coordinator['left']:
        coordinator['turn'] = 'right'
      else:
        obstacle.left-=3
    elif coordinator['turn'] == 'right':
      if obstacle.left >= coordinator['right']:
        coordinator['turn'] = 'left'
      else: 
        obstacle.left+=3

  for i in range(len(obstacles)):
    obstacle = obstacles[i]  
    if projectiles != []:
      if obstacle.collidelist(projectiles) != -1:
        pygame.draw.rect(screen,'red',obstacle)
        obstacles.remove(obstacles[i])
        obstacle_movement.remove(obstacle_movement[i])
        break
      else:
        pygame.draw.rect(screen,'blue',obstacle)
    else:
      pygame.draw.rect(screen,'blue',obstacle)
      
      
  

    
  pygame.draw.rect(screen,'yellow',pygame.Rect(x,y,width,height))
  pygame.display.update()
pygame.quit()

