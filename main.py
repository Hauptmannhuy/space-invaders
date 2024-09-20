import pygame
import random

pygame.init()


class Player:
  def __init__(self,y,x,width,height) -> None:
    self.rect = pygame.Rect(x,y,width,height)
    self.width, self.height = width, height
    
  def move(self,screen):
    keys = pygame.key.get_pressed()
    x,y = screen.get_size()
    left = 0
    top = 0
    if keys[pygame.K_w]:
      top -= 8
    elif keys[pygame.K_s]:
      top += 8
    elif keys[pygame.K_a]:
      left -= 8
    elif keys[pygame.K_d]:
      left += 8
    if self.player_crossing_border(x,y,left,top) is False:
      self.rect.top += top
      self.rect.left += left
  
  def draw(self,surface):
    pygame.draw.rect(surface,'yellow',self.rect)
    
  def player_crossing_border(self,x,y,left,top):
    if self.rect.left+left > x-60 or self.rect.left+left <= 0:
      return True
    elif self.rect.top+top < y*70/100 or self.rect.top+top > y-50 or self.rect.top+top <= 0:
      return True
    else: 
      return False
  
      
class Projectile:
  def __init__(self, y, x, width, height, destination) -> None:
    self.rect = pygame.Rect(x,y,width,height)
    self.destination = destination - 850
  
  def reached_destination(self):
    return True if self.rect.top < self.destination else False
  
  def draw(self, surface):
    pygame.draw.rect(surface,'red', self.rect)
  
class Obstacle:
  def __init__(self, x, y, width, height) -> None:
    self.rect = pygame.Rect(x, y, width, height)
    self.left_move = x - 150
    self.right_move = x + 150
    self.turn = 'left'
    
  def draw(self, surface, color):
    pygame.draw.rect(surface, color, self.rect)
  
  
obstacle_movement = []
obstacles = []

x,y = 1000,1000
width,height = 50,50

projectiles = []

player = Player(y,x,width,height)
screen = pygame.display.set_mode((1920,1080))
running = True
print(screen.get_size())

for _ in range(6):
  obstacle = Obstacle(random.randrange(0,1920),0,30,30)
  obstacles.append(obstacle)
  
fps = pygame.time.Clock()


while (running):
  fps.tick(40)
  
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        start_projectile_x = player.rect.left+player.rect.width/2
        start_projectile_y = player.rect.top
        destination = player.rect.top
        projectile = Projectile(start_projectile_y, start_projectile_x, 5, 15, destination)      
        projectiles.append(projectile)
  
  player.move(screen)

  screen.fill('black')

            
  for i in range(len(projectiles)):
    projectile = projectiles[i]
    if projectile.reached_destination() is False:     
      projectile.rect.top-=20
      projectile.draw(screen)
  
  for i in range(len(projectiles)):
    if projectiles[i].reached_destination():
      projectiles.remove(projectiles[0])
      break
  
  
  for i in range(len(obstacles)):
    obstacle = obstacles[i]
    obstacle_x = obstacle.rect.left
    if obstacle.turn == 'right':
      if obstacle.right_move <= obstacle.rect.left:
        obstacle.turn = 'left'
      else:
        obstacle.rect.left += 3
    elif obstacle.turn == 'left':
      if obstacle.left_move >= obstacle.rect.left:
        obstacle.turn = 'right'
      else: 
        obstacle.rect.left -= 3

  for i in range(len(obstacles)):
    obstacle = obstacles[i]  
    if projectiles != []:
      if obstacle.rect.collidelist(projectiles) != -1:
        obstacle.draw(screen,'red')
        obstacles.remove(obstacles[i])
        break
      else:
        obstacle.draw(screen,'blue')
    else:
      obstacle.draw(screen,'blue')
      
  player.draw(screen)
  pygame.display.update()
pygame.quit()

