from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print"This scene is not yet configured. Subclass it and implement enter()."
        exit(1)        
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        
        
class Death(Scene):

    def enter(self):
        pass
        
class CentralCorridor(Scene):

    def enter(self):
        pass
        
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class  TheBridge(Scene):
    
    def enter(self):
        enter
        
class EscapePod(Scene):

    def enter(self):
        pass
        

class Map(object):

    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
a_map = Map('centra;_corridor')
a_game = Engine(a_map)
a_game.play()

print '*' * 10, "Test successful", '*' * 10