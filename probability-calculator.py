import copy
import random
from collections import Counter

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, num_balls_drawn):
    drawn_balls = []
    if num_balls_drawn >= len(self.contents):
        drawn_balls = self.contents
        self.contents = []
    else:
        drawn_balls = random.sample(self.contents, num_balls_drawn)
        for ball in drawn_balls:
            self.contents.remove(ball)
    return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  for _ in range(num_experiments):
      hat_copy = copy.deepcopy(hat)
      drawn_balls = hat_copy.draw(num_balls_drawn)
      color_count = Counter(drawn_balls)
      color_dict = dict(color_count)
  
      # Check if expected_balls are contained within color_dict
      if all(color_dict.get(color, 0) >= count for color, count in expected_balls.items()):
          success_count += 1
        
  return success_count / num_experiments
