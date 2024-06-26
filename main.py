import random

class Student:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.progress = 0
    self.alive = True

  def to_study(self):
    print("Time to study")
    self.progress += 0.15
    self.gladness -= 3

  def to_sleep(self):
    print("Time to sleep")
    self.gladness += 3

  def to_chill(self):
    print("Time to chill")
    self.gladness += 5
    self.progress -= 0.1

  def is_alive(self):
    if self.progress < -0.5:
      print("Sorry, but you failed")
      self.alive = False
    elif self.gladness <= 0:
      print("Sorry, but you are depressed")
      self.alive = False
    elif self.progress > 5:
      print("Congratulations! You have passed the exam")
      self.alive = False

    def end_of_day(self):
      print(f"Gladness = {round(self.gladness, 2)}")
      print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
      day = f"Day {day} of {self.name} life"
      print(f"{day:=^40}")
      live_cube = random.randint(1, 3)
      if live_cube == 1:
        self.to_study()
      elif live_cube == 2:
        self.to_sleep()
      elif live_cube == 3:
        self.to_chill()
      self.end_of_day()
      self.is_alive()

nick = Student("Vasya")
for day in range(1, 366):
  if nick.alive == False:
    break
