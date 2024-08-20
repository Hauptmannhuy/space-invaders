from dataclasses import dataclass

@dataclass
class Projectile:
    start_x: int
    start_y: int
    end_y: int
    
    def reached_destination(self):
      return True if self.start_y < self.end_y else False



