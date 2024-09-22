import pygame

pygame.init()


class Player:
  def __init__(self,y,x,width,height) -> None:
    self.rect = pygame.Rect(x,y,width,height)
    self.width, self.height = width, height
    self.projectiles = []
    
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
      
  def shoot(self):
    start_projectile_x = player.rect.left+player.rect.width/2
    start_projectile_y = player.rect.top
    destination = player.rect.top - 850
    projectile = Projectile(start_projectile_y, start_projectile_x, 5, 15, destination)      
    self.projectiles.append(projectile)
    
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
  def __init__(self, y, x, width, height, destination,direction='up') -> None:
    self.rect = pygame.Rect(x,y,width,height)
    self.destination = destination
    self.direction = direction
    self.movespan_end = False
  
  def reached_destination(self, target):
      if self.direction == 'up':
        if self.rect.top < self.destination:
          return True
      elif self.direction == 'down':
        if self.rect.top > self.destination:
          return True
        
      if self.rect.collidelist(target) != -1:
        return True
      else:
        return False
  
  def update(self, target):
    if self.reached_destination(target):
      self.movespan_end = True
      return
    
    if self.direction == 'up':
      self.rect.top -= 20
    else:
      self.rect.top += 20
    
  
  def draw(self, surface):
    pygame.draw.rect(surface,'red', self.rect)
  
class Invader:
  def __init__(self, x, y, width, height) -> None:
    self.rect = pygame.Rect(x, y, width, height)
    self.left_move = x - 150
    self.right_move = x + 150
    self.hit = False
    self.turn = 'left'
    
  def draw(self, surface, color):
    pygame.draw.rect(surface, color, self.rect)
  

x,y = 1000,1000
width,height = 50,50

invaders = []

player = Player(y,x,width,height)
screen = pygame.display.set_mode((1920,1080))
running = True


initial_y_obst = 10
for _ in range(5):
  initial_x_obst = 0 + screen.get_size()[1]/2
  for _ in range(10):
    invader = Invader(initial_x_obst,initial_y_obst,30,30)
    invaders.append(invader)
    initial_x_obst+=50
  initial_y_obst+=50
    
  
fps = pygame.time.Clock()

def remove_expired_projectiles(projectiles):
  for projectile in projectiles:
    if projectile.movespan_end == True:
      projectiles.remove(projectile)
      
def update_projectiles(projectiles, target):
  for projectile in projectiles:
    projectile.update(target)
      

def invader_got_hit(invaders,projectiles):
  for i in range(len(invaders)):
    invader = invaders[i]  
    if projectiles != []:
      if invader.rect.collidelist(projectiles) != -1:
        invader.hit = True
        
def update_invader_movement(invaders):  
  for i in range(len(invaders)):
    invader = invaders[i]
    if invader.turn == 'right':
      if invader.right_move <= invader.rect.left:
        invader.turn = 'left'
      else:
        invader.rect.left += 3
    elif invader.turn == 'left':
      if invader.left_move >= invader.rect.left:
        invader.turn = 'right'
      else: 
        invader.rect.left -= 3

def draw_invaders(screen, invaders):
  for invader in invaders:
    color = 'blue' if invader.hit == False else 'red'
    invader.draw(screen, color)
    
def remove_hitted_invaders(invaders):
  for invader in invaders:
    if invader.hit == True:
      invaders.remove(invader)
      
def draw_projectiles(projectiles):
  for projectile in projectiles:
    if projectile.movespan_end == False:
      projectile.draw(screen)

while (running):
  fps.tick(60)
  
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.shoot()
  
  player.move(screen)

  screen.fill('black')

  
          
  update_invader_movement(invaders)
  invader_got_hit(invaders, player.projectiles)
  update_projectiles(player.projectiles, invaders)
  
  player.draw(screen)
  draw_projectiles(player.projectiles)
  draw_invaders(screen, invaders)    
  
  remove_expired_projectiles(player.projectiles)
  remove_hitted_invaders(invaders)
  pygame.display.update()
pygame.quit()

